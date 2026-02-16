# Python Watcher Setup

## Installation

```bash
pip install watchdog pyyaml
```

## Basic Watcher Script

Create `vault_watcher.py`:

```python
import time
import yaml
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class VaultHandler(FileSystemEventHandler):
    def __init__(self, vault_path):
        self.vault_path = Path(vault_path)
        self.inbox = self.vault_path / "Inbox"

    def on_created(self, event):
        if event.is_directory:
            return

        file_path = Path(event.src_path)

        # Only process markdown files in Inbox
        if file_path.parent == self.inbox and file_path.suffix == '.md':
            print(f"New file detected: {file_path.name}")
            self.process_inbox_item(file_path)

    def process_inbox_item(self, file_path):
        """
        Process new inbox item and route to appropriate folder
        In production, this would call Claude Code via API
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Simple routing logic (expand with AI in production)
            if 'urgent' in content.lower() or 'asap' in content.lower():
                destination = self.vault_path / "Needs_Action"
            elif 'invoice' in content.lower() or '$' in content:
                destination = self.vault_path / "Accounting"
            elif 'proposal' in content.lower() or 'plan' in content.lower():
                destination = self.vault_path / "Plans"
            else:
                destination = self.vault_path / "Needs_Action"

            # Move file
            new_path = destination / file_path.name
            file_path.rename(new_path)
            print(f"Routed to: {destination.name}")

            # Log the action
            self.log_action(file_path.name, destination.name)

        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    def log_action(self, filename, destination):
        """Log routing decision"""
        log_file = self.vault_path / "Logs" / f"activity-{time.strftime('%Y-%m-%d')}.md"

        with open(log_file, 'a', encoding='utf-8') as f:
            timestamp = time.strftime('%H:%M')
            f.write(f"- [{timestamp}] `{filename}` → /{destination}\n")

def main():
    vault_path = Path(__file__).parent

    print(f"Watching vault at: {vault_path}")
    print("Press Ctrl+C to stop")

    event_handler = VaultHandler(vault_path)
    observer = Observer()
    observer.schedule(event_handler, str(vault_path / "Inbox"), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    main()
```

## Advanced Watcher with Claude Code Integration

Create `advanced_watcher.py`:

```python
import time
import subprocess
import json
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class AIVaultHandler(FileSystemEventHandler):
    def __init__(self, vault_path):
        self.vault_path = Path(vault_path)
        self.inbox = self.vault_path / "Inbox"
        self.processing = set()  # Track files being processed

    def on_created(self, event):
        if event.is_directory or event.src_path in self.processing:
            return

        file_path = Path(event.src_path)

        if file_path.parent == self.inbox and file_path.suffix == '.md':
            self.processing.add(event.src_path)
            print(f"🔔 New item: {file_path.name}")
            self.trigger_ai_triage(file_path)
            self.processing.discard(event.src_path)

    def trigger_ai_triage(self, file_path):
        """
        Call Claude Code to process the file using triage skill
        """
        try:
            # Read the triage skill
            skill_path = self.vault_path / "Skills" / "triage.md"

            # Prepare prompt for Claude Code
            prompt = f"""
            Using the triage skill defined in {skill_path}, process this inbox item:

            File: {file_path}

            Read the file, analyze it, and move it to the appropriate folder.
            Log your decision in today's activity log.
            """

            # Call Claude Code (adjust command based on your setup)
            # This is a placeholder - actual implementation depends on your Claude Code setup
            result = subprocess.run(
                ['claude', 'code', '--prompt', prompt],
                capture_output=True,
                text=True,
                cwd=str(self.vault_path)
            )

            if result.returncode == 0:
                print(f"✅ Processed: {file_path.name}")
            else:
                print(f"❌ Error processing: {result.stderr}")

        except Exception as e:
            print(f"❌ Error: {e}")

class ApprovalHandler(FileSystemEventHandler):
    """Watch Pending_Approval folder and notify human"""

    def __init__(self, vault_path):
        self.vault_path = Path(vault_path)
        self.pending = self.vault_path / "Pending_Approval"

    def on_created(self, event):
        if event.is_directory:
            return

        file_path = Path(event.src_path)

        if file_path.parent == self.pending:
            self.notify_approval_needed(file_path)

    def notify_approval_needed(self, file_path):
        """Notify human that approval is needed"""
        print(f"⏳ APPROVAL NEEDED: {file_path.name}")

        # Could integrate with:
        # - Desktop notification
        # - Email
        # - Slack/Discord
        # - SMS

        # Example: Desktop notification (Windows)
        try:
            from plyer import notification
            notification.notify(
                title='AI Employee - Approval Needed',
                message=f'{file_path.name} requires your review',
                timeout=10
            )
        except ImportError:
            pass

def main():
    vault_path = Path(__file__).parent

    print("🤖 AI Employee Vault Watcher")
    print(f"📁 Vault: {vault_path}")
    print("👀 Monitoring: Inbox, Pending_Approval")
    print("⌨️  Press Ctrl+C to stop\n")

    # Set up observers
    observer = Observer()

    # Watch Inbox for new items
    inbox_handler = AIVaultHandler(vault_path)
    observer.schedule(inbox_handler, str(vault_path / "Inbox"), recursive=False)

    # Watch Pending_Approval for items needing review
    approval_handler = ApprovalHandler(vault_path)
    observer.schedule(approval_handler, str(vault_path / "Pending_Approval"), recursive=False)

    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Stopping watcher...")
        observer.stop()

    observer.join()
    print("✅ Watcher stopped")

if __name__ == "__main__":
    main()
```

## Running the Watcher

```bash
# Basic watcher
python vault_watcher.py

# Advanced watcher with AI integration
python advanced_watcher.py

# Run in background (Linux/Mac)
nohup python advanced_watcher.py &

# Run in background (Windows)
pythonw advanced_watcher.py
```

## Systemd Service (Linux)

Create `/etc/systemd/system/ai-vault-watcher.service`:

```ini
[Unit]
Description=AI Employee Vault Watcher
After=network.target

[Service]
Type=simple
User=your-username
WorkingDirectory=/path/to/AI_Employee_Vault
ExecStart=/usr/bin/python3 /path/to/AI_Employee_Vault/advanced_watcher.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable ai-vault-watcher
sudo systemctl start ai-vault-watcher
sudo systemctl status ai-vault-watcher
```

## Windows Task Scheduler

1. Open Task Scheduler
2. Create Basic Task
3. Trigger: At startup
4. Action: Start a program
5. Program: `pythonw.exe`
6. Arguments: `C:\path\to\advanced_watcher.py`
7. Start in: `C:\path\to\AI_Employee_Vault`

## Configuration File

Create `watcher_config.yaml`:

```yaml
vault_path: "."
watch_folders:
  - Inbox
  - Pending_Approval
  - Needs_Action

notifications:
  enabled: true
  methods:
    - desktop
    - email

email:
  smtp_server: "smtp.gmail.com"
  smtp_port: 587
  from_address: "ai-employee@example.com"
  to_address: "you@example.com"

logging:
  level: INFO
  file: "Logs/watcher.log"

ai_integration:
  enabled: true
  claude_code_path: "claude"
  skills_path: "Skills"
```

## Troubleshooting

**Watcher not detecting files:**
- Check file permissions
- Verify folder paths
- Ensure markdown files have .md extension

**High CPU usage:**
- Increase sleep interval
- Reduce recursive watching
- Add file type filters

**Files processed multiple times:**
- Use processing set to track active files
- Add delay before processing
- Check for duplicate observers
