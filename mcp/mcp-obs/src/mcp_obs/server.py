"""MCP server for observability tools."""

import asyncio
from mcp.server.fastmcp import FastMCP

from .observability import ObservabilityClient

mcp = FastMCP("observability")

# Global client instance
_client: ObservabilityClient | None = None


def get_client() -> ObservabilityClient:
    """Get or create the observability client."""
    global _client
    if _client is None:
        import os

        victorialogs_url = os.environ.get(
            "VICTORIALOGS_URL", "http://victorialogs:9428"
        )
        victoriatraces_url = os.environ.get(
            "VICTORIATRACES_URL", "http://victoriatraces:10428"
        )
        _client = ObservabilityClient(
            victorialogs_url=victorialogs_url,
            victoriatraces_url=victoriatraces_url,
        )
    return _client


@mcp.tool()
async def logs_search(
    query: str = "severity:ERROR",
    limit: int = 50,
    time_range: str = "10m",
) -> str:
    """
    Search logs in VictoriaLogs using LogsQL.

    Use this to find specific log entries by keyword, severity, or service.

    Args:
        query: LogsQL query (e.g., 'severity:ERROR', 'service.name:"Learning Management Service"')
        limit: Maximum number of results (default: 50)
        time_range: Time range like '10m', '1h', '1d' (default: 10m)

    Returns:
        Formatted log entries
    """
    try:
        client = get_client()
        results = await client.logs_search(
            query=query, limit=limit, time_range=time_range
        )

        if not results:
            return "No log entries found matching your query."

        # Format results
        lines = [f"Found {len(results)} log entries:\n"]
        for entry in results[:10]:  # Show first 10
            if isinstance(entry, dict):
                timestamp = entry.get("_time", entry.get("timestamp", "N/A"))
                severity = entry.get("severity", entry.get("level", "N/A"))
                service = entry.get("service.name", entry.get("service", "N/A"))
                message = entry.get("message", entry.get("msg", str(entry)))
                lines.append(
                    f"[{timestamp}] {severity} - {service}: {message[:200]}"
                )
            else:
                lines.append(str(entry)[:200])

        if len(results) > 10:
            lines.append(f"\n... and {len(results) - 10} more entries")

        return "\n".join(lines)
    except Exception as e:
        return f"Error searching logs: {e}"


@mcp.tool()
async def logs_error_count(
    service: str = "Learning Management Service",
    time_range: str = "10m",
) -> str:
    """
    Count errors for a service over a time window.

    Use this first when the user asks about errors to get a quick count.

    Args:
        service: Service name (default: "Learning Management Service")
        time_range: Time range like '10m', '1h', '1d' (default: 10m)

    Returns:
        Error count summary
    """
    try:
        client = get_client()
        result = await client.logs_error_count(
            service=service, time_range=time_range
        )

        count = result.get("error_count", 0)
        if count == 0:
            return f"No errors found for '{service}' in the last {time_range}."
        else:
            return f"Found {count} error(s) for '{service}' in the last {time_range}. Use logs_search to see details."
    except Exception as e:
        return f"Error counting errors: {e}"


@mcp.tool()
async def traces_list(
    service: str = "Learning Management Service",
    limit: int = 10,
) -> str:
    """
    List recent traces for a service.

    Args:
        service: Service name (default: "Learning Management Service")
        limit: Maximum number of traces (default: 10)

    Returns:
        Formatted list of traces
    """
    try:
        client = get_client()
        traces = await client.traces_list(service=service, limit=limit)

        if not traces:
            return f"No traces found for '{service}'."

        lines = [f"Found {len(traces)} recent trace(s) for '{service}':\n"]
        for i, trace in enumerate(traces[:5], 1):  # Show first 5
            trace_id = trace.get("traceID", "unknown")
            spans = len(trace.get("spans", []))
            start_time = trace.get("startTime", 0)
            duration = trace.get("duration", 0)
            lines.append(
                f"{i}. Trace ID: {trace_id[:16]}... | Spans: {spans} | Duration: {duration / 1000000:.2f}ms"
            )

        if len(traces) > 5:
            lines.append(f"\n... and {len(traces) - 5} more traces")

        lines.append(
            "\nUse traces_get with a trace_id to see full details including span hierarchy."
        )

        return "\n".join(lines)
    except Exception as e:
        return f"Error listing traces: {e}"


@mcp.tool()
async def traces_get(trace_id: str) -> str:
    """
    Fetch a specific trace by ID and show span hierarchy.

    Use this after finding a trace_id from logs_search or traces_list.

    Args:
        trace_id: The trace ID to fetch

    Returns:
        Formatted trace with span hierarchy
    """
    try:
        client = get_client()
        trace = await client.traces_get(trace_id=trace_id)

        if not trace:
            return f"Trace {trace_id} not found."

        trace_id_full = trace.get("traceID", trace_id)
        spans = trace.get("spans", [])

        lines = [
            f"Trace: {trace_id_full[:16]}...",
            f"Total spans: {len(spans)}",
            "\nSpan hierarchy:",
        ]

        # Sort spans by start time
        sorted_spans = sorted(spans, key=lambda s: s.get("startTime", 0))

        for span in sorted_spans:
            operation = span.get("operationName", "unknown")
            duration = span.get("duration", 0) / 1000000  # Convert to ms
            service = span.get("process", {}).get("serviceName", "unknown")
            tags = span.get("tags", [])

            # Check for errors
            has_error = any(
                t.get("key") == "error" or t.get("key") == "error.message"
                for t in tags
            )
            error_marker = " ⚠️ ERROR" if has_error else ""

            lines.append(
                f"  - [{service}] {operation} ({duration:.2f}ms){error_marker}"
            )

        return "\n".join(lines)
    except Exception as e:
        return f"Error fetching trace: {e}"


def main():
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
