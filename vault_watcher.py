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
        log_file = self.vault_path / "Logs" / f"watcher-activity-{time.strftime('%Y-%m-%d')}.md"

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
