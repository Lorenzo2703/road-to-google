import json
import os

def create_notebook(path, title, day, topic, is_coding=True):
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
                "## 📚 Theory\n",
                "\n",
                "Add theoretical concepts here."
            ]
        }
    ]
    
    if is_coding:
        cells.extend([
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## 🔨 Practice Problems"]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Problem 1\n",
                    "def solve():\n",
                    "    pass\n",
                    "\n",
                    "print('Ready to code!')"
                ]
            }
        ])
    
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            f"## 📝 Day {day} Review\n",
            "\n",
            "- [ ] Concept 1\n",
            "- [ ] Concept 2\n"
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

# Week 2
w2 = 'week-02-intermediate-dsa'
create_notebook(f'{w2}/day-08-binary-search.ipynb', 'Binary Search', 8, 'Week 2 — Intermediate DSA')
create_notebook(f'{w2}/day-09-trees-basics.ipynb', 'Trees Basics', 9, 'Week 2 — Intermediate DSA')
create_notebook(f'{w2}/day-10-trees-advanced.ipynb', 'Trees Advanced', 10, 'Week 2 — Intermediate DSA')
create_notebook(f'{w2}/day-11-heaps-priority-queues.ipynb', 'Heaps & Priority Queues', 11, 'Week 2 — Intermediate DSA')
create_notebook(f'{w2}/day-12-recursion-backtracking.ipynb', 'Recursion & Backtracking', 12, 'Week 2 — Intermediate DSA')
create_notebook(f'{w2}/day-13-sorting-algorithms.ipynb', 'Sorting Algorithms', 13, 'Week 2 — Intermediate DSA')
create_notebook(f'{w2}/day-14-review-and-mock.ipynb', 'Review & Mock', 14, 'Week 2 — Intermediate DSA')

# Week 3
w3 = 'week-03-advanced-dsa'
create_notebook(f'{w3}/day-15-graphs-bfs-dfs.ipynb', 'Graphs: BFS & DFS', 15, 'Week 3 — Advanced DSA')
create_notebook(f'{w3}/day-16-graphs-shortest-path.ipynb', 'Graphs: Shortest Path', 16, 'Week 3 — Advanced DSA')
create_notebook(f'{w3}/day-17-dynamic-programming-1d.ipynb', 'Dynamic Programming 1D', 17, 'Week 3 — Advanced DSA')
create_notebook(f'{w3}/day-18-dynamic-programming-2d.ipynb', 'Dynamic Programming 2D', 18, 'Week 3 — Advanced DSA')
create_notebook(f'{w3}/day-19-tries-and-advanced-strings.ipynb', 'Tries & Advanced Strings', 19, 'Week 3 — Advanced DSA')
create_notebook(f'{w3}/day-20-greedy-algorithms.ipynb', 'Greedy Algorithms', 20, 'Week 3 — Advanced DSA')
create_notebook(f'{w3}/day-21-review-and-mock.ipynb', 'Review & Mock', 21, 'Week 3 — Advanced DSA')

# Week 4
w4 = 'week-04-system-design'
create_notebook(f'{w4}/day-22-system-design-fundamentals.ipynb', 'System Design Fundamentals', 22, 'Week 4 — System Design', False)
create_notebook(f'{w4}/day-23-designing-distributed-systems.ipynb', 'Designing Distributed Systems', 23, 'Week 4 — System Design', False)
create_notebook(f'{w4}/day-24-designing-an-agent-orchestrator.ipynb', 'Designing an Agent Orchestrator', 24, 'Week 4 — System Design', False)
create_notebook(f'{w4}/day-25-designing-an-sdk-platform.ipynb', 'Designing an SDK Platform', 25, 'Week 4 — System Design', False)
create_notebook(f'{w4}/day-26-observability-and-monitoring.ipynb', 'Observability & Monitoring', 26, 'Week 4 — System Design', False)
create_notebook(f'{w4}/day-27-cloud-deployment-patterns.ipynb', 'Cloud Deployment Patterns', 27, 'Week 4 — System Design', False)
create_notebook(f'{w4}/day-28-review-and-mock.ipynb', 'Review & Mock', 28, 'Week 4 — System Design', False)

# Week 5
w5 = 'week-05-agent-development'
create_notebook(f'{w5}/day-29-llm-fundamentals.ipynb', 'LLM Fundamentals', 29, 'Week 5 — Agent Development')
create_notebook(f'{w5}/day-30-agent-architectures.ipynb', 'Agent Architectures', 30, 'Week 5 — Agent Development')
create_notebook(f'{w5}/day-31-google-adk-deep-dive.ipynb', 'Google ADK Deep Dive', 31, 'Week 5 — Agent Development')
create_notebook(f'{w5}/day-32-tool-use-and-function-calling.ipynb', 'Tool Use & Function Calling', 32, 'Week 5 — Agent Development')
create_notebook(f'{w5}/day-33-testing-debugging-agents.ipynb', 'Testing & Debugging Agents', 33, 'Week 5 — Agent Development')
create_notebook(f'{w5}/day-34-agent-deployment-observability.ipynb', 'Agent Deployment & Observability', 34, 'Week 5 — Agent Development')
create_notebook(f'{w5}/day-35-review-and-mock.ipynb', 'Review & Mock', 35, 'Week 5 — Agent Development')

# Week 6
w6 = 'week-06-behavioral-and-final'
create_notebook(f'{w6}/day-36-behavioral-interview-prep.ipynb', 'Behavioral Interview Prep', 36, 'Week 6 — Behavioral & Final', False)
create_notebook(f'{w6}/day-37-googleyness-and-leadership.ipynb', 'Googleyness & Leadership', 37, 'Week 6 — Behavioral & Final', False)
create_notebook(f'{w6}/day-38-system-design-final.ipynb', 'System Design Final', 38, 'Week 6 — Behavioral & Final', False)
create_notebook(f'{w6}/day-39-coding-final-hard.ipynb', 'Coding Final (Hard)', 39, 'Week 6 — Behavioral & Final')
create_notebook(f'{w6}/day-40-mock-interview-full.ipynb', 'Mock Interview Full', 40, 'Week 6 — Behavioral & Final')
create_notebook(f'{w6}/day-41-role-fit-and-portfolio.ipynb', 'Role Fit & Portfolio', 41, 'Week 6 — Behavioral & Final', False)
create_notebook(f'{w6}/day-42-final-review-and-application.ipynb', 'Final Review & Application', 42, 'Week 6 — Behavioral & Final', False)

print("All notebooks generated successfully!")
