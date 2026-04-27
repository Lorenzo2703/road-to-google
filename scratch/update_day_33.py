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
                "## 📚 Theory: Predicting & Managing Scale\n",
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
            "- [ ] Explain the relationship between arrival rate and response time using Little's Law.\n",
            "- [ ] Identify the 'knee' in a latency/throughput curve.\n",
            "- [ ] Differentiate between Stress Testing and Soak Testing.\n",
            "- [ ] Calculate the number of replicas needed for 20% organic growth + 10% headroom.\n"
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

# --- Day 33 CONTENT ---
DAY_33_THEORY = """
### 1. Utilization and Saturation
- **Utilization**: How much of a resource is being used (e.g., CPU is 60% active).
- **Saturation**: The amount of work the resource cannot handle and is being queued.
- **The Golden Signal connection**: Saturation is often the earliest indicator of impending latency spikes.

### 2. Little's Law
`L = λW`
- `L`: Average number of items in the system.
- `λ`: Average arrival rate (Requests per second).
- `W`: Average wait time (Latency per request).
- **Practical Use**: If your app can handle 100 concurrent requests and average latency is 200ms, your max throughput is $100 / 0.2 = 500\ RPS$.

### 3. Load Testing (Benchmarking)
- **Baseline Testing**: Determining the capacity of a single instance.
- **Stress Testing**: Increasing load until the system breaks to find the bottleneck (CPU, DB Connections, I/O).
- **Soak Testing**: Running at high load for hours/days to find memory leaks or resource exhaustion.
- **Canary Testing**: Using a small % of real production traffic to validate capacity.

### 4. Forecasting & Efficiency
- **Organic Growth**: Steady increase in users.
- **Seasonal Spikes**: Predictable events (e.g., weekend traffic, product launches).
- **Efficiency**: SREs must balance 'Headroom' (spare capacity for spikes) with 'Cost'. 
- **Right-sizing**: Tuning CPU/Memory requests in Kubernetes to match actual usage.
"""

DAY_33_PROBLEMS = [
    {
        "name": "Throughput Calculator",
        "desc": "Write a function that calculates the maximum RPS a cluster can handle given the number of replicas, max concurrency per replica, and average latency.",
        "code": """def max_rps(replicas, concurrency_per_replica, avg_latency_sec):
    total_concurrency = replicas * concurrency_per_replica
    return total_concurrency / avg_latency_sec

# Scenario: 5 replicas, 20 concurrent reqs each, 150ms avg latency
print(f'Max RPS: {max_rps(5, 20, 0.150):.2f}')"""
    },
    {
        "name": "Linear Growth Predictor",
        "desc": "Given current traffic and a monthly growth rate, predict how many replicas you will need in 6 months if you want to keep CPU utilization at 70%.",
        "code": """def predict_replicas(current_traffic_rps, growth_rate, months, capacity_per_replica):
    future_traffic = current_traffic_rps * ((1 + growth_rate) ** months)
    # Replicas needed for future traffic at 70% utilization
    replicas = (future_traffic / capacity_per_replica) / 0.7
    return int(replicas) + 1

# 1000 RPS current, 5% monthly growth, 200 RPS capacity per replica
print(f'Replicas needed in 6 months: {predict_replicas(1000, 0.05, 6, 200)}')"""
    }
]

if __name__ == '__main__':
    create_notebook(
        path='week-05-cloud-sre/day-33-capacity-planning.ipynb',
        title="Capacity Planning & Load Testing",
        day=33,
        topic="Week 5 — Cloud SRE",
        theory_md=DAY_33_THEORY,
        problems=DAY_33_PROBLEMS
    )
    print("Regenerated Day 33 with extreme detail.")
