# Skill: Report

## Purpose
Generate status reports, briefings, and summaries of activities, progress, and metrics.

## Inputs
- Report type: Daily/Weekly/Monthly/Custom
- Time period: Date range to cover
- Scope: What to include (projects, tasks, metrics)
- Audience: Who will read the report
- Format: Brief/Standard/Detailed

## Outputs
- Report document: Formatted status report
- Metrics summary: Key performance indicators
- Highlights: Notable achievements or issues
- Action items: Follow-up tasks identified

## Process

1. **Gather Data**
   - Scan relevant folders for activity
   - Extract completed tasks from /Done
   - Review active projects status
   - Collect metrics and KPIs
   - Note pending approvals

2. **Analyze Activity**
   - Calculate completion rates
   - Identify trends and patterns
   - Flag blockers or delays
   - Highlight achievements

3. **Structure Report**
   - Executive summary
   - Key metrics
   - Progress by project/area
   - Issues and blockers
   - Upcoming priorities

4. **Format Output**
   - Use consistent template
   - Include visualizations (tables, lists)
   - Add relevant links
   - Save to /Briefings folder

5. **Archive**
   - Name with date: `report-YYYY-MM-DD.md`
   - Tag appropriately
   - Link to previous reports

## Success Criteria
- All relevant activity captured
- Metrics accurate and up-to-date
- Clear and scannable format
- Actionable insights provided
- Delivered on schedule

## Error Handling
- **Missing data**: Note gaps, estimate where reasonable
- **Incomplete projects**: Flag status as uncertain
- **Conflicting information**: Investigate and clarify
- **No activity**: Report as such, don't fabricate

## Examples

### Example 1: Daily Briefing
**Input:**
- Type: Daily briefing
- Date: 2024-02-12
- Scope: All activities

**Output:**
```markdown
# Daily Briefing - February 12, 2024

## Summary
Processed 8 inbox items, completed 5 tasks, 2 items pending approval.

## Completed Today
- ✅ Research report on project management tools
- ✅ Draft email to client re: Q2 meeting
- ✅ Updated budget spreadsheet
- ✅ Reviewed marketing proposal
- ✅ Triaged 8 inbox items

## In Progress
- 📝 Customer portal enhancement plan (80% complete)
- 📝 Q1 financial analysis (waiting for data)

## Pending Approval
- ⏳ Marketing campaign proposal
- ⏳ Budget increase request

## Blockers
- None

## Metrics
- Tasks completed: 5
- Approval rate: 100% (2/2 items approved yesterday)
- Response time: <2h average

## Tomorrow's Priorities
1. Complete customer portal plan
2. Process pending approvals
3. Begin Q2 planning document
```

### Example 2: Weekly Report
**Input:**
- Type: Weekly report
- Period: Feb 5-11, 2024
- Scope: All projects and tasks

**Output:**
```markdown
# Weekly Report - Week of February 5, 2024

## Executive Summary
Strong week with 23 tasks completed and 3 projects advanced. Marketing campaign approved and launched. Customer portal planning on track.

## Key Metrics
| Metric | This Week | Last Week | Change |
|--------|-----------|-----------|--------|
| Tasks Completed | 23 | 18 | +28% |
| Approval Rate | 92% | 85% | +7% |
| Active Projects | 4 | 5 | -1 |
| Avg Response Time | 1.5h | 2.3h | -35% |

## Project Progress

### Customer Portal Enhancement
**Status:** On Track (60% complete)
- ✅ Requirements gathered
- ✅ Design mockups created
- ✅ Budget approved
- 🔄 Development starting next week

### Marketing Campaign Q2
**Status:** Completed
- ✅ Plan approved
- ✅ Creative assets finalized
- ✅ Campaign launched Feb 10
- 📊 Early metrics positive

### Financial System Upgrade
**Status:** On Hold
- ⏸️ Waiting for vendor response
- Next action: Follow up on Feb 15

## Highlights
- 🎉 Marketing campaign launched successfully
- 🎉 Reduced response time by 35%
- 🎉 Zero critical issues this week

## Issues & Blockers
- Financial system vendor delayed (low impact)
- Budget approval process slow (medium impact)

## Next Week Priorities
1. Begin customer portal development
2. Review marketing campaign metrics
3. Complete Q1 financial analysis
4. Process 3 pending proposals

## Resource Utilization
- AI processing time: 12.5 hours
- Human review time: 3.2 hours
- Efficiency ratio: 3.9:1
```

### Example 3: Monthly Report
**Input:**
- Type: Monthly report
- Period: January 2024
- Scope: Full operations

**Output:**
```markdown
# Monthly Report - January 2024

## Executive Summary
Successful first month of AI Employee operations. 87 tasks completed with 89% approval rate. System stability excellent with 99.2% uptime.

## Monthly Metrics
| Category | Target | Actual | Status |
|----------|--------|--------|--------|
| Tasks Completed | 80 | 87 | ✅ +9% |
| Approval Rate | 85% | 89% | ✅ +4% |
| Response Time | <2h | 1.8h | ✅ |
| Error Rate | <5% | 3.2% | ✅ |
| Uptime | >95% | 99.2% | ✅ |

## Projects Completed (3)
1. **Marketing Website Redesign** - Launched Jan 28
2. **Q4 Financial Report** - Submitted Jan 15
3. **Customer Survey Analysis** - Completed Jan 22

## Projects In Progress (4)
1. **Customer Portal Enhancement** - 60% complete
2. **Sales Process Automation** - 40% complete
3. **Data Migration Project** - 25% complete
4. **Q1 Planning** - 80% complete

## Operational Insights

### What Worked Well
- Inbox triage automation saved ~8 hours/week
- Draft generation quality exceeded expectations
- Review process caught 15 potential issues

### Challenges
- Budget approval workflow needs streamlining
- Some complex research tasks required multiple iterations
- Integration with external tools limited

### Improvements Made
- Enhanced triage skill with better categorization
- Added review checklist templates
- Improved error handling in watchers

## Financial Impact
- Time saved: ~32 hours
- Cost savings: $2,400 (at $75/hour rate)
- ROI: 240% (vs. setup cost)

## Skills Performance
| Skill | Uses | Success Rate | Avg Time |
|-------|------|--------------|----------|
| Triage | 156 | 96% | 2 min |
| Draft | 34 | 91% | 15 min |
| Research | 18 | 94% | 45 min |
| Review | 28 | 89% | 12 min |
| Summarize | 42 | 98% | 5 min |

## February Goals
1. Increase task completion to 100/month
2. Improve approval rate to 92%
3. Add 2 new custom skills
4. Integrate with calendar system
5. Reduce response time to <1.5h

## Recommendations
1. Invest in calendar integration MCP server
2. Create custom skill for financial reporting
3. Expand automation to email processing
4. Schedule monthly system optimization review
```
