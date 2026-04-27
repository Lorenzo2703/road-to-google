import json
import os

def create_notebook(path, title, day, topic, theory_md, problems, is_coding=True):
    cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"# Day {day:02d}: {title}\n",
                "\n",
                f"**{topic}**\n",
                "\n",
                "---\n",
                "\n",
                "## 📚 Theory: The War on Toil\n",
                "\n"
            ] + [line + "\n" for line in theory_md.split("\n")]
        }
    ]
    
    if is_coding and problems:
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 🔨 Hands-on Labs\n"]
        })
        for i, prob in enumerate(problems, 1):
            cells.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"### Lab {i}: {prob['name']}\n", "\n"] + [line + "\n" for line in prob.get('desc', '').split('\n')]
            })
            cells.append({
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [line + "\n" for line in prob.get('code', 'def solve():\n    pass').split('\n')]
            })

    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            f"## \ud83d\udcdd Day {day} Mastery Checklist\n",
            "\n",
            "- [ ] Audit your current workflow: What % of your time is spent on 'Toil'?\n",
            "- [ ] Explain the difference between 'Scripting' and 'Engineering for Automation'.\n",
            "- [ ] Describe a 'GitOps' workflow for a Kubernetes deployment.\n",
            "- [ ] Identify a manual task that could be replaced by a 'Self-healing' policy.\n"
        ]
    })

    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.10.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1)

# --- Day 34 CONTENT ---
DAY_34_THEORY = """
### 1. Defining Toil
Toil is NOT just "work I don't like." In SRE, Toil has specific characteristics:
- **Manual**: Running a script by hand or clicking in a UI.
- **Repetitive**: Doing the same thing over and over.
- **Automatable**: If a machine could do it, it's toil.
- **Tactical**: Interrupt-driven and not providing long-term value.
- **Scales Linearly**: If traffic doubles, the work doubles.

### 2. The 50% Rule
Google SREs are capped at 50% toil. 
- If toil exceeds 50%, the excess work is handed back to the developer teams. 
- This ensures SREs have time for **Project Work** (improving the system, building automation).

### 3. Automation Strategies
- **Scripts**: Good for one-off tasks, but hard to maintain and lack 'state'.
- **Configuration Management**: (Ansible, Puppet) Ensures a set of machines are in a specific state.
- **Infrastructure as Code (IaC)**: (Terraform, Pulumi) Treating infrastructure exactly like application code.
- **Control Loops**: (Kubernetes) Continuously reconciling 'Desired State' with 'Actual State'. This is the ultimate form of automation.

### 4. GitOps
- The 'Source of Truth' for everything is a Git repository.
- Changes are made via Pull Requests.
- An automated agent (like ArgoCD) detects changes and applies them to the cluster.
- Benefit: Audit trail, easy rollbacks, and no manual access to production needed.
"""

DAY_34_PROBLEMS = [
    {
        "name": "The Toil Auditor",
        "desc": "Write a Python script that parses a mock 'Engineer Activity Log' and calculates what percentage of tasks were 'Toil' vs 'Project Work' based on keywords.",
        "code": """activities = [
    {"task": "Reset database password", "type": "manual"},
    {"task": "Design new autoscaler", "type": "project"},
    {"task": "Manually restart failed pod", "type": "manual"},
    {"task": "Update documentation", "type": "project"},
    {"task": "Run data cleanup script", "type": "manual"}
]

def calculate_toil(activities):
    toil_count = sum(1 for a in activities if a["type"] == "manual")
    total = len(activities)
    return (toil_count / total) * 100

print(f'Toil Percentage: {calculate_toil(activities)}%')"""
    },
    {
        "name": "Declarative vs Imperative",
        "desc": "Explain why a declarative 'End State' (like Terraform) is safer for SREs than an imperative 'Step-by-Step' script.",
        "code": "# Discussion: Declarative handles 'drift' detection and avoids partial failures where a script might fail halfway through."
    }
]

if __name__ == '__main__':
    create_notebook(
        path='week-05-cloud-sre/day-34-automation-and-toil.ipynb',
        title="Automation & Eliminating Toil",
        day=34,
        topic="Week 5 — Cloud SRE",
        theory_md=DAY_34_THEORY,
        problems=DAY_34_PROBLEMS
    )
    print("Regenerated Day 34 with extreme detail.")
