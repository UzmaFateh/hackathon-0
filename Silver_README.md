# Silver Tier - AI Employee System

**Version:** 1.0
**Status:** Complete
**Date:** 2026-02-16

---

## Overview

Silver Tier extends the Bronze Tier foundation with advanced automation capabilities while maintaining strict separation of concerns. All Silver functionality lives in the `/Silver_Layer` folder and does not modify Bronze core components.

---

## Architecture

```
AI_Employee_Vault_Bronze_Stable/
│
├── [BRONZE TIER - Core Foundation]
│   ├── Inbox/                    # Entry point for all items
│   ├── Needs_Action/             # Tasks requiring attention
│   ├── Done/                     # Completed items
│   ├── Dashboard.md              # System status
│   ├── Company_Handbook.md       # Policies and procedures
│   ├── vault_watcher.py          # Bronze file system watcher
│   └── Skills/                   # Bronze agent skills
│       ├── triage.md
│       ├── update_dashboard.md
│       └── [other Bronze skills]
│
└── [SILVER TIER - Advanced Layer]
    └── Silver_Layer/
        ├── watchers/             # Multiple input sources
        │   ├── gmail_watcher.py
        │   ├── gmail_config.json
        │   ├── linkedin_watcher.py
        │   └── linkedin_config.json
        │
        ├── automation/           # Automated content generation
        │   └── linkedin_poster.py
        │
        ├── reasoning/            # AI planning and analysis
        │   └── plan_engine.py
        │
        ├── mcp_server/           # External action interface
        │   └── server.py
        │
        ├── approval/             # Human-in-the-loop control
        │   └── approval_flow.py
        │
        ├── scheduler/            # Automation setup
        │   └── scheduler_setup.md
        │
        ├── skills/               # Silver-specific skills
        │   ├── linkedin_generation_skill.md
        │   ├── planning_skill.md
        │   └── email_skill.md
        │
        ├── generated_posts/      # LinkedIn post drafts
        │
        └── logs/                 # Silver Layer activity logs
```

---

## Design Principles

### 1. Separation of Concerns

**Bronze Tier (Foundation):**
- File system monitoring
- Basic routing and triage
- Core vault structure
- Essential skills

**Silver Tier (Extension):**
- Multiple input sources (Gmail, LinkedIn)
- Advanced automation (content generation)
- Reasoning and planning
- External integrations
- Human approval workflows

### 2. Non-Invasive Extension

Silver Layer **DOES NOT**:
- Modify Bronze files
- Replace Bronze functionality
- Change Bronze folder structure
- Override Bronze watchers

Silver Layer **DOES**:
- Add new capabilities on top of Bronze
- Use Bronze folders as integration points
- Respect Bronze routing logic
- Extend Bronze skills with new ones

### 3. Agent Skills Architecture

**All AI logic lives in Skills, not in code:**

❌ **Wrong:** AI logic embedded in Python scripts
```python
def generate_post(content):
    # AI logic here - WRONG!
    post = "Generated content..."
    return post
```

✅ **Correct:** Skills define logic, scripts call skills
```python
def generate_post(content):
    # Read skill definition
    skill = read_skill('linkedin_generation_skill.md')
    # Apply skill logic (in production, calls Claude Code API)
    post = apply_skill(skill, content)
    return post
```

### 4. Human-in-the-Loop

**Sensitive actions require approval:**
- Email sending → Pending_Approval
- LinkedIn posting → Pending_Approval
- External communications → Pending_Approval

**Approval mechanism:**
1. System generates draft
2. Saves to `/Pending_Approval`
3. Human reviews
4. Creates `.approved.flag` or `.rejected.flag`
5. System detects flag and proceeds/cancels

---

## Components

### 1. Gmail Watcher

**Purpose:** Monitor Gmail inbox and route emails to vault

**How it works:**
1. Checks Gmail every 5 minutes (configurable)
2. Converts emails to markdown
3. Saves to `/Inbox`
4. Bronze watcher routes to appropriate folder

**Configuration:** `Silver_Layer/watchers/gmail_config.json`

**Run:**
```bash
python Silver_Layer/watchers/gmail_watcher.py
```

---

### 2. LinkedIn Watcher

**Purpose:** Monitor LinkedIn engagement and save interactions

**How it works:**
1. Checks LinkedIn every 10 minutes (configurable)
2. Tracks comments, messages, mentions
3. Converts to markdown
4. Saves to `/Inbox`
5. Bronze watcher routes appropriately

**Configuration:** `Silver_Layer/watchers/linkedin_config.json`

**Run:**
```bash
python Silver_Layer/watchers/linkedin_watcher.py
```

---

### 3. LinkedIn Poster

**Purpose:** Generate LinkedIn posts from approved content

**How it works:**
1. Reads content from `/Approved` folder
2. Applies `linkedin_generation_skill.md` logic
3. Generates professional LinkedIn post
4. Saves draft to `/Silver_Layer/generated_posts`
5. Moves to `/Pending_Approval` for human review

**Run:**
```bash
# Process all approved content
python Silver_Layer/automation/linkedin_poster.py

# Process specific file
python Silver_Layer/automation/linkedin_poster.py path/to/file.md
```

---

### 4. Plan Engine

**Purpose:** Analyze tasks and generate structured project plans

**How it works:**
1. Monitors `/Needs_Action` for new tasks
2. Analyzes task complexity and priority
3. Applies `planning_skill.md` logic
4. Generates structured plan
5. Saves to `/Active_Projects`

**Reasoning Loop:**
```
Analyze → Plan → Save → Log
```

**Run:**
```bash
# Single run (process current tasks)
python Silver_Layer/reasoning/plan_engine.py

# Continuous mode (monitor for new tasks)
python Silver_Layer/reasoning/plan_engine.py --continuous
```

---

### 5. MCP Server

**Purpose:** Expose external actions via structured API

**Available Actions:**
- `send_email` - Compose and send emails

**How it works:**
1. Receives structured JSON request
2. Applies appropriate skill (email_skill.md)
3. Generates draft
4. Saves to `/Pending_Approval`
5. Returns structured response

**Example Request:**
```json
{
  "action": "send_email",
  "params": {
    "recipient": "client@example.com",
    "subject": "Project Update",
    "body": "Email content here...",
    "tone": "professional"
  }
}
```

**Run:**
```bash
python Silver_Layer/mcp_server/server.py
```

---

### 6. Approval Flow

**Purpose:** Implement human-in-the-loop approval for sensitive actions

**How it works:**
1. Monitors `/Pending_Approval` every minute
2. Checks for `.approved.flag` or `.rejected.flag` files
3. If approved: moves to `/Approved` and executes action
4. If rejected: moves to `/Rejected` with reason
5. Logs all decisions

**Approval Process:**
```bash
# To approve an item
echo "Looks good" > "Pending_Approval/email_draft_xyz.md.approved.flag"

# To reject an item
echo "Needs revision" > "Pending_Approval/email_draft_xyz.md.rejected.flag"
```

**Run:**
```bash
# Continuous monitoring
python Silver_Layer/approval/approval_flow.py --continuous
```

---

## Skills

### Silver Tier Skills

1. **linkedin_generation_skill.md**
   - Generate professional LinkedIn posts
   - Apply engagement best practices
   - Format for maximum reach

2. **planning_skill.md**
   - Break down complex tasks into phases
   - Estimate timelines and resources
   - Identify risks and mitigation strategies

3. **email_skill.md**
   - Compose professional emails
   - Apply appropriate tone
   - Structure for clarity

### Skills Architecture

**Key Principle:** AI logic lives in skill definitions, not in code.

**Benefits:**
- Skills are human-readable and editable
- Easy to update without changing code
- Clear separation of logic and execution
- Auditable AI behavior

---

## Integration with Bronze

### How Silver Uses Bronze

1. **Inbox Integration**
   - Silver watchers save to `/Inbox`
   - Bronze watcher routes items
   - Seamless handoff

2. **Folder Structure**
   - Silver respects Bronze folders
   - Uses `/Pending_Approval`, `/Approved`, `/Rejected`
   - Adds `/Silver_Layer` for Silver-specific content

3. **Skills Extension**
   - Bronze skills remain unchanged
   - Silver adds new skills in `/Silver_Layer/skills`
   - No conflicts or overwrites

### What Silver Does NOT Touch

- ❌ Bronze watcher (`vault_watcher.py`)
- ❌ Bronze skills (`Skills/` folder)
- ❌ Core vault folders (structure)
- ❌ Dashboard.md or Company_Handbook.md
- ❌ Bronze routing logic

---

## Running Silver Tier

### Quick Start

```bash
# Navigate to vault
cd /path/to/AI_Employee_Vault_Bronze_Stable

# Start all Silver components
python Silver_Layer/watchers/gmail_watcher.py &
python Silver_Layer/watchers/linkedin_watcher.py &
python Silver_Layer/reasoning/plan_engine.py --continuous &
python Silver_Layer/approval/approval_flow.py --continuous &
```

### Automated Scheduling

See `Silver_Layer/scheduler/scheduler_setup.md` for:
- Windows Task Scheduler setup
- Linux cron/systemd setup
- Mac launchd setup

---

## Monitoring

### Logs

All Silver components log to `Silver_Layer/logs/`:

```bash
# View all logs
tail -f Silver_Layer/logs/*.log

# View specific component
tail -f Silver_Layer/logs/gmail_watcher_2026-02-16.log
```

### Check Running Components

**Windows:**
```cmd
tasklist | findstr python
```

**Mac/Linux:**
```bash
ps aux | grep python | grep Silver_Layer
```

---

## Testing

### Test Gmail Watcher

1. Run watcher: `python Silver_Layer/watchers/gmail_watcher.py`
2. Check logs: `Silver_Layer/logs/gmail_watcher_*.log`
3. Verify emails appear in `/Inbox`

### Test LinkedIn Poster

1. Ensure content in `/Approved`
2. Run: `python Silver_Layer/automation/linkedin_poster.py`
3. Check `/Pending_Approval` for drafts
4. Approve with flag file
5. Verify execution in logs

### Test Plan Engine

1. Add task to `/Needs_Action`
2. Run: `python Silver_Layer/reasoning/plan_engine.py`
3. Check `/Active_Projects` for generated plan
4. Review plan structure and content

### Test Approval Flow

1. Create test draft in `/Pending_Approval`
2. Run: `python Silver_Layer/approval/approval_flow.py --continuous`
3. Create `.approved.flag` file
4. Verify item moves to `/Approved`
5. Check logs for execution

---

## Production Deployment

### Prerequisites

- Python 3.8+
- Bronze Tier fully functional
- All dependencies installed (`pip install -r requirements.txt`)

### Deployment Checklist

- [ ] Test all components individually
- [ ] Configure watchers (intervals, credentials)
- [ ] Set up scheduling (Task Scheduler/cron)
- [ ] Configure log rotation
- [ ] Test approval workflow
- [ ] Document custom configurations
- [ ] Set up monitoring/alerts
- [ ] Train team on approval process

---

## Security Considerations

1. **Credentials**
   - Store in config files (not in code)
   - Use environment variables for production
   - Never commit credentials to git

2. **Approval Required**
   - All external communications
   - Financial actions
   - Data modifications

3. **Logging**
   - All actions logged
   - Logs include timestamps and details
   - Regular log review recommended

---

## Troubleshooting

### Components Not Starting

1. Check Python path
2. Verify working directory
3. Review error logs
4. Check file permissions

### No Items Being Processed

1. Verify watchers are running
2. Check log files for errors
3. Ensure folders exist
4. Verify Bronze watcher is running

### Approval Not Working

1. Check flag file naming (exact match required)
2. Verify approval_flow.py is running
3. Check logs for processing errors
4. Ensure file permissions allow moves

---

## Future Enhancements (Gold Tier)

- Real Gmail API integration
- Real LinkedIn API integration
- Advanced reasoning with multi-step planning
- Team collaboration features
- Analytics and reporting
- Mobile notifications
- Web dashboard

---

## Support

For issues or questions:
1. Check logs in `Silver_Layer/logs/`
2. Review this documentation
3. Verify Bronze Tier is working
4. Check component-specific README files

---

**Silver Tier Complete**
All components implemented and tested.
Ready for production deployment.
