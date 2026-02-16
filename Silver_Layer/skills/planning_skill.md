# Skill: Planning

## Purpose
Analyze tasks and generate structured project plans with clear steps, timelines, and resource requirements.

## Inputs
- Task description: Content from Needs_Action file
- Context: Related files, business goals, constraints
- Priority level: High/Medium/Low
- Deadline: Target completion date (if specified)

## Outputs
- Structured plan document (Plan.md)
- Task breakdown (phases and steps)
- Resource requirements (time, people, tools)
- Risk assessment
- Success criteria

## Process

1. **Analyze Task Requirements**
   - Read task description thoroughly
   - Identify objectives and deliverables
   - Extract constraints (time, budget, resources)
   - Determine complexity level

2. **Break Down Into Phases**
   - Divide work into logical phases
   - Each phase should have clear deliverable
   - Phases should be sequential or parallel
   - Estimate duration for each phase

3. **Define Specific Steps**
   - Break each phase into actionable steps
   - Each step should be concrete and measurable
   - Assign estimated time per step
   - Identify dependencies between steps

4. **Identify Resources**
   - People needed (roles, not names)
   - Tools and systems required
   - Budget estimates (if applicable)
   - External dependencies

5. **Assess Risks**
   - What could go wrong?
   - What are the blockers?
   - What assumptions are we making?
   - Mitigation strategies

6. **Define Success Criteria**
   - How do we know it's done?
   - What are the quality standards?
   - What metrics will we track?

## Plan Structure

```markdown
# Project Plan: [Title]

**Created:** [Date]
**Priority:** [High/Medium/Low]
**Deadline:** [Date]
**Estimated Duration:** [X days/weeks]

## Objective

[Clear statement of what we're trying to achieve]

## Phases

### Phase 1: [Name]
**Duration:** [X days]
**Deliverable:** [What gets produced]

Steps:
1. [Step 1] - [Time estimate]
2. [Step 2] - [Time estimate]
3. [Step 3] - [Time estimate]

### Phase 2: [Name]
...

## Resources Required

- **People:** [Roles needed]
- **Tools:** [Systems/software needed]
- **Budget:** [Estimated cost]

## Risks & Mitigation

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [Strategy] |

## Success Criteria

- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

## Next Steps

1. [Immediate action]
2. [Follow-up action]
```

## Success Criteria
- Plan is clear and actionable
- All phases have time estimates
- Resources are identified
- Risks are assessed
- Success criteria are measurable

## Error Handling
- **Vague requirements**: Create plan with assumptions, flag for clarification
- **Missing information**: Note gaps, proceed with best estimates
- **Conflicting constraints**: Highlight conflicts, propose options
- **Too complex**: Break into sub-projects

## Examples

### Example 1: Marketing Campaign
**Input:** "Launch social media campaign for new product"

**Output:**
```markdown
# Project Plan: Social Media Product Launch Campaign

**Created:** 2026-02-16
**Priority:** High
**Deadline:** 2026-03-15
**Estimated Duration:** 4 weeks

## Objective

Launch coordinated social media campaign to generate awareness and leads for new AI Employee product.

## Phases

### Phase 1: Strategy & Content Planning
**Duration:** 1 week
**Deliverable:** Content calendar and messaging framework

Steps:
1. Define target audience and key messages - 2 days
2. Create content calendar (4 weeks of posts) - 2 days
3. Design visual templates - 2 days
4. Get stakeholder approval - 1 day

### Phase 2: Content Creation
**Duration:** 1.5 weeks
**Deliverable:** All posts, graphics, and videos ready

Steps:
1. Write all post copy - 3 days
2. Create graphics and visuals - 3 days
3. Record video content - 2 days
4. Review and revisions - 2 days

### Phase 3: Launch & Monitoring
**Duration:** 1.5 weeks
**Deliverable:** Campaign live with daily monitoring

Steps:
1. Schedule all posts - 1 day
2. Launch campaign - 1 day
3. Daily monitoring and engagement - ongoing
4. Adjust based on performance - ongoing

## Resources Required

- **People:** Marketing manager, content writer, graphic designer
- **Tools:** Social media scheduler, design software, analytics
- **Budget:** $2,000 (ads), $500 (tools)

## Risks & Mitigation

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Content delays | High | Medium | Start 1 week early, have backup content |
| Low engagement | Medium | Medium | A/B test messaging, adjust quickly |
| Budget overrun | Low | Low | Set hard limits, track daily |

## Success Criteria

- [ ] 50+ posts scheduled across platforms
- [ ] 10,000+ impressions in first week
- [ ] 100+ leads generated
- [ ] Engagement rate >3%

## Next Steps

1. Schedule kickoff meeting with team
2. Begin audience research
3. Set up analytics tracking
```

### Example 2: Technical Implementation
**Input:** "Implement user authentication system"

**Output:**
```markdown
# Project Plan: User Authentication System

**Created:** 2026-02-16
**Priority:** High
**Deadline:** 2026-03-01
**Estimated Duration:** 2 weeks

## Objective

Implement secure user authentication with email/password and OAuth options.

## Phases

### Phase 1: Design & Setup
**Duration:** 3 days
**Deliverable:** Architecture design and environment setup

Steps:
1. Design authentication flow - 1 day
2. Choose auth library/service - 0.5 days
3. Set up development environment - 0.5 days
4. Database schema design - 1 day

### Phase 2: Core Implementation
**Duration:** 5 days
**Deliverable:** Working authentication system

Steps:
1. Implement user registration - 1 day
2. Implement login/logout - 1 day
3. Add password reset flow - 1 day
4. Implement OAuth (Google, GitHub) - 2 days

### Phase 3: Security & Testing
**Duration:** 3 days
**Deliverable:** Secure, tested system

Steps:
1. Add security measures (rate limiting, etc.) - 1 day
2. Write unit tests - 1 day
3. Security audit and penetration testing - 1 day

### Phase 4: Deployment
**Duration:** 1 day
**Deliverable:** Live authentication system

Steps:
1. Deploy to staging - 0.5 days
2. Final testing - 0.25 days
3. Deploy to production - 0.25 days

## Resources Required

- **People:** Backend developer, security specialist
- **Tools:** Auth library, database, testing tools
- **Budget:** $0 (using open source)

## Risks & Mitigation

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Security vulnerability | Critical | Low | Security audit, use proven libraries |
| OAuth integration issues | Medium | Medium | Test thoroughly, have fallback |
| Performance problems | Medium | Low | Load testing, caching strategy |

## Success Criteria

- [ ] Users can register and login
- [ ] OAuth works for Google and GitHub
- [ ] Password reset functional
- [ ] All security tests pass
- [ ] Response time <200ms

## Next Steps

1. Review and approve architecture
2. Set up development environment
3. Begin Phase 1 implementation
```

## Planning Best Practices
- Be realistic with time estimates
- Add 20% buffer for unknowns
- Identify dependencies early
- Keep phases focused and deliverable-oriented
- Make success criteria measurable
- Document assumptions clearly
