# Task Manager Skill

## Purpose
Automatically draft or start work on tasks received in `/Needs_Action` folder.

## Inputs
- Task file content from `/Needs_Action`
- Task metadata (priority, due date, type)

## Outputs
- Drafted content (AI generated)
- Optional suggestions or next steps
- Log entry in `/Logs`

## Decision Rules
- If task type = "content" → generate draft
- If task type = "analysis" → generate summary/report
- If unclear → flag for manual review

## Escalation Conditions
- AI cannot generate content (empty output)
- Task missing priority/due date
- Conflicting instructions in task

## Example Workflow
1. Task appears in `/Needs_Action/test-task.md`
2. AI reads task content
3. AI generates draft or first version
4. Draft saved in `/Pending_Approval/test-task-draft.md`
5. Human reviews draft
6. Human approves → move to `/Approved`
7. Human rejects → move to `/Rejected` with notes
