# Running the Watcher

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the watcher:
```bash
python vault_watcher.py
```

3. Test it:
   - Drop a .md file into /Inbox
   - Watch it automatically route to the appropriate folder
   - Check /Logs for activity log

## How It Works

The watcher monitors /Inbox for new markdown files and automatically routes them:
- Files with "urgent" or "asap" → /Needs_Action
- Files with "invoice" or "$" → /Accounting
- Files with "proposal" or "plan" → /Plans
- Everything else → /Needs_Action

All actions are logged in /Logs/watcher-activity-YYYY-MM-DD.md

## Stop the Watcher

Press `Ctrl+C` to stop monitoring.
