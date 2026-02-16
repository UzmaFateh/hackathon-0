"""
Plan Engine - Silver Tier Component
Implements reasoning loop: analyze → plan → save → log
Uses the planning_skill to generate structured plans from tasks
"""

import time
from pathlib import Path
from datetime import datetime


class PlanEngine:
    def __init__(self, vault_path):
        self.vault_path = Path(vault_path)
        self.needs_action_folder = self.vault_path / "Needs_Action"
        self.active_projects_folder = self.vault_path / "Active_Projects"
        self.skill_path = self.vault_path / "Silver_Layer" / "skills" / "planning_skill.md"

        # Ensure folders exist
        self.active_projects_folder.mkdir(parents=True, exist_ok=True)

    def read_planning_skill(self):
        """Read the planning skill definition for guidance"""
        try:
            with open(self.skill_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"⚠️  Planning skill not found: {self.skill_path}")
            return None

    def find_tasks_needing_plans(self):
        """Find tasks in Needs_Action that require planning"""
        tasks = list(self.needs_action_folder.glob("*.md"))
        # Filter out templates
        tasks = [t for t in tasks if not t.name.startswith('_template')]
        return tasks

    def analyze_task(self, task_file):
        """
        Analyze task to determine if it needs a plan
        Returns: (needs_plan: bool, complexity: str, priority: str)
        """
        with open(task_file, 'r', encoding='utf-8') as f:
            content = f.read().lower()

        # Simple heuristic analysis
        needs_plan = any(keyword in content for keyword in [
            'project', 'implement', 'launch', 'campaign', 'system', 'build'
        ])

        # Determine complexity
        if any(word in content for word in ['complex', 'multiple', 'phases', 'team']):
            complexity = 'high'
        elif any(word in content for word in ['simple', 'quick', 'small']):
            complexity = 'low'
        else:
            complexity = 'medium'

        # Determine priority
        if any(word in content for word in ['urgent', 'asap', 'critical', 'immediate']):
            priority = 'high'
        elif any(word in content for word in ['low priority', 'when possible', 'eventually']):
            priority = 'low'
        else:
            priority = 'medium'

        return needs_plan, complexity, priority

    def generate_plan(self, task_file, complexity, priority):
        """
        Generate structured plan using planning_skill logic
        This simulates calling Claude Code with the planning skill
        """
        # Read task content
        with open(task_file, 'r', encoding='utf-8') as f:
            task_content = f.read()

        # Extract title
        title_line = task_content.split('\n')[0]
        title = title_line.replace('#', '').strip()

        # Apply planning skill logic
        plan = self.apply_planning_skill(title, task_content, complexity, priority)

        return plan

    def apply_planning_skill(self, title, content, complexity, priority):
        """
        Apply planning skill logic to generate structured plan
        In production, this would call Claude Code API with the skill
        """
        # Estimate duration based on complexity
        duration_map = {
            'low': '3-5 days',
            'medium': '1-2 weeks',
            'high': '3-4 weeks'
        }
        duration = duration_map.get(complexity, '1-2 weeks')

        # Generate deadline (2 weeks from now for demo)
        deadline = datetime.now().strftime('%Y-%m-%d')

        plan = f"""# Project Plan: {title}

**Created:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Priority:** {priority.title()}
**Estimated Duration:** {duration}
**Status:** Draft

## Objective

{self.extract_objective(content)}

## Phases

### Phase 1: Planning & Setup
**Duration:** 2-3 days
**Deliverable:** Project structure and requirements defined

Steps:
1. Define detailed requirements - 1 day
2. Identify resources and dependencies - 1 day
3. Set up project structure - 0.5 days
4. Get stakeholder approval - 0.5 days

### Phase 2: Implementation
**Duration:** {self.estimate_implementation_time(complexity)}
**Deliverable:** Core functionality complete

Steps:
1. Build core components - {self.estimate_step_time(complexity, 0.4)}
2. Integrate systems - {self.estimate_step_time(complexity, 0.3)}
3. Testing and refinement - {self.estimate_step_time(complexity, 0.3)}

### Phase 3: Review & Launch
**Duration:** 2-3 days
**Deliverable:** Project live and documented

Steps:
1. Final review and testing - 1 day
2. Documentation - 1 day
3. Launch and monitoring - 1 day

## Resources Required

- **People:** Project lead, {self.estimate_team_size(complexity)} team members
- **Tools:** Standard development/business tools
- **Budget:** To be determined based on scope

## Risks & Mitigation

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Scope creep | High | Medium | Clear requirements, change control process |
| Resource constraints | Medium | Medium | Prioritize features, adjust timeline |
| Technical challenges | Medium | Low | Research upfront, have backup approaches |

## Success Criteria

- [ ] All phases completed on schedule
- [ ] Deliverables meet quality standards
- [ ] Stakeholder approval obtained
- [ ] Documentation complete

## Next Steps

1. Review and refine this plan
2. Get approval from stakeholders
3. Assign resources and begin Phase 1
4. Set up project tracking

---

*Generated by Silver Layer Plan Engine*
*Source: {content[:100]}...*
*Planning Skill Applied: {datetime.now().isoformat()}*
"""
        return plan

    def extract_objective(self, content):
        """Extract or generate objective from task content"""
        lines = [line.strip() for line in content.split('\n') if line.strip() and not line.startswith('#')]
        if lines:
            return lines[0][:200]
        return "Complete the task as described in the requirements."

    def estimate_implementation_time(self, complexity):
        """Estimate implementation phase duration"""
        time_map = {
            'low': '1-2 days',
            'medium': '5-7 days',
            'high': '2-3 weeks'
        }
        return time_map.get(complexity, '1 week')

    def estimate_step_time(self, complexity, fraction):
        """Estimate time for a step as fraction of implementation"""
        base_days = {'low': 1.5, 'medium': 6, 'high': 17.5}
        days = base_days.get(complexity, 6) * fraction
        if days < 1:
            return f"{days:.1f} days"
        return f"{int(days)} days"

    def estimate_team_size(self, complexity):
        """Estimate team size needed"""
        size_map = {
            'low': '1-2',
            'medium': '2-3',
            'high': '3-5'
        }
        return size_map.get(complexity, '2-3')

    def save_plan(self, plan, task_file):
        """Save generated plan to Active_Projects"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        plan_filename = f"Plan_{task_file.stem}_{timestamp}.md"
        plan_path = self.active_projects_folder / plan_filename

        with open(plan_path, 'w', encoding='utf-8') as f:
            f.write(plan)

        print(f"✅ Plan saved: {plan_filename}")
        return plan_path

    def log_action(self, task_file, plan_path, complexity, priority):
        """Log plan generation"""
        log_dir = self.vault_path / "Silver_Layer" / "logs"
        log_dir.mkdir(exist_ok=True)
        log_file = log_dir / f"plan_engine_{datetime.now().strftime('%Y-%m-%d')}.log"

        with open(log_file, 'a', encoding='utf-8') as f:
            timestamp = datetime.now().strftime('%H:%M:%S')
            f.write(f"[{timestamp}] Generated plan: {task_file.name} → {plan_path.name} "
                   f"(complexity: {complexity}, priority: {priority})\n")

    def process_task(self, task_file):
        """
        Reasoning loop: analyze → plan → save → log
        """
        print(f"\n🔍 Analyzing: {task_file.name}")

        # Step 1: Analyze
        needs_plan, complexity, priority = self.analyze_task(task_file)

        if not needs_plan:
            print(f"   ℹ️  Task doesn't require detailed plan (simple action)")
            return None

        print(f"   📊 Complexity: {complexity}, Priority: {priority}")

        # Step 2: Plan
        print(f"   🧠 Generating plan using planning_skill...")
        plan = self.generate_plan(task_file, complexity, priority)

        # Step 3: Save
        plan_path = self.save_plan(plan, task_file)

        # Step 4: Log
        self.log_action(task_file, plan_path, complexity, priority)

        return plan_path

    def run(self, continuous=False, interval=300):
        """
        Main execution
        If continuous=True, runs as a loop checking for new tasks
        Otherwise, processes current tasks once
        """
        print("🤖 Plan Engine - Silver Layer")
        print(f"📁 Vault: {self.vault_path}")
        print(f"🎯 Mode: {'Continuous' if continuous else 'Single run'}\n")

        if continuous:
            print(f"⏱️  Check interval: {interval}s")
            print("Press Ctrl+C to stop\n")

        try:
            while True:
                tasks = self.find_tasks_needing_plans()
                print(f"Found {len(tasks)} tasks in Needs_Action\n")

                for task in tasks:
                    self.process_task(task)

                if not continuous:
                    break

                print(f"\n⏳ Waiting {interval}s before next check...")
                time.sleep(interval)

        except KeyboardInterrupt:
            print("\n👋 Plan Engine stopped")

        print("\n✅ Plan generation complete")


def main():
    import sys

    vault_path = Path(__file__).parent.parent.parent
    engine = PlanEngine(vault_path)

    # Check for continuous mode flag
    continuous = '--continuous' in sys.argv or '-c' in sys.argv

    engine.run(continuous=continuous)


if __name__ == "__main__":
    main()
