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
                "## 📚 Theory: The Math of Reliability\n",
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
            "- [ ] Define SLI, SLO, and SLA without looking them up.\n",
            "- [ ] Calculate the 30-day downtime allowed for 99.95% availability.\n",
            "- [ ] Explain why a burn rate of 14.4 is a common threshold for alerting.\n",
            "- [ ] Draft a set of SLIs for a global key-value store.\n"
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

# --- Day 31 CONTENT ---
DAY_31_THEORY = """
### 1. Service Level Indicators (SLI)
The **metrics** that tell you how your service is performing.
- **Availability**: $Success / Total Requests$.
- **Latency**: Time to service a request (Focus on P99, not Average).
- **Throughput**: Requests per second.
- **Durability**: Probability that data is NOT lost over time.

### 2. Service Level Objectives (SLO)
The **target** you set for your SLI.
- **The Power of 9s**: 
  - 99%: 3.65 days downtime/year.
  - 99.9%: 8.77 hours downtime/year.
  - 99.99%: 52.6 minutes downtime/year.
- **Why not 100%?**: Users don't notice the difference between 99.9% and 100%, and the cost of 100% is exponential.

### 3. Error Budgets
$Error Budget = 1.0 - SLO$.
If your SLO is 99.9%, you have a 0.1% budget for failure. This budget is shared between:
- Planned downtime (maintenance).
- Unplanned downtime (incidents).
- New feature rollouts (which carry risk).

### 4. Burn Rate Alerting
How fast are you using your budget?
- **Burn Rate 1**: You'll exhaust the budget exactly at the end of the window (e.g., 30 days).
- **Burn Rate 14.4**: You'll exhaust 2% of your 30-day budget in 1 hour. (A standard "Critical" alert threshold at Google).
"""

DAY_31_PROBLEMS = [
    {
        "name": "Downtime Calculator",
        "desc": "Write a function that takes an SLO percentage and a window (in days) and returns the allowed downtime in minutes.",
        "code": """def allowed_downtime(slo_percent, window_days):
    total_minutes = window_days * 24 * 60
    error_budget = 1.0 - (slo_percent / 100.0)
    return total_minutes * error_budget

print(f'99.9% SLO for 30 days allows: {allowed_downtime(99.9, 30):.2f} minutes')
print(f'99.99% SLO for 30 days allows: {allowed_downtime(99.99, 30):.2f} minutes')"""
    },
    {
        "name": "Burn Rate Analysis",
        "desc": "Given a 30-day window, how many minutes of downtime constitute a 'Burn Rate of 10' for 1 hour? (Hint: In 1 hour, you expect to lose 1/720th of the budget if Burn Rate=1).",
        "code": """# Discussion:
# 30 days = 720 hours.
# At Burn Rate 1, in 1 hour you use 1/720 of the budget.
# At Burn Rate 10, in 1 hour you use 10/720 (1/72) of the budget."""
    }
]

if __name__ == '__main__':
    create_notebook(
        path='week-05-cloud-sre/day-31-slis-slos-slas.ipynb',
        title="Reliability Math: SLIs, SLOs, SLAs",
        day=31,
        topic="Week 5 — Cloud SRE",
        theory_md=DAY_31_THEORY,
        problems=DAY_31_PROBLEMS
    )
    print("Regenerated Day 31 with extreme detail.")
