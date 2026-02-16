# Researcher Skill

## Purpose
Automatically gather, summarize, and analyze information from multiple sources.

## Inputs
- Task description from `/Needs_Action`
- Keywords, URLs, or reference material

## Outputs
- Summarized findings
- Reports or tables
- Recommended next steps

## Decision Rules
- If task type = research → gather relevant info
- If unclear → flag for human review
- Prioritize by deadline and relevance

## Escalation Conditions
- Unable to find sufficient information
- Conflicting data
- Time-sensitive deadlines

## Example Workflow
1. Task appears in `/Needs_Action/research-task.md`
2. AI gathers info from web, files, or databases
3. Creates summary report in `/Pending_Approval/research-task-summary.md`
4. Human reviews and approves → move to `/Approved`
5. Human rejects → move to `/Rejected` with notes
