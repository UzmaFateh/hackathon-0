# Skill: Review

## Purpose
Perform quality checks on documents, code, plans, and other work products before submission or approval.

## Inputs
- Item to review: Document, code, plan, etc.
- Review type: Quality/Compliance/Technical/Editorial
- Criteria: Specific standards or requirements
- Severity threshold: What issues to flag

## Outputs
- Review report: Findings and assessment
- Issue list: Problems identified with severity
- Recommendations: Suggested improvements
- Approval status: Pass/Fail/Conditional
- Confidence score: Reliability of review

## Process

1. **Understand Context**
   - Review item type and purpose
   - Identify applicable standards
   - Clarify success criteria
   - Note any special requirements

2. **Perform Checks**
   - **Completeness**: All required elements present
   - **Accuracy**: Facts and data verified
   - **Consistency**: No contradictions or conflicts
   - **Clarity**: Clear and understandable
   - **Format**: Proper structure and style
   - **Compliance**: Meets standards and policies

3. **Identify Issues**
   - Categorize by severity (Critical/High/Medium/Low)
   - Document specific problems
   - Note location of issues
   - Suggest fixes where possible

4. **Assess Quality**
   - Overall quality rating
   - Readiness for next stage
   - Risk assessment
   - Improvement opportunities

5. **Generate Report**
   - Summarize findings
   - List issues by priority
   - Provide recommendations
   - Give approval decision

## Success Criteria
- All critical issues identified
- Clear, actionable feedback provided
- Consistent with review standards
- Appropriate severity assignments
- Helpful improvement suggestions

## Error Handling
- **Ambiguous criteria**: Request clarification, use best judgment
- **Complex item**: Break into sections, review incrementally
- **Missing information**: Flag gaps, request additional context
- **Conflicting standards**: Document conflict, escalate decision

## Examples

### Example 1: Document Review
**Input:**
- Item: Project proposal
- Type: Quality review
- Criteria: Completeness, clarity, feasibility

**Output:**
**Review Report: Project Proposal - Customer Portal Enhancement**

**Overall Assessment:** CONDITIONAL PASS
Quality Score: 7/10

**Critical Issues (Must Fix):**
1. **Missing budget breakdown** (Line 45)
   - Issue: Total budget shown but no itemization
   - Fix: Add detailed cost breakdown by category

**High Priority Issues:**
2. **Vague success metrics** (Section 3)
   - Issue: "Improve user satisfaction" lacks specific target
   - Fix: Define measurable KPIs (e.g., "Increase NPS from 6 to 8")

3. **Timeline lacks milestones** (Section 5)
   - Issue: Only shows month-level phases
   - Fix: Add specific milestone dates and deliverables

**Medium Priority Issues:**
4. **Risk assessment incomplete** (Section 7)
   - Issue: Only 3 risks identified, no mitigation plans
   - Fix: Expand risk analysis, add mitigation strategies

**Low Priority Issues:**
5. **Formatting inconsistency** (Throughout)
   - Issue: Mixed heading styles
   - Fix: Standardize markdown formatting

**Recommendations:**
- Add competitive analysis section
- Include stakeholder sign-off section
- Consider adding visual timeline diagram

**Approval Status:** Conditional - Fix critical and high priority issues before resubmission

**Next Steps:**
1. Address critical issue #1
2. Revise high priority items #2-3
3. Resubmit for final review

### Example 2: Code Review
**Input:**
- Item: Python script for data processing
- Type: Technical review
- Criteria: Best practices, security, performance

**Output:**
**Code Review Report: data_processor.py**

**Overall Assessment:** PASS WITH RECOMMENDATIONS
Quality Score: 8/10

**Critical Issues:** None

**High Priority Issues:**
1. **SQL injection vulnerability** (Line 67)
   ```python
   # Current (vulnerable):
   query = f"SELECT * FROM users WHERE id = {user_id}"

   # Recommended:
   query = "SELECT * FROM users WHERE id = ?"
   cursor.execute(query, (user_id,))
   ```

**Medium Priority Issues:**
2. **Missing error handling** (Lines 45-52)
   - Add try-except blocks for file operations
   - Handle potential connection failures

3. **Hard-coded configuration** (Line 12)
   - Move database credentials to environment variables
   - Use config file for settings

**Low Priority Issues:**
4. **Inconsistent naming** (Throughout)
   - Mix of camelCase and snake_case
   - Standardize to snake_case per PEP 8

**Positive Observations:**
- Good function documentation
- Efficient algorithm choice
- Clean code structure

**Recommendations:**
- Add unit tests for core functions
- Consider adding logging for debugging
- Document expected input/output formats

**Approval Status:** Approved pending fix of issue #1

### Example 3: Plan Review
**Input:**
- Item: Marketing campaign plan
- Type: Compliance review
- Criteria: Brand guidelines, budget limits, legal requirements

**Output:**
**Compliance Review: Q2 Marketing Campaign**

**Overall Assessment:** FAIL - Requires Revision

**Critical Issues:**
1. **Budget exceeds limit** (Section 4)
   - Proposed: $75k | Approved limit: $50k
   - Must reduce by $25k or request budget increase

2. **Brand guideline violations** (Section 2)
   - Logo usage doesn't match brand standards
   - Color palette includes unapproved colors

**High Priority Issues:**
3. **Missing legal review** (Section 6)
   - Claims require legal approval before publication
   - No evidence of legal team sign-off

4. **Timeline conflicts** (Section 5)
   - Launch date conflicts with product release
   - Coordinate with product team

**Approval Status:** REJECTED - Address all critical issues and resubmit

**Required Actions:**
1. Revise budget or request approval for increase
2. Update creative assets to match brand guidelines
3. Submit claims to legal team for review
4. Coordinate timeline with product team
5. Resubmit for review after changes
