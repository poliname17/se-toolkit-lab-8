"""VictoriaLogs and VictoriaTraces API client."""

import httpx


class ObservabilityClient:
    """Client for querying VictoriaLogs and VictoriaTraces."""

    def __init__(
        self,
        victorialogs_url: str = "http://localhost:9428",
        victoriatraces_url: str = "http://localhost:10428",
    ):
        self.victorialogs_url = victorialogs_url.rstrip("/")
        self.victoriatraces_url = victoriatraces_url.rstrip("/")

    async def logs_search(
        self, query: str, limit: int = 50, time_range: str = "1h"
    ) -> list[dict]:
        """
        Search logs in VictoriaLogs using LogsQL.

        Args:
            query: LogsQL query string (e.g., 'severity:ERROR')
            limit: Maximum number of results
            time_range: Time range like '1h', '10m', '1d'

        Returns:
            List of log entries
        """
        url = f"{self.victorialogs_url}/select/logsql/query"
        params = {
            "query": f"_time:{time_range} {query}",
            "limit": limit,
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params, timeout=30.0)
            response.raise_for_status()
            return response.json()

    async def logs_error_count(
        self, service: str = "Learning Management Service", time_range: str = "1h"
    ) -> dict:
        """
        Count errors per service over a time window.

        Args:
            service: Service name to filter
            time_range: Time range like '1h', '10m', '1d'

        Returns:
            Dict with error count
        """
        query = f'service.name:"{service}" severity:ERROR'
        url = f"{self.victorialogs_url}/select/logsql/query"
        params = {
            "query": f"_time:{time_range} {query}",
            "limit": 1000,
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params, timeout=30.0)
            response.raise_for_status()
            data = response.json()
            # Count the number of error entries
            count = len(data) if isinstance(data, list) else 0
            return {"service": service, "error_count": count, "time_range": time_range}

    async def traces_list(
        self, service: str = "Learning Management Service", limit: int = 20
    ) -> list[dict]:
        """
        List recent traces for a service.

        Args:
            service: Service name
            limit: Maximum number of traces

        Returns:
            List of trace summaries
        """
        url = f"{self.victoriatraces_url}/select/jaeger/api/traces"
        params = {
            "service": service,
            "limit": limit,
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params, timeout=30.0)
            response.raise_for_status()
            data = response.json()
            # Jaeger API returns {"data": [...]}
            if isinstance(data, dict) and "data" in data:
                return data["data"]
            return data if isinstance(data, list) else []

    async def traces_get(self, trace_id: str) -> dict:
        """
        Fetch a specific trace by ID.

        Args:
            trace_id: The trace ID to fetch

        Returns:
            Full trace data with spans
        """
        url = f"{self.victoriatraces_url}/select/jaeger/api/traces/{trace_id}"

        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=30.0)
            response.raise_for_status()
            data = response.json()
            # Jaeger API returns {"data": [...]}
            if isinstance(data, dict) and "data" in data:
                traces = data["data"]
                return traces[0] if traces else {}
            return data if isinstance(data, list) else (data if data else {})
