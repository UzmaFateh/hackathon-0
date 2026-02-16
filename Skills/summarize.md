# Skill: Summarize

## Purpose
Create concise, actionable summaries of documents, meetings, reports, and other content.

## Inputs
- Source content: Text to summarize
- Summary type: Brief/Standard/Detailed
- Target audience: Technical/Executive/General
- Key focus areas: Specific aspects to emphasize

## Outputs
- Summary text: Condensed version of content
- Key points: Bullet list of main takeaways
- Action items: Extracted tasks and next steps
- Metadata: Word count, reading time, confidence level

## Process

1. **Analyze Content**
   - Identify document type and structure
   - Extract main themes and topics
   - Note key facts, figures, and dates

2. **Identify Key Information**
   - Main arguments or conclusions
   - Critical decisions or recommendations
   - Important data points
   - Action items and deadlines

3. **Generate Summary**
   - **Brief** (2-3 sentences): Core message only
   - **Standard** (1 paragraph): Main points with context
   - **Detailed** (multiple paragraphs): Comprehensive overview

4. **Extract Action Items**
   - Convert implicit tasks to explicit action items
   - Assign priorities
   - Note dependencies and deadlines

5. **Format Output**
   - Use clear headers and structure
   - Include bullet points for scannability
   - Add relevant links and references

## Success Criteria
- Summary captures essential information
- No critical details omitted
- Action items are clear and actionable
- Appropriate length for summary type
- Maintains original meaning and context

## Error Handling
- **Unclear content**: Note ambiguities, request clarification
- **Missing context**: Flag gaps in information
- **Conflicting information**: Highlight contradictions
- **Too complex**: Break into sections, summarize each

## Examples

### Example 1: Meeting Notes
**Input:**
```markdown
Team discussed Q1 goals. Sarah proposed new feature for user dashboard.
Mike raised concerns about timeline. Agreed to prototype by end of month.
Budget approved: $15k. Next meeting: Feb 20.
```

**Output:**
**Summary:** Team aligned on Q1 goals with focus on new dashboard feature. Budget of $15k approved despite timeline concerns.

**Key Points:**
- New user dashboard feature proposed by Sarah
- Timeline concerns raised but moving forward
- Budget: $15k approved
- Prototype deadline: End of month

**Action Items:**
- [ ] Create dashboard prototype (Due: End of month)
- [ ] Schedule follow-up meeting (Feb 20)

### Example 2: Long Report
**Input:** [10-page market analysis report]

**Output (Standard):**
**Summary:** Market analysis reveals 23% growth opportunity in target segment. Primary competitors are consolidating, creating entry window. Recommended investment: $50k for 6-month pilot. Key risks include regulatory changes and supply chain constraints.

**Key Points:**
- 23% growth potential identified
- Competitor consolidation creates opportunity
- $50k investment recommended
- 6-month pilot timeline
- Regulatory and supply chain risks noted

**Action Items:**
- [ ] Review investment proposal
- [ ] Assess risk mitigation strategies
- [ ] Prepare pilot program plan
