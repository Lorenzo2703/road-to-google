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
                "## 📚 Theory: The SRE Response Protocol\n",
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
            "- [ ] Explain why 'Blamelessness' is critical for long-term reliability.\n",
            "- [ ] List the first 3 actions you take when paged for a 10% error rate spike.\n",
            "- [ ] Draft a clear incident status update for external customers.\n",
            "- [ ] Differentiate between an 'Action Item' and a 'Long-term Project' in a postmortem.\n"
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

# --- Day 32 CONTENT ---
DAY_32_THEORY = """
### 1. Incident Roles (ICS - Incident Command System)
- **Incident Commander (IC)**: The ultimate authority. Focuses on the big picture, delegates tasks, and clears roadblocks.
- **Operations Lead (Ops)**: Hands-on technical responder. Executes mitigations (rollbacks, scaling).
- **Communication Lead (Comm)**: Manages internal/external updates. Keeps the 'War Room' quiet so the IC and Ops can work.

### 2. Triage & Mitigation (Stop the Bleeding)
**Triage**: Is it real? What is the impact? (e.g., US-East only? All users?).
**Mitigation**: The goal is to restore the service *quickly*, not to find the root cause yet.
- **Rollback**: Usually the first and best option if a release just happened.
- **Shedding Load**: Dropping non-critical traffic (e.g., background tasks) to save the core API.
- **Isolating**: Cutting off a failing region or service.

### 3. The Troubleshooting Framework
- **What changed?**: 90% of outages are caused by a change (Config, Code, or Traffic).
- **Binary Search**: Isolate the component. Is the error coming from the Load Balancer? The App? The Database?
- **Golden Signals**: Look for the signal that spiked first. Latency up -> Saturation up? Or Saturation up -> Latency up?

### 4. Blameless Postmortems
A postmortem is a document written after an incident is resolved.
- **What happened?**: Timeline of events.
- **Why did it happen?**: Root cause analysis (The 5 Whys).
- **How was it caught?**: Did an alert fire? Or did a user report it?
- **Action Items**: Concrete steps to prevent it from happening again. *Rule: Every incident must have at least one P0 action item to automate the fix.*
"""

DAY_32_PROBLEMS = [
    {
        "name": "Timeline Reconstructor",
        "desc": "Given a mock log file with timestamps and error codes, write a Python function that identifies the exact minute the outage began and the minute it was mitigated (error rate dropped below 1%).",
        "code": """import datetime

logs = [
    ("14:00:01", 200), ("14:00:15", 200), ("14:00:30", 200),
    ("14:01:05", 500), ("14:01:20", 500), ("14:01:45", 500),
    ("14:02:10", 500), ("14:02:40", 200), ("14:03:05", 200)
]

def analyze_incident(logs):
    start_time = None
    end_time = None
    for ts, code in logs:
        if code == 500 and not start_time:
            start_time = ts
        if start_time and code == 200:
            end_time = ts
    return start_time, end_time

start, end = analyze_incident(logs)
print(f'Outage started at: {start}, Mitigated at: {end}')"""
    },
    {
        "name": "The 5 Whys Exercise",
        "desc": "Perform a '5 Whys' analysis for this scenario: 'The database ran out of disk space.'",
        "code": """# Discussion:
# 1. Why? The disk is full of logs.
# 2. Why? Log rotation failed.
# 3. Why? The cron job script had a syntax error.
# 4. Why? The script was updated without testing.
# 5. Why? No CI/CD pipeline for infrastructure scripts."""
    }
]

if __name__ == '__main__':
    create_notebook(
        path='week-05-cloud-sre/day-32-incident-response.ipynb',
        title="Incident Management & Postmortems",
        day=32,
        topic="Week 5 — Cloud SRE",
        theory_md=DAY_32_THEORY,
        problems=DAY_32_PROBLEMS
    )
    print("Regenerated Day 32 with extreme detail.")
