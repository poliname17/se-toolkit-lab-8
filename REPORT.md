# Lab 8 — Report

Paste your checkpoint evidence below. Add screenshots as image files in the repo and reference them with `![description](path)`.

## Task 1A — Bare agent

<!-- Paste the agent's response to "What is the agentic loop?" and "What labs are available in our LMS?" -->
Based on the search results, here's the answer to quiz question Q18:                                                                                                           

The Agentic Loop                                                                                                                                                               

The agentic loop is the core architectural pattern that distinguishes AI agents from simple chatbots. It's an iterative cycle where an AI agent:                               

 1 Perceives — Observes the environment or receives input                                                                                                                      
 2 Reasons — Processes information and plans actions using an LLM                                                                                                              
 3 Acts — Invokes tools or takes actions in the environment                                                                                                                    
 4 Evaluates — Assesses the results of its actions                                                                                                                             
 5 Repeats — Continues the loop until the task is complete or a stopping condition is reached                                                                                  

Key Characteristics:                                                                                                                                                           

 • Iterative: The agent repeats the cycle multiple times as needed                                                                                                             
 • Autonomous: Can operate semi- or fully independently without constant human input                                                                                           
 • Adaptive: Responds dynamically to what it finds in the environment                                                                                                          
 • Tool-using: The LLM invokes external tools within the loop to accomplish tasks                                                                                              

This architecture emerged from AI research in the 1980s-1990s focused on building systems that can operate in uncertain, dynamic environments. The agentic loop is what enables
AI agents to pursue goals autonomously rather than just responding to single prompts like traditional chatbots.  

Based on the workspace structure, here are the available labs in your LMS:                                                                                                     

Lab Structure                                                                                                                                                                  

Current Lab: se-toolkit-lab-8                                                                                                                                                  

Tasks Available:                                                                                                                                                               

Required Tasks:                                                                                                                                                                

 • task-1.md                                                                                                                                                                   
 • task-2.md                                                                                                                                                                   
 • task-3.md                                                                                                                                                                   
 • task-4.md                                                                                                                                                                   
 • task-5.md                                                                                                                                                                   

Optional Tasks:                                                                                                                                                                

 • task-1.md                                                                                                                                                                   

Lab Resources:                                                                                                                                                                 

 • Wiki documentation (/wiki/) - Contains guides on various topics like:                                                                                                       
    • Git workflow, Docker, PostgreSQL, Python, Node.js                                                                                                                        
    • API development, frontend/backend setup                                                                                                                                  
    • Linux administration, security, and more                                                                                                                                 
 • Lab setup (/lab/setup/) - Setup instructions                                                                                                                                
 • Lab images (/lab/images/) - Visual resources                                                                                                                                

The lab appears to be a Software Engineering Toolkit where you work through tasks with the help of:                                                                            

 • TA supervision                                                                                                                                                              
 • Classmates collaboration                                                                                                                                                    
 • AI assistants (chatbots, coding agents)                                                                                                                                     

Would you like me to help you with a specific task or explore the lab documentation further?    

## Task 1B — Agent with LMS tools

<!-- Paste the agent's response to "What labs are available?" and "Describe the architecture of the LMS system" -->
Based on the LMS system, here are the available labs:


 ID  Lab Title                                               
 ─────────────────────────────────────────────────────────── 
 1   Lab 01 – Products, Architecture & Roles                 
 2   Lab 02 — Run, Fix, and Deploy a Backend Service         
 3   Lab 03 — Backend API: Explore, Debug, Implement, Deploy 
 4   Lab 04 — Testing, Front-end, and AI Agents              
 5   Lab 05 — Data Pipeline and Analytics Dashboard          
 6   Lab 06 — Build Your Own Agent                           
 7   Lab 07 — Build a Client with an AI Coding Agent         
 8   lab-08                                                  


There are 8 labs available. Would you like to see scores, pass rates, or other details for any specific lab?

Yes, the LMS backend is healthy. It currently contains 56 items.

## Task 1C — Skill prompt

<!-- Paste the agent's response to "Show me the scores" (without specifying a lab) -->
Which lab would you like to see the scores for? Here are the available labs:

 1 Lab 01 – Products, Architecture & Roles
 2 Lab 02 — Run, Fix, and Deploy a Backend Service
 3 Lab 03 — Backend API: Explore, Debug, Implement, Deploy
 4 Lab 04 — Testing, Front-end, and AI Agents
 5 Lab 05 — Data Pipeline and Analytics Dashboard
 6 Lab 06 — Build Your Own Agent
 7 Lab 07 — Build a Client with an AI Coding Agent
 8 Lab 08 — lab-08

Please let me know which lab you're interested in, or I can show you pass rates, completion rates, top learners, or group performance for a specific lab.                                                                                

## Task 2A — Deployed agent

<!-- Paste a short nanobot startup log excerpt showing the gateway started inside Docker -->

operator1@polinaVM2001:~/se-toolkit-lab-8$ docker compose --env-file .env.docker.secret logs nanobot --tail 30
nanobot-1  | 
nanobot-1  | 2026-03-31 18:57:38.361 | INFO     | nanobot.agent.loop:stop:387 - Agent loop stopping
nanobot-1  | 2026-03-31 18:57:38.362 | INFO     | nanobot.channels.manager:stop_all:99 - Stopping all channels...
nanobot-1  | 2026-03-31 18:57:38.362 | INFO     | nanobot.channels.manager:stop_all:113 - Stopped webchat channel
nanobot-1  | Using config: /tmp/nanobot/config.resolved.json
nanobot-1  | Using config: /tmp/nanobot/config.resolved.json
nanobot-1  | 🐈 Starting nanobot gateway version 0.1.4.post5 on port 18790...
nanobot-1  | 2026-03-31 18:58:09.564 | DEBUG    | nanobot.channels.registry:discover_all:64 - Skipping built-in channel 'matrix': Matrix dependencies not installed. Run: pip install nanobot-ai[matrix]
nanobot-1  | 2026-03-31 18:58:09.998 | INFO     | nanobot.channels.manager:_init_channels:58 - WebChat channel enabled
nanobot-1  | ✓ Channels enabled: webchat
nanobot-1  | ✓ Heartbeat: every 1800s
nanobot-1  | 2026-03-31 18:58:10.000 | INFO     | nanobot.cron.service:start:202 - Cron service started with 0 jobs
nanobot-1  | 2026-03-31 18:58:10.000 | INFO     | nanobot.heartbeat.service:start:124 - Heartbeat started (every 1800s)
nanobot-1  | 2026-03-31 18:58:10.349 | INFO     | nanobot.channels.manager:start_all:91 - Starting webchat channel...
nanobot-1  | 2026-03-31 18:58:10.350 | INFO     | nanobot.channels.manager:_dispatch_outbound:119 - Outbound dispatcher started
nanobot-1  | 2026-03-31 18:58:12.049 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_health' from server 'lms'
nanobot-1  | 2026-03-31 18:58:12.049 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_labs' from server 'lms'
nanobot-1  | 2026-03-31 18:58:12.049 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_learners' from server 'lms'
nanobot-1  | 2026-03-31 18:58:12.049 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_pass_rates' from server 'lms'
nanobot-1  | 2026-03-31 18:58:12.049 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_timeline' from server 'lms'
nanobot-1  | 2026-03-31 18:58:12.049 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_groups' from server 'lms'
nanobot-1  | 2026-03-31 18:58:12.049 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_top_learners' from server 'lms'
nanobot-1  | 2026-03-31 18:58:12.049 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_completion_rate' from server 'lms'
nanobot-1  | 2026-03-31 18:58:12.049 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_sync_pipeline' from server 'lms'
nanobot-1  | 2026-03-31 18:58:12.049 | INFO     | nanobot.agent.tools.mcp:connect_mcp_servers:246 - MCP server 'lms': connected, 9 tools registered
nanobot-1  | 2026-03-31 18:58:13.774 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_webchat_ui_message' from server 'webchat'
nanobot-1  | 2026-03-31 18:58:13.774 | INFO     | nanobot.agent.tools.mcp:connect_mcp_servers:246 - MCP server 'webchat': connected, 1 tools registered
nanobot-1  | /app/.venv/bin/python: No module named mcp_obs
nanobot-1  | 2026-03-31 18:58:13.814 | ERROR    | nanobot.agent.tools.mcp:connect_mcp_servers:248 - MCP server 'obs': failed to connect: Connection closed
nanobot-1  | 2026-03-31 18:58:13.814 | INFO     | nanobot.agent.loop:run:280 - Agent loop started

## Task 2B — Web client

<!-- Screenshot of a conversation with the agent in the Flutter web app -->
No labs found. Let me trigger the LMS sync pipeline first as you requested.
The sync pipeline is running (it may take a moment). Let me check for labs again:
Great! The sync completed and now we have 8 labs available. Since you asked for scores, which lab would you like to see?
The interactive UI isn't available on this channel. Let me present the options as text:

**Which lab would you like to see scores for?**

1. Lab 01 – Products, Architecture & Roles (`lab-01`)
2. Lab 02 — Run, Fix, and Deploy a Backend Service (`lab-02`)
3. Lab 03 — Backend API: Explore, Debug, Implement, Deploy (`lab-03`)
4. Lab 04 — Testing, Front-end, and AI Agents (`lab-04`)
5. Lab 05 — Data Pipeline and Analytics Dashboard (`lab-05`)
6. Lab 06 — Build Your Own Agent (`lab-06`)
7. Lab 07 — Build a Client with an AI Coding Agent (`lab-07`)
8. lab-08 (`lab-08`)

Just tell me which lab number or ID you'd like to see!
![alt text](screenshots/image.png)
## Task 3A — Structured logging

<!-- Paste happy-path and error-path log excerpts, VictoriaLogs query screenshot -->
backend-1  | 2026-03-31 19:44:35,601 INFO [lms_backend.main] [main.py:62] [trace_id=79b9cb769ab05f29b629b4de5bcd0198 span_id=2b5e71670949512c resource.service.name=Learning Management Service trace_sampled=True] - request_started
backend-1  | 2026-03-31 19:44:35,604 INFO [lms_backend.auth] [auth.py:30] [trace_id=79b9cb769ab05f29b629b4de5bcd0198 span_id=2b5e71670949512c resource.service.name=Learning Management Service trace_sampled=True] - auth_success
backend-1  | 2026-03-31 19:44:35,616 INFO [lms_backend.main] [main.py:74] [trace_id=79b9cb769ab05f29b629b4de5bcd0198 span_id=2b5e71670949512c resource.service.name=Learning Management Service trace_sampled=True] - request_completed

backend-1  | 2026-03-31 20:15:20,904 INFO [lms_backend.main] [main.py:62] [trace_id=e5068c0642f0bdd994ff3532bcf41977 span_id=376fb4e98f961ba2 resource.service.name=Learning Management Service trace_sampled=True] - request_started
backend-1  | 2026-03-31 20:15:20,906 INFO [lms_backend.auth] [auth.py:30] [trace_id=e5068c0642f0bdd994ff3532bcf41977 span_id=376fb4e98f961ba2 resource.service.name=Learning Management Service trace_sampled=True] - auth_success
backend-1  | 2026-03-31 20:15:20,906 INFO [lms_backend.db.items] [items.py:16] [trace_id=e5068c0642f0bdd994ff3532bcf41977 span_id=376fb4e98f961ba2 resource.service.name=Learning Management Service trace_sampled=True] - db_query
backend-1  | 2026-03-31 20:15:20,909 ERROR [lms_backend.db.items] [items.py:23] [trace_id=e5068c0642f0bdd994ff3532bcf41977 span_id=376fb4e98f961ba2 resource.service.name=Learning Management Service trace_sampled=True] - db_query
backend-1  | 2026-03-31 20:15:20,909 WARNING [lms_backend.routers.items] [items.py:23] [trace_id=e5068c0642f0bdd994ff3532bcf41977 span_id=376fb4e98f961ba2 resource.service.name=Learning Management Service trace_sampled=True] - items_list_failed_as_not_found
backend-1  | 2026-03-31 20:15:20,910 INFO [lms_backend.main] [main.py:74] [trace_id=e5068c0642f0bdd994ff3532bcf41977 span_id=376fb4e98f961ba2 resource.service.name=Learning Management Service trace_sampled=True] - request_completed
backend-1  | INFO:     172.19.0.10:52106 - "GET /items/ HTTP/1.1" 404
backend-1  | INFO:     172.19.0.10:52106 - "GET /items/ HTTP/1.1" 404 Not Found

## Task 3B — Traces

<!-- Screenshots: healthy trace span hierarchy, error trace -->

## Task 3C — Observability MCP tools

<!-- Paste agent responses to "any errors in the last hour?" under normal and failure conditions -->

## Task 4A — Multi-step investigation

<!-- Paste the agent's response to "What went wrong?" showing chained log + trace investigation -->

## Task 4B — Proactive health check

<!-- Screenshot or transcript of the proactive health report that appears in the Flutter chat -->

## Task 4C — Bug fix and recovery

<!-- 1. Root cause identified
     2. Code fix (diff or description)
     3. Post-fix response to "What went wrong?" showing the real underlying failure
     4. Healthy follow-up report or transcript after recovery -->
