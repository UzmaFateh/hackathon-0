# AI Employee Vault - Architecture & Workflow

## Overview

This Obsidian vault serves as the operational workspace for a Personal AI Employee (Digital FTE) system. It combines Claude Code, Python watchers, and MCP servers to create an autonomous yet human-supervised AI assistant.

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Human Operator                        │
└────────────────────┬────────────────────────────────────┘
                     │
                     ↓
┌─────────────────────────────────────────────────────────┐
│                  Obsidian Vault                          │
│  (Central Knowledge Base & Task Management)              │
└────────┬────────────────────────────────────────────────┘
         │
         ↓
┌─────────────────────────────────────────────────────────┐
│              Python File Watchers                        │
│  (Monitor vault changes, trigger workflows)              │
└────────┬────────────────────────────────────────────────┘
         │
         ↓
┌─────────────────────────────────────────────────────────┐
│                 MCP Servers                              │
│  (Tool integrations, external services)                  │
└────────┬────────────────────────────────────────────────┘
         │
         ↓
┌─────────────────────────────────────────────────────────┐
│                 Claude Code                              │
│  (AI reasoning, task execution, skill orchestration)     │
└─────────────────────────────────────────────────────────┘
```

## Folder Structure

### `/Inbox`
Entry point for all new items. Python watchers monitor this folder and trigger AI triage.

**Workflow:**
1. New file appears in Inbox
2. Watcher detects change
3. AI analyzes content and routes to appropriate folder
4. Original file moved or archived

### `/Needs_Action`
Tasks requiring immediate attention from AI or human.

**Triggers:**
- High priority items from Inbox
- Scheduled tasks due today
- Escalated issues from Active_Projects

### `/Plans`
Strategic plans, proposals, and project designs.

**Format:**
- Each plan is a separate markdown file
- Include objectives, approach, resources, timeline
- Move to Pending_Approval when ready

### `/Pending_Approval`
Items awaiting human review and approval.

**Process:**
1. AI moves completed work here
2. Human reviews and decides
3. Approved → /Approved folder
4. Rejected → /Rejected folder with feedback

### `/Approved`
Approved plans and tasks ready for execution.

**Next Steps:**
- AI can proceed autonomously
- Move to Active_Projects when execution begins
- Track progress and status

### `/Rejected`
Rejected items with reasoning for learning.

**Purpose:**
- Train AI on what not to do
- Identify patterns in rejections
- Improve future proposals

### `/Active_Projects`
Currently executing projects with status tracking.

**Structure:**
```
Active_Projects/
├── project-name/
│   ├── README.md (project overview)
│   ├── tasks.md (task breakdown)
│   ├── status.md (current status)
│   └── notes.md (working notes)
```

### `/Done`
Completed tasks and projects for reference.

**Archival:**
- Moved here when project completes
- Includes final status and outcomes
- Used for metrics and learning

### `/Logs`
System activity logs and decision trails.

**Types:**
- `activity-YYYY-MM-DD.md` - Daily activity log
- `decisions-YYYY-MM-DD.md` - Decision log with reasoning
- `errors-YYYY-MM-DD.md` - Error log for debugging

### `/Accounting`
Financial tracking and records.

**Contents:**
- Invoices
- Expenses
- Budget tracking
- Financial reports

### `/Briefings`
Status reports and summaries.

**Schedule:**
- Daily: End-of-day summary
- Weekly: Progress report
- Monthly: Metrics and analysis

### `/Skills`
Agent skill definitions and configurations.

**Skill Structure:**
```markdown
# Skill: [Name]

## Purpose
[What this skill does]

## Inputs
- Input 1: Description
- Input 2: Description

## Outputs
- Output 1: Description

## Process
1. Step 1
2. Step 2
3. Step 3

## Success Criteria
- Criteria 1
- Criteria 2

## Error Handling
- Error type 1: Response
- Error type 2: Response

## Examples
[Usage examples]
```

## Core Workflows

### 1. Task Intake
```
New Item → Inbox → AI Triage → Appropriate Folder
```

### 2. Approval Flow
```
Draft → Pending_Approval → Human Review → Approved/Rejected
```

### 3. Project Execution
```
Approved → Active_Projects → Progress Tracking → Done
```

### 4. Daily Operations
```
Morning: Process Inbox, Review Needs_Action
Midday: Update Active_Projects
Evening: Generate Briefing, Log Activities
```

## Python Watcher Implementation

```python
# Example watcher structure
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class VaultHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Trigger AI processing
        pass

    def on_modified(self, event):
        # Handle updates
        pass
```

**Key Watchers:**
- Inbox monitor (high priority)
- Needs_Action monitor (daily check)
- Pending_Approval monitor (notify human)

## MCP Server Integration

**Recommended MCP Servers:**
- File system operations
- Calendar/scheduling
- Email integration
- Database access
- API connectors

**Configuration:**
Each MCP server defined in Claude Code settings with appropriate permissions.

## Agent Skills System

All AI functionality is modular and defined as skills in `/Skills` folder.

**Core Skills:**
- `triage.md` - Inbox processing and routing
- `summarize.md` - Document summarization
- `research.md` - Information gathering
- `draft.md` - Document drafting
- `review.md` - Quality checking
- `report.md` - Status reporting

**Custom Skills:**
Add domain-specific skills as needed.

## Getting Started

1. **Initial Setup**
   - Review and customize Company_Handbook.md
   - Define your Business_Goals.md
   - Configure Python watchers
   - Set up MCP servers

2. **First Tasks**
   - Create a test item in Inbox
   - Verify watcher triggers
   - Test approval workflow
   - Review logs

3. **Daily Usage**
   - Check Dashboard.md each morning
   - Process Pending_Approval items
   - Review daily briefing
   - Update active projects

4. **Continuous Improvement**
   - Analyze rejection patterns
   - Refine agent skills
   - Optimize workflows
   - Update metrics

## Best Practices

- **Atomic Files**: One task/project per file
- **Clear Naming**: Use descriptive, consistent file names
- **Rich Metadata**: Use frontmatter for structured data
- **Linked Thinking**: Connect related notes with [[links]]
- **Regular Reviews**: Weekly review of all folders
- **Backup**: Regular vault backups

## Security Considerations

- Keep sensitive data in separate encrypted folder
- Use #confidential tag for sensitive items
- Review all external API calls
- Audit logs regularly
- Limit MCP server permissions

## Troubleshooting

**Watcher not triggering:**
- Check Python process is running
- Verify file permissions
- Review watcher logs

**AI not routing correctly:**
- Review triage skill definition
- Check for ambiguous content
- Update routing rules

**Approval bottleneck:**
- Set up notification system
- Define approval SLAs
- Delegate approval authority

## Metrics & Analytics

Track these metrics in Dashboard.md:
- Tasks processed per day
- Approval rate
- Average completion time
- Error rate
- Time saved

## Future Enhancements

- [ ] Web interface for mobile access
- [ ] Voice input integration
- [ ] Advanced analytics dashboard
- [ ] Multi-agent collaboration
- [ ] Learning from outcomes

## Support

For issues or questions:
1. Check logs in /Logs folder
2. Review Company_Handbook.md
3. Consult skill definitions in /Skills
4. Update this README with solutions

---

**Version:** 1.0.0
**Last Updated:** {{date}}
**Maintained By:** [Your Name]
