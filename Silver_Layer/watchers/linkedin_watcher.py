"""
LinkedIn Watcher - Silver Tier Component
Monitors LinkedIn engagement and saves relevant interactions to vault
"""

import time
import json
from pathlib import Path
from datetime import datetime


class LinkedInWatcher:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
        self.vault_path = Path(self.config.get('vault_path', '../..'))
        self.inbox_folder = self.vault_path / "Inbox"
        self.check_interval = self.config.get('check_interval', 600)  # 10 minutes default

    def load_config(self, config_path):
        """Load configuration from JSON file"""
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Config file not found: {config_path}")
            return {}

    def simulate_linkedin_check(self):
        """
        Simulate checking LinkedIn for engagement
        In production, this would use LinkedIn API
        """
        # Simulated LinkedIn interactions
        interactions = [
            {
                'type': 'comment',
                'post_title': 'AI Employee System Launch',
                'author': 'John Smith',
                'content': 'This looks interesting! Can you share more details?',
                'timestamp': datetime.now().isoformat()
            },
            {
                'type': 'message',
                'from': 'Sarah Johnson',
                'subject': 'Partnership Opportunity',
                'content': 'I saw your post about AI automation. Would love to discuss collaboration.',
                'timestamp': datetime.now().isoformat()
            }
        ]
        return interactions

    def process_interaction(self, interaction):
        """
        Convert LinkedIn interaction to markdown and save to Inbox
        Bronze watcher will then route it appropriately
        """
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        interaction_type = interaction['type']

        if interaction_type == 'comment':
            title = f"LinkedIn Comment on {interaction['post_title']}"
            author = interaction['author']
        else:
            title = f"LinkedIn Message: {interaction['subject']}"
            author = interaction['from']

        filename = f"linkedin_{interaction_type}_{timestamp}.md"
        filepath = self.inbox_folder / filename

        content = f"""# {title}

**Type:** LinkedIn {interaction_type.title()}
**From:** {author}
**Received:** {interaction['timestamp']}

---

{interaction['content']}

---

*Source: LinkedIn Watcher (Silver Layer)*
*Processed: {datetime.now().isoformat()}*
*Action Required: Review and respond*
"""

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"💼 LinkedIn {interaction_type} saved: {filename}")
        self.log_action(filename, interaction)

    def log_action(self, filename, interaction):
        """Log LinkedIn interaction processing"""
        log_dir = self.vault_path / "Silver_Layer" / "logs"
        log_dir.mkdir(exist_ok=True)
        log_file = log_dir / f"linkedin_watcher_{datetime.now().strftime('%Y-%m-%d')}.log"

        with open(log_file, 'a', encoding='utf-8') as f:
            timestamp = datetime.now().strftime('%H:%M:%S')
            f.write(f"[{timestamp}] Processed: {interaction['type']} - {filename}\n")

    def run(self):
        """Main watcher loop"""
        print(f"🔍 LinkedIn Watcher started")
        print(f"📁 Vault: {self.vault_path}")
        print(f"⏱️  Check interval: {self.check_interval}s")
        print("Press Ctrl+C to stop\n")

        try:
            while True:
                interactions = self.simulate_linkedin_check()

                for interaction in interactions:
                    self.process_interaction(interaction)

                time.sleep(self.check_interval)

        except KeyboardInterrupt:
            print("\n👋 LinkedIn Watcher stopped")


def main():
    config_path = Path(__file__).parent / "linkedin_config.json"
    watcher = LinkedInWatcher(config_path)
    watcher.run()


if __name__ == "__main__":
    main()
