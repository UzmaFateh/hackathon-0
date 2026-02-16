# Quick Start Guide

## Welcome to Your AI Employee System

This guide will help you get your Personal AI Employee operational in 30 minutes.

## Prerequisites

- [ ] Obsidian installed
- [ ] Claude Code installed and configured
- [ ] Python 3.8+ installed
- [ ] Node.js installed (for MCP servers)

## Step 1: Verify Vault Structure (2 minutes)

Open this vault in Obsidian and verify all folders exist:

```
✓ /Inbox
✓ /Needs_Action
✓ /Plans
✓ /Pending_Approval
✓ /Approved
✓ /Rejected
✓ /Active_Projects
✓ /Done
✓ /Logs
✓ /Accounting
✓ /Briefings
✓ /Skills
```

## Step 2: Customize Core Documents (5 minutes)

1. **Open Dashboard.md**
   - Replace {{date}} and {{time}} placeholders
   - Add your initial priorities

2. **Open Company_Handbook.md**
   - Review and adjust policies to your needs
   - Customize decision authority levels

3. **Open Business_Goals.md**
   - Define your vision and objectives
   - Set realistic KPI targets
   - Add your specific goals

## Step 3: Set Up Python Watcher (10 minutes)

1. **Install dependencies:**
   ```bash
   pip install watchdog pyyaml
   ```

2. **Create watcher script:**
   - Copy code from `WATCHER_SETUP.md`
   - Save as `vault_watcher.py` in vault root
   - Adjust `vault_path` if needed

3. **Test the watcher:**
   ```bash
   python vault_watcher.py
   ```

4. **Verify it's working:**
   - Create a test file in `/Inbox`
   - Watch it get routed automatically

## Step 4: Configure MCP Servers (10 minutes)

1. **Choose your MCP servers** (start with these):
   - Filesystem (essential)
   - Web search (recommended)
   - GitHub (if you use it)

2. **Get API keys:**
   - Brave Search: https://brave.com/search/api/
   - GitHub: https://github.com/settings/tokens

3. **Update Claude Code config:**
   - Follow instructions in `MCP_SETUP.md`
   - Add at least the filesystem server

4. **Test MCP servers:**
   ```bash
   # Restart Claude Code after config changes
   ```

## Step 5: Test the Workflow (5 minutes)

### Test 1: Inbox Processing

1. Create a test task in `/Inbox/test-task.md`:
   ```markdown
   # Urgent: Review quarterly report

   Need to review Q4 financial report by Friday.
   Requires analysis of revenue trends.
   ```

2. Watch the watcher route it to `/Needs_Action`

3. Verify the routing was logged in `/Logs`

### Test 2: Create a Plan

1. Copy `/Plans/_template_plan.md` to `/Plans/test-plan.md`

2. Fill in a simple plan (e.g., "Organize digital files")

3. Move to `/Pending_Approval` when ready

### Test 3: Approval Workflow

1. Review the plan in `/Pending_Approval`

2. Make your decision (approve/reject)

3. Move to appropriate folder:
   - Approved → `/Approved`
   - Rejected → `/Rejected`

## Step 6: Daily Operations

### Morning Routine (5 minutes)
1. Open `Dashboard.md`
2. Review `/Needs_Action` folder
3. Check `/Pending_Approval` for items needing review
4. Set today's priorities

### Throughout the Day
- Add new items to `/Inbox`
- Let watcher route them automatically
- Review and approve items as needed
- Update active projects

### Evening Routine (5 minutes)
1. Review what was completed
2. Move completed items to `/Done`
3. Check tomorrow's priorities
4. Review daily activity log

## Common Workflows

### Creating a New Task
```
1. Create file in /Inbox
2. Watcher detects and routes
3. AI processes based on content
4. Appears in appropriate folder
```

### Executing a Project
```
1. Create plan in /Plans
2. Move to /Pending_Approval
3. Human reviews and approves
4. Move to /Approved
5. Create project in /Active_Projects
6. Track progress
7. Move to /Done when complete
```

### Getting AI Help
```
1. Create task describing what you need
2. Reference appropriate skill (research, draft, etc.)
3. AI executes using skill guidelines
4. Reviews output in /Pending_Approval
5. Approve or request revisions
```

## Tips for Success

### Do's
- ✅ Process inbox daily
- ✅ Review pending approvals promptly
- ✅ Keep Dashboard.md updated
- ✅ Use templates for consistency
- ✅ Tag items appropriately
- ✅ Link related items
- ✅ Review logs weekly

### Don'ts
- ❌ Let inbox pile up
- ❌ Skip approval reviews
- ❌ Ignore rejected items (learn from them)
- ❌ Create files outside the structure
- ❌ Forget to update project status
- ❌ Neglect to log important decisions

## Customization Ideas

### Add Custom Skills
Create new skills in `/Skills` for:
- Email drafting
- Meeting notes summarization
- Code review
- Data analysis
- Report generation

### Integrate More Tools
Add MCP servers for:
- Calendar management
- Email processing
- Database access
- API integrations
- Cloud storage

### Automate More
Extend Python watcher to:
- Send notifications
- Generate daily briefings
- Update metrics automatically
- Sync with external tools

## Troubleshooting

### Watcher Not Working
```bash
# Check if Python is running
ps aux | grep vault_watcher  # Linux/Mac
tasklist | findstr python    # Windows

# Check logs
tail -f Logs/watcher.log
```

### Files Not Routing
- Verify file is in `/Inbox`
- Check file has `.md` extension
- Ensure watcher is running
- Review watcher logs for errors

### MCP Servers Not Connecting
- Verify API keys are correct
- Check config file syntax
- Restart Claude Code
- Test servers individually

### AI Not Following Skills
- Ensure skill files are in `/Skills`
- Check skill format matches template
- Verify skill is referenced in task
- Review skill success criteria

## Next Steps

Now that you're set up:

1. **Week 1: Learn the System**
   - Use it daily
   - Test all workflows
   - Identify pain points

2. **Week 2: Optimize**
   - Add custom skills
   - Refine routing rules
   - Integrate more tools

3. **Week 3: Scale**
   - Automate more tasks
   - Add advanced workflows
   - Measure improvements

4. **Week 4: Review**
   - Analyze metrics
   - Adjust goals
   - Plan enhancements

## Getting Help

- **Documentation:** Review all `.md` files in vault root
- **Skills Reference:** Check `/Skills` folder
- **Templates:** Use `_template_*.md` files
- **Logs:** Check `/Logs` for activity history

## Success Metrics to Track

After 30 days, measure:
- Tasks automated: Target 50+
- Time saved per week: Target 10+ hours
- Approval rate: Target 85%+
- Response time: Target <2 hours
- Error rate: Target <5%

---

**You're ready to go! Start by creating your first task in `/Inbox`.**
