# Observability Skill

## CRITICAL: Evidence Citation Requirement

When responding to "What went wrong?", you **MUST** include direct quotes from logs and traces:

You have access to observability tools that can query VictoriaLogs and VictoriaTraces. Use these tools to investigate system health, errors, and request traces.

## Available Tools

### Log Tools (VictoriaLogs)

- **`mcp_obs_logs_search`** — Search logs using LogsQL queries
  - Use for finding specific events, errors, or patterns
  - Time range: use `time_range` like "10m", "1h" (e.g., `_time:10m`)
  - Default limit: 50 entries
  - Example query: `service.name:"Learning Management Service" severity:ERROR`

- **`mcp_obs_logs_error_count`** — Count errors per service
  - Use as **first step** when asked about errors or "what went wrong"
  - Returns count grouped by service
  - Default time window: 10 minutes

### Trace Tools (VictoriaTraces)

- **`mcp_obs_traces_list`** — List recent traces for a service
  - Returns trace summaries with: trace_id, duration, span_count, status (ok/error)
  - Default service: "Learning Management Service"
  - Use to find traces to investigate

- **`mcp_obs_traces_get`** — Get full trace details by ID
  - Returns complete span hierarchy with errors highlighted
  - **CRITICAL:** You MUST call this if you find a trace_id in logs
  - Use after finding a trace_id from logs_search

---

## Investigation Flow for "What went wrong?"

When the user asks **"What went wrong?"**, **"Check system health"**, or asks about errors/failures, follow this **exact flow**:

### Step 1: Count Recent Errors (REQUIRED - First Step)

Call `mcp_obs_logs_error_count` with a **fresh, narrow time window**:

```
mcp_obs_logs_error_count(service="Learning Management Service", time_range="10m")
```

This tells you which services have recent errors. If count > 0, proceed to Step 2.

### Step 2: Search Error Logs (REQUIRED - Second Step)

Call `mcp_obs_logs_search` to find specific error logs:

```
mcp_obs_logs_search(query='service.name:"Learning Management Service" severity:ERROR', time_range="10m", limit=20)
```

**Look for:**
- Error messages (exception.message, db.statement, error)
- **`trace_id`** fields in the log entries ← **EXTRACT THIS**

### Step 3: Fetch the Trace (REQUIRED - Third Step)

**If you found a `trace_id` in Step 2, you MUST call:**

```
mcp_obs_traces_get(trace_id="<trace_id_from_logs>")
```

This shows the full request flow and where it failed. **Do not skip this step.**

### Step 4: Check Backend Health (Optional - Fourth Step)

Call `mcp_lms_lms_health` to verify current backend status.

### Step 5: Summarize Findings (REQUIRED - Final Step)

Write a **single coherent investigation** that includes:

1. **Log evidence**: Quote at least one error message from logs (include timestamp)
2. **Trace evidence**: Name the failing operation from the trace (include trace_id)
3. **Affected service**: Explicitly name the service (e.g., "Learning Management Service")
4. **Root cause**: Explain what actually failed (e.g., "PostgreSQL hostname resolution failed")
5. **Discrepancy (if any)**: Note any mismatch between actual error and reported HTTP status

---

## Response Templates

### For "What went wrong?" investigations:

```
**Root Cause:** <one-sentence explanation of what failed>

**Log Evidence:**
- Found X errors in the last 10 minutes for <service>
- Error at <timestamp>: "<specific error message>"
- The error occurred during <operation>

**Trace Evidence:**
- Trace `<trace_id>` shows:
  - [<span1>]: OK
  - [<span2>]: FAILED after Xms with error: <error details>

**Affected:** <service> - <specific operation>

**Discrepancy:** <note if HTTP status doesn't match the error, e.g., "Backend returned 404 but the real issue is PostgreSQL down">

**Recommendation:** <what to fix>
```

### Example Good Response:

> **Root Cause:** The LMS backend failed because PostgreSQL is unreachable.
>
> **Log Evidence:**
> - Found 5 errors in the last 10 minutes for Learning Management Service
> - Error at 15:24:37: `socket.gaierror: [Errno -2] Name or service not known` when connecting to `postgres:5432`
> - The error occurred during `db_query` operation
>
> **Trace Evidence:**
> - Trace `2e282ae8e5702832657ffbec701963cf` shows:
>   - `[Learning Management Service] request_started`: OK
>   - `[Learning Management Service] db_query`: **FAILED** after 197ms with `error: true`
>
> **Affected:** Learning Management Service - database connection layer
>
> **Discrepancy:** The backend returned HTTP 404 "Items not found", but the real issue is PostgreSQL being unavailable (connection failure, not missing data). This should be 503 Service Unavailable, not 404.
>
> **Recommendation:** Restart PostgreSQL or fix the database connection configuration.

### For General Health Checks:

```
**System Health Status:**

- **<Service>:** <status>
  - Errors in last 10 minutes: X
  - Recent traces: all OK / X failed

**Summary:** <one-sentence summary>
```

---

## Query Examples

### Find LMS backend errors in the last 10 minutes:
```
mcp_obs_logs_error_count(service="Learning Management Service", time_range="10m")
```

### Search for specific error pattern:
```
mcp_obs_logs_search(query='service.name:"Learning Management Service" severity:ERROR', time_range="10m", limit=20)
```

### Fetch a specific trace:
```
mcp_obs_traces_get(trace_id="2e282ae8e5702832657ffbec701963cf")
```

---

## Common Error Patterns

| Error message | Likely cause |
|--------------|--------------|
| `Name or service not known` | Service discovery failure (target service down) |
| `Connection refused` | Service running but port not accessible |
| `Connection timeout` | Network issue or overloaded service |
| `db_query failed` | Database connection or query error |
| `socket.gaierror` | DNS/hostname resolution failure |
| `SQLAlchemy` errors | Database ORM layer failure |

---

## Critical Rules

### You MUST:
- ✅ Call `mcp_obs_logs_error_count` **first** when investigating errors
- ✅ Call `mcp_obs_logs_search` **second** to find specific error messages
- ✅ Call `mcp_obs_traces_get` if you find a `trace_id` in the logs
- ✅ Quote **specific error messages** from logs (include timestamps)
- ✅ Name the **failing operation** from the trace
- ✅ Note any **discrepancy** between the real error and HTTP status

### You MUST NOT:
- ❌ Dump raw JSON responses - summarize in plain language
- ❌ Skip the trace investigation if `trace_id` is available
- ❌ Report old errors - use fresh time windows (10m, not 1h)
- ❌ Give generic answers like "service is down" without citing evidence
- ❌ Say "I don't have access to logs" - you DO have access via MCP tools

---

## Troubleshooting

### If tools return errors:
1. Try again with a narrower time window
2. Check if the service name is correct: "Learning Management Service"
3. Report the tool error to the user but still provide what info you have

### If no errors found:
1. Widen the time window (try "1h" instead of "10m")
2. Check if the service name matches exactly
3. Report "No errors found in the last X minutes" clearly

### If trace_id not found in logs:
1. Use `mcp_obs_traces_list` to find recent traces
2. Pick a trace with status="error" and fetch it with `mcp_obs_traces_get`

### DO NOT say:
- ❌ "The backend is down" (without citing evidence)
- ❌ "Multiple failures detected" (without specific errors)
- ❌ "This could be due to..." (without data)

### DO say:
- ✅ "At 17:14:37, logs show: 'socket.gaierror: Name or service not known'"
- ✅ "Trace a8a4fcc2eb92351e failed at span 'db_query' after 197ms"
- ✅ "The backend returned 404, but logs show PostgreSQL connection failure"
