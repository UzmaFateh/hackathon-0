"""
Approval Flow - Silver Tier Component
Implements human-in-the-loop approval for sensitive actions
Checks for approval flags before proceeding with actions
"""

import time
from pathlib import Path
from datetime import datetime


class ApprovalFlow:
    def __init__(self, vault_path):
        self.vault_path = Path(vault_path)
        self.pending_approval_folder = self.vault_path / "Pending_Approval"
        self.approved_folder = self.vault_path / "Approved"
        self.rejected_folder = self.vault_path / "Rejected"
        self.check_interval = 60  # Check every minute

    def find_pending_items(self):
        """Find items awaiting approval"""
        pending_items = list(self.pending_approval_folder.glob("*.md"))
        # Filter out templates
        pending_items = [p for p in pending_items if not p.name.startswith('_template')]
        return pending_items

    def check_approval_status(self, item_path):
        """
        Check if item has been approved or rejected
        Returns: ('approved', flag_path) or ('rejected', flag_path) or ('pending', None)
        """
        # Check for approval flag
        approved_flag = item_path.parent / f"{item_path.name}.approved.flag"
        if approved_flag.exists():
            return 'approved', approved_flag

        # Check for rejection flag
        rejected_flag = item_path.parent / f"{item_path.name}.rejected.flag"
        if rejected_flag.exists():
            return 'rejected', rejected_flag

        return 'pending', None

    def process_approved_item(self, item_path, flag_path):
        """
        Process an approved item
        Move to Approved folder and execute associated action
        """
        print(f"✅ APPROVED: {item_path.name}")

        # Read approval notes if any
        try:
            with open(flag_path, 'r', encoding='utf-8') as f:
                approval_notes = f.read().strip()
        except:
            approval_notes = "No notes provided"

        # Move item to Approved folder
        approved_path = self.approved_folder / item_path.name
        item_path.rename(approved_path)

        # Remove flag file
        flag_path.unlink()

        # Log approval
        self.log_action(item_path.name, 'approved', approval_notes)

        # Execute associated action
        self.execute_approved_action(approved_path)

        return approved_path

    def process_rejected_item(self, item_path, flag_path):
        """
        Process a rejected item
        Move to Rejected folder with rejection reason
        """
        print(f"❌ REJECTED: {item_path.name}")

        # Read rejection reason
        try:
            with open(flag_path, 'r', encoding='utf-8') as f:
                rejection_reason = f.read().strip()
        except:
            rejection_reason = "No reason provided"

        # Add rejection metadata to file
        with open(item_path, 'a', encoding='utf-8') as f:
            f.write(f"\n\n---\n\n## REJECTION\n\n")
            f.write(f"**Rejected:** {datetime.now().isoformat()}\n")
            f.write(f"**Reason:** {rejection_reason}\n")

        # Move item to Rejected folder
        rejected_path = self.rejected_folder / item_path.name
        item_path.rename(rejected_path)

        # Remove flag file
        flag_path.unlink()

        # Log rejection
        self.log_action(item_path.name, 'rejected', rejection_reason)

        return rejected_path

    def execute_approved_action(self, approved_path):
        """
        Execute the action associated with an approved item
        Determines action type from filename and executes accordingly
        """
        filename = approved_path.name

        if 'email_draft' in filename:
            self.execute_email_send(approved_path)
        elif 'linkedin_post' in filename:
            self.execute_linkedin_post(approved_path)
        else:
            print(f"   ℹ️  No automatic action for this item type")

    def execute_email_send(self, email_draft_path):
        """
        Execute email sending (simulated)
        In production, would actually send via SMTP/API
        """
        print(f"   📧 Executing: Send email")

        # Read email content
        with open(email_draft_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract recipient and subject (simplified parsing)
        lines = content.split('\n')
        recipient = None
        subject = None

        for line in lines:
            if line.startswith('**Recipient:**'):
                recipient = line.split('**Recipient:**')[1].strip()
            elif line.startswith('**Subject:**'):
                subject = line.split('**Subject:**')[1].strip()

        # Simulate sending
        print(f"   → To: {recipient}")
        print(f"   → Subject: {subject}")
        print(f"   → Status: SIMULATED SEND (would send in production)")

        # Log send action
        log_dir = self.vault_path / "Silver_Layer" / "logs"
        log_dir.mkdir(exist_ok=True)
        log_file = log_dir / f"email_sent_{datetime.now().strftime('%Y-%m-%d')}.log"

        with open(log_file, 'a', encoding='utf-8') as f:
            timestamp = datetime.now().strftime('%H:%M:%S')
            f.write(f"[{timestamp}] SENT: {recipient} - {subject}\n")

    def execute_linkedin_post(self, post_draft_path):
        """
        Execute LinkedIn posting (simulated)
        In production, would post via LinkedIn API
        """
        print(f"   💼 Executing: Post to LinkedIn")

        # Read post content
        with open(post_draft_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Simulate posting
        print(f"   → Status: SIMULATED POST (would post in production)")

        # Log post action
        log_dir = self.vault_path / "Silver_Layer" / "logs"
        log_dir.mkdir(exist_ok=True)
        log_file = log_dir / f"linkedin_posted_{datetime.now().strftime('%Y-%m-%d')}.log"

        with open(log_file, 'a', encoding='utf-8') as f:
            timestamp = datetime.now().strftime('%H:%M:%S')
            f.write(f"[{timestamp}] POSTED: {post_draft_path.name}\n")

    def log_action(self, item_name, action, notes):
        """Log approval/rejection action"""
        log_dir = self.vault_path / "Silver_Layer" / "logs"
        log_dir.mkdir(exist_ok=True)
        log_file = log_dir / f"approval_flow_{datetime.now().strftime('%Y-%m-%d')}.log"

        with open(log_file, 'a', encoding='utf-8') as f:
            timestamp = datetime.now().strftime('%H:%M:%S')
            f.write(f"[{timestamp}] {action.upper()}: {item_name}\n")
            if notes:
                f.write(f"           Notes: {notes}\n")

    def create_approval_instructions(self, item_path):
        """
        Create instruction file for human reviewer
        """
        instructions_path = self.pending_approval_folder / "APPROVAL_INSTRUCTIONS.md"

        if not instructions_path.exists():
            instructions = f"""# Approval Instructions

## How to Approve an Item

1. Review the item in `/Pending_Approval`
2. If you approve, create a flag file:
   - Filename: `[item_name].approved.flag`
   - Example: `email_draft_Project_Update_20260216.md.approved.flag`
   - Content: Optional approval notes

3. The system will detect the flag and:
   - Move item to `/Approved`
   - Execute the associated action
   - Log the approval

## How to Reject an Item

1. Review the item in `/Pending_Approval`
2. If you reject, create a flag file:
   - Filename: `[item_name].rejected.flag`
   - Example: `email_draft_Project_Update_20260216.md.rejected.flag`
   - Content: Rejection reason (required)

3. The system will detect the flag and:
   - Move item to `/Rejected`
   - Add rejection reason to file
   - Log the rejection

## Quick Approval (Windows)

```cmd
echo Approved > "Pending_Approval\\[filename].approved.flag"
```

## Quick Approval (Mac/Linux)

```bash
touch "Pending_Approval/[filename].approved.flag"
```

## Current Pending Items

Check `/Pending_Approval` folder for items awaiting your review.

---

*This file is auto-generated by the Approval Flow system*
"""
            with open(instructions_path, 'w', encoding='utf-8') as f:
                f.write(instructions)

    def run(self, continuous=True):
        """
        Main approval flow loop
        Continuously checks for approval/rejection flags
        """
        print("🔐 Approval Flow - Silver Layer")
        print(f"📁 Vault: {self.vault_path}")
        print(f"⏱️  Check interval: {self.check_interval}s")
        print("Press Ctrl+C to stop\n")

        # Create instructions file
        self.create_approval_instructions(None)

        try:
            while True:
                pending_items = self.find_pending_items()

                if pending_items:
                    print(f"📋 Found {len(pending_items)} pending items")

                    for item in pending_items:
                        status, flag_path = self.check_approval_status(item)

                        if status == 'approved':
                            self.process_approved_item(item, flag_path)
                        elif status == 'rejected':
                            self.process_rejected_item(item, flag_path)
                        # else: still pending, do nothing

                if not continuous:
                    break

                time.sleep(self.check_interval)

        except KeyboardInterrupt:
            print("\n👋 Approval Flow stopped")

        print("\n✅ Approval processing complete")


def main():
    import sys

    vault_path = Path(__file__).parent.parent.parent
    flow = ApprovalFlow(vault_path)

    # Check for single-run mode
    continuous = '--continuous' not in sys.argv and '-c' not in sys.argv

    flow.run(continuous=continuous)


if __name__ == "__main__":
    main()
