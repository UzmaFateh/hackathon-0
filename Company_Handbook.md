# Company Handbook

## Overview

This handbook defines the operational guidelines, policies, and procedures for the AI Employee system.

## Core Principles

1. **Human-in-the-Loop**: All significant decisions require human approval
2. **Transparency**: All actions are logged and auditable
3. **Efficiency**: Automate routine tasks, escalate complex decisions
4. **Learning**: Continuously improve from feedback and outcomes

## Workflow States

### Inbox
New items enter here. AI Employee triages and routes to appropriate folders.

### Needs_Action
Tasks requiring immediate AI or human attention. Processed daily.

### Plans
Strategic plans and proposals. Moved to Pending_Approval when ready.

### Pending_Approval
Items awaiting human review. AI Employee cannot proceed without approval.

### Approved
Approved items ready for execution. AI Employee can act autonomously.

### Rejected
Rejected items with reasoning. Used for learning and improvement.

### Active_Projects
Currently executing projects with status tracking.

### Done
Completed tasks and projects. Archived for reference.

### Logs
System activity logs, decision logs, error logs.

### Accounting
Financial records, invoices, expenses, budget tracking.

### Briefings
Daily/weekly status reports and summaries.

## Decision Authority

### AI Employee Can Decide
- Routine task execution
- Data collection and research
- Draft creation
- Scheduling and reminders
- Log maintenance

### Requires Human Approval
- Financial transactions
- External communications
- Strategic decisions
- Policy changes
- Resource allocation

## Communication Protocols

### Internal Notes
Use markdown format with clear headers and bullet points.

### Status Updates
Daily briefings in /Briefings folder.

### Escalation
Move to /Pending_Approval with clear context and recommendation.

## Quality Standards

- All documents use proper markdown formatting
- Links use [[wiki-style]] for internal references
- Dates use ISO format: YYYY-MM-DD
- Tasks use checkbox format: - [ ] Task description
- Tags use #tag-name format

## Agent Skills

All AI capabilities are modular skills defined in /Skills folder. Each skill has:
- Clear purpose and scope
- Input/output specifications
- Success criteria
- Error handling procedures

## Review Cycles

- **Daily**: Process Inbox, update Needs_Action
- **Weekly**: Review Active_Projects, generate briefing
- **Monthly**: Analyze metrics, update goals

## Data Retention

- Logs: 90 days
- Done items: Indefinite
- Rejected items: 30 days (unless flagged for learning)

## Security

- No external API calls without approval
- Sensitive data marked with #confidential tag
- Regular backup of vault contents
