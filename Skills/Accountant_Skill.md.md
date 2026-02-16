# Accountant Skill

## Purpose
Manage all financial records, track budgets, and generate reports automatically.

## Inputs
- Expense and revenue entries
- Project budgets
- Task cost metadata

## Outputs
- Financial summaries
- Budget status reports
- Alerts for overspending

## Decision Rules
- If expense > budget → flag for review
- If revenue delayed → notify human
- If project costs exceed limit → escalate

## Escalation Conditions
- Missing transaction data
- Discrepancies in totals
- Critical budget breaches

## Example Workflow
1. Monitor `/Accounting` folder for new entries
2. Generate weekly/monthly financial summary
3. Send alert if budget limits are exceeded
4. Update `/Logs` with all financial actions
