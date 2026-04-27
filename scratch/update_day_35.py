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
                "## 📚 Theory: Synthesis & Interview Mastery\n",
                "\n"
            ] + [line + "\n" for line in theory_md.split("\n")]
        }
    ]
    
    if is_coding and problems:
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 🔨 Hands-on Labs & Mocks\n"]
        })
        for i, prob in enumerate(problems, 1):
            cells.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"### Mock {i}: {prob['name']}\n", "\n"] + [line + "\n" for line in prob.get('desc', '').split('\n')]
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
            f"## \ud83d\udcdd Day {day} Final Readiness Checklist\n",
            "\n",
            "- [ ] Can you explain the 'Life of a Request' from Browser to Database?\n",
            "- [ ] Are you comfortable saying 'I don't know, but here is how I would find out'?\n",
            "- [ ] Do you have 3 STAR stories specifically about incidents and reliability?\n",
            "- [ ] Can you perform back-of-envelope calculations for 100k RPS in your head?\n"
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

# --- Day 35 CONTENT ---
DAY_35_THEORY = """
### 1. The SRE Troubleshooting Framework
When faced with an outage in an interview, follow this heuristic:
1.  **Define the Scope**: "Is it all regions or just one? All users or a subset?"
2.  **Examine the Signals**: Look at the 4 Golden Signals. Latency? Errors? Saturation?
3.  **Hypothesize & Binary Search**: "If latency is up but DB CPU is low, the bottleneck might be the network or a lock."
4.  **Mitigate**: "I will first rollback the latest config change to restore the SLO."
5.  **Verify**: "I'm checking the metrics to ensure the error rate is returning to baseline."

### 2. SRE Cultural "Gotchas"
- **Blamelessness**: Never blame a person. Blame the system that allowed the person to make the mistake.
- **Error Budgets as a Tool**: They aren't just metrics; they are a **policy**. When the budget is gone, engineering work *stops* and reliability work *starts*.
- **Postmortem Value**: A postmortem is only successful if it results in an **Action Item** that prevents the same failure twice.

### 3. Key Interview Patterns
- **The Slow Service**: Usually a saturation or dependency issue.
- **The Inconsistent Data**: Usually a CAP theorem or consensus (Paxos/Raft) issue.
- **The Failing Release**: Usually a deployment pipeline or canary analysis issue.
- **The Scaling Outage**: Usually a database sharding or global load balancing issue.
"""

DAY_35_PROBLEMS = [
    {
        "name": "Mock Scenario: The Global 500s",
        "desc": "Google Search is returning 500 errors for 20% of traffic in Europe. Monitoring shows high CPU on the API servers. What are your first 3 steps?",
        "code": """# Discussion:
# 1. Triage: Check if a new version was deployed in Europe recently.
# 2. Mitigate: Drain traffic from Europe to the US or Asia (if capacity allows).
# 3. Analyze: Check logs for 'Out of Memory' or 'Thread Pool Exhausted' errors."""
    },
    {
        "name": "The SRE Cheat Sheet (Quick Recall)",
        "desc": "Quickly answer: 1. What is the default TCP timeout? 2. What is the 'OOM Score'? 3. What is a 'Sticky Session'?",
        "code": """# 1. TCP default timeout is OS-dependent but usually 2 minutes for ESTABLISHED.
# 2. OOM Score is a kernel value used to decide which process to kill when memory is low.
# 3. A Sticky Session ensures a user stays on the same backend server for a session duration."""
    }
]

if __name__ == '__main__':
    create_notebook(
        path='week-05-cloud-sre/day-35-review-and-mock.ipynb',
        title="Review & SRE Mock Interview",
        day=35,
        topic="Week 5 — Cloud SRE",
        theory_md=DAY_35_THEORY,
        problems=DAY_35_PROBLEMS
    )
    print("Regenerated Day 35 with extreme detail.")
