"""
Gmail Watcher - Silver Tier Component
Monitors Gmail inbox and routes emails to vault
"""

import time
import json
from pathlib import Path
from datetime import datetime


class GmailWatcher:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
        self.vault_path = Path(self.config.get('vault_path', '../..'))
        self.inbox_folder = self.vault_path / "Inbox"
        self.check_interval = self.config.get('check_interval', 300)  # 5 minutes default

    def load_config(self, config_path):
        """Load configuration from JSON file"""
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Config file not found: {config_path}")
            return {}

    def simulate_gmail_check(self):
        """
        Simulate checking Gmail inbox
        In production, this would use Gmail API
        """
        # Simulated email data
        emails = [
            {
                'subject': 'Project Update Request',
                'from': 'client@example.com',
                'body': 'Can you provide an update on the marketing project?',
                'timestamp': datetime.now().isoformat()
            }
        ]
        return emails

    def process_email(self, email):
        """
        Convert email to markdown and save to Inbox
        Bronze watcher will then route it appropriately
        """
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"email_{timestamp}_{email['subject'].replace(' ', '_')[:30]}.md"
        filepath = self.inbox_folder / filename

        content = f"""# Email: {email['subject']}

**From:** {email['from']}
**Received:** {email['timestamp']}

---

{email['body']}

---

*Source: Gmail Watcher (Silver Layer)*
*Processed: {datetime.now().isoformat()}*
"""

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✉️  Email saved: {filename}")
        self.log_action(filename, email)

    def log_action(self, filename, email):
        """Log email processing"""
        log_dir = self.vault_path / "Silver_Layer" / "logs"
        log_dir.mkdir(exist_ok=True)
        log_file = log_dir / f"gmail_watcher_{datetime.now().strftime('%Y-%m-%d')}.log"

        with open(log_file, 'a', encoding='utf-8') as f:
            timestamp = datetime.now().strftime('%H:%M:%S')
            f.write(f"[{timestamp}] Processed: {email['subject']} from {email['from']}\n")

    def run(self):
        """Main watcher loop"""
        print(f"🔍 Gmail Watcher started")
        print(f"📁 Vault: {self.vault_path}")
        print(f"⏱️  Check interval: {self.check_interval}s")
        print("Press Ctrl+C to stop\n")

        try:
            while True:
                emails = self.simulate_gmail_check()

                for email in emails:
                    self.process_email(email)

                time.sleep(self.check_interval)

        except KeyboardInterrupt:
            print("\n👋 Gmail Watcher stopped")


def main():
    config_path = Path(__file__).parent / "gmail_config.json"
    watcher = GmailWatcher(config_path)
    watcher.run()


if __name__ == "__main__":
    main()
