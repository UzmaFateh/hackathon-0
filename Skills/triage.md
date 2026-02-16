# Skill: Triage

## Purpose
Process incoming items from Inbox and route them to the appropriate folder based on content, urgency, and type.

## Inputs
- File path: Path to the file in /Inbox
- File content: Markdown content of the item

## Outputs
- Destination folder: Where the item should be moved
- Priority level: High/Medium/Low
- Assigned tags: Relevant categorization tags
- Routing reason: Brief explanation of routing decision

## Process

1. **Analyze Content**
   - Read file content
   - Identify type (task, project, question, information)
   - Extract key metadata (dates, priorities, dependencies)

2. **Determine Urgency**
   - Check for deadline keywords (urgent, ASAP, today, tomorrow)
   - Identify time-sensitive content
   - Assess impact and importance

3. **Route to Destination**
   - **Needs_Action**: Urgent tasks, questions requiring immediate response
   - **Plans**: Strategic proposals, project ideas, long-term planning
   - **Accounting**: Financial documents, invoices, expenses
   - **Active_Projects**: Updates to existing projects
   - **Logs**: System notifications, automated reports

4. **Add Metadata**
   - Add frontmatter with routing info
   - Tag appropriately (#urgent, #financial, #project, etc.)
   - Link to related items if applicable

5. **Move File**
   - Move from /Inbox to destination
   - Log the routing decision
   - Create follow-up tasks if needed

## Success Criteria
- Item correctly categorized (>95% accuracy)
- Urgent items flagged appropriately
- All items processed within 5 minutes of arrival
- Clear routing reasoning provided

## Error Handling
- **Ambiguous content**: Move to /Needs_Action with #needs-review tag
- **Missing information**: Create clarification task in /Needs_Action
- **Multiple categories**: Route to highest priority destination, add note
- **Corrupted file**: Log error, notify human

## Examples

### Example 1: Urgent Task
**Input:**
```markdown
Need to submit quarterly report by Friday. Requires financial data from last 3 months.
```

**Output:**
- Destination: /Needs_Action
- Priority: High
- Tags: #urgent #report #financial
- Reason: Time-sensitive task with clear deadline

### Example 2: Project Proposal
**Input:**
```markdown
# New Marketing Campaign Idea
I'm thinking we should launch a social media campaign...
```

**Output:**
- Destination: /Plans
- Priority: Medium
- Tags: #project #marketing #proposal
- Reason: Strategic proposal requiring planning and approval

### Example 3: Invoice
**Input:**
```markdown
Invoice #12345
Amount: $500
Due: 2024-03-15
```

**Output:**
- Destination: /Accounting
- Priority: Medium
- Tags: #invoice #financial
- Reason: Financial document for accounting records
