---
name: observability
description: Use observability tools to search logs and traces for errors and debugging
always: true
---

# Observability Skill

You have access to observability tools that can search logs and traces from VictoriaLogs and VictoriaTraces.

## Available Tools

### Log Tools
- `mcp_obs_logs_search` - Search logs using LogsQL queries
- `mcp_obs_logs_error_count` - Count errors for a service over a time window

### Trace Tools
- `mcp_obs_traces_list` - List recent traces for a service
- `mcp_obs_traces_get` - Get full details of a specific trace by ID

## When to Use These Tools

Use observability tools when the user asks about:
- Errors, failures, or issues in the system
- What went wrong with a request
- System health or status
- Debugging a problem
- Recent activity in a service

## Strategy for Error Investigation

When the user asks about errors (e.g., "Any errors in the last hour?"):

1. **First**, use `mcp_obs_logs_error_count` with:
   - `service`: "Learning Management Service" (or the service the user asks about)
   - `time_range`: Use the time range the user mentioned, or default to "10m" for recent issues

2. **If errors are found**, use `mcp_obs_logs_search` to see the actual error messages:
   - `query`: 'service.name:"Learning Management Service" severity:ERROR'
   - `time_range`: Same as step 1
   - `limit`: 10-20 entries is usually enough

3. **Look for trace_id** in the log entries. If you find one, use `mcp_obs_traces_get` to see the full request flow and where it failed.

4. **Summarize findings** concisely:
   - How many errors occurred
   - What the errors were (brief description)
   - What component failed (from trace spans)
   - Any patterns you notice

## Strategy for Trace Investigation

When you have a specific trace_id (from logs or user input):

1. Use `mcp_obs_traces_get` with the trace_id
2. Look at the span hierarchy to understand the request flow
3. Identify which span has the error (marked with ⚠️ ERROR)
4. Explain what went wrong in plain language

## Response Format

- Keep responses concise and focused on the user's question
- Don't dump raw JSON - summarize the findings
- Include relevant details like timestamps, error messages, and affected components
- If no errors are found, say so clearly

## Examples

**User**: "Any errors in the last hour?"

**You should**:
1. Call `mcp_obs_logs_error_count` with time_range="1h"
2. If count > 0, call `mcp_obs_logs_search` to see details
3. Summarize: "Found X errors in the last hour. The errors were: [brief description]"

**User**: "What went wrong with request abc123?"

**You should**:
1. Call `mcp_obs_traces_get` with trace_id="abc123"
2. Look for spans with errors
3. Explain: "The request failed at [component] because [reason]"

**User**: "Is the backend healthy?"

**You should**:
1. Call `mcp_obs_logs_error_count` with service="Learning Management Service" and time_range="10m"
2. If no errors: "The backend appears healthy - no errors in the last 10 minutes"
3. If errors: Report them and offer to investigate further

## Important Notes

- Always specify the service name when querying - "Learning Management Service" for the LMS backend
- Use narrow time ranges (10m, 1h) for recent issues, wider ranges (1d) for historical analysis
- If a tool fails, try again or explain the limitation to the user
- When in doubt, start with `logs_error_count` to get a quick overview before diving into details
