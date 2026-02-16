# CEO Skill

## Purpose
Oversee high-level strategy, approvals, and priority decisions across all projects.

## Inputs
- Summaries and recommendations from other skills
- Business goals and KPIs
- Pending approvals and escalations

## Outputs
- Decisions on project priorities
- Approval/rejection of plans and tasks
- Strategic guidance for AI Employees

## Decision Rules
- Approve tasks aligned with company goals
- Escalate conflicting priorities or resource constraints
- Delegate operational tasks to relevant skills

## Escalation Conditions
- Conflicting recommendations from multiple skills
- Tasks exceeding budget or resources
- Critical deadlines at risk

## Example Workflow
1. AI collects all pending plans in `/Pending_Approval`
2. CEO Skill reviews summaries and recommendations
3. Makes decisions → move items to `/Approved` or `/Rejected`
4. Updates Dashboard.md with priorities
5. Logs all decisions in `/Logs`
