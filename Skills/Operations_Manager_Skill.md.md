# Operations Manager Skill

## Purpose
Manage the execution of approved tasks and projects, ensuring deadlines, resource allocation, and progress tracking.

## Inputs
- Approved plans and tasks from /Approved
- Active project details
- Resource availability

## Outputs
- Assigned tasks to responsible owners
- Progress updates
- Alerts for delays or resource issues
- Logs in /Logs

## Decision Rules
- Assign tasks to team members based on workload and skills
- Track deadlines and escalate risks
- Ensure dependencies are respected

## Escalation Conditions
- Task delayed beyond deadline
- Resource conflict or shortage
- Critical milestones at risk

## Example Workflow
1. Task appears in /Approved
2. Operations Manager Skill assigns task to responsible team or skill
3. Updates task metadata (due date, owner)
4. Creates progress entry in /Active_Projects
5. Monitors execution and escalates if issues arise
6. Logs all actions in /Logs
