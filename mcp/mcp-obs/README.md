# MCP Observability Server

MCP server providing tools for querying VictoriaLogs and VictoriaTraces.

## Tools

- `logs_search` - Search logs using LogsQL
- `logs_error_count` - Count errors for a service
- `traces_list` - List recent traces
- `traces_get` - Get full trace details

## Usage

```bash
uv run python -m mcp_obs
```

## Environment Variables

- `VICTORIALOGS_URL` - VictoriaLogs endpoint (default: http://victorialogs:9428)
- `VICTORIATRACES_URL` - VictoriaTraces endpoint (default: http://victoriatraces:10428)
