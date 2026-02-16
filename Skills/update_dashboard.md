# Skill: Update Dashboard

## Purpose
Update Dashboard.md with current system status, priorities, and metrics.

## Inputs
- Current vault state (folders, files, counts)
- Active projects from /Active_Projects
- Pending items from /Needs_Action
- Recent completions from /Done

## Outputs
- Updated Dashboard.md with current data
- Timestamp of last update
- Log entry in /Logs

## Process

1. **Collect Current State**
   - Count files in each folder
   - Identify active projects
   - List pending actions
   - Check for urgent items (deadlines within 48h)

2. **Calculate Metrics**
   - Tasks completed this week/month
   - Tasks created vs completed
   - Active project count
   - Approval queue status

3. **Update Dashboard Sections**
   - System Status (counts and alerts)
   - Today's Priorities (urgent items first)
   - Active Projects Overview (table format)
   - Recent Completions (last 7 days)
   - Metrics (weekly and monthly)

4. **Add Timestamp**
   - Update "Last Updated" field
   - Use format: YYYY-MM-DD HH:MM

5. **Log Update**
   - Record dashboard update in activity log
   - Note any significant changes

## Success Criteria
- Dashboard reflects current vault state
- All sections updated accurately
- Timestamp is current
- No data inconsistencies

## Error Handling
- **Missing files**: Note gaps, continue with available data
- **Parse errors**: Log error, skip problematic section
- **Write failure**: Retry once, then escalate

## Example Workflow
1. Skill triggered (manual or scheduled)
2. Scan vault folders for current state
3. Read active project files
4. Calculate metrics from logs
5. Update Dashboard.md
6. Log completion
