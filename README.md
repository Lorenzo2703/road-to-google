# 🚀 Road to Google — SWE II, Agent Development

> A comprehensive, structured preparation plan to maximize chances of landing a **Software Engineer II, Agent Development** role at Google.

[![Google](https://img.shields.io/badge/Google-SWE%20II-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://www.google.com/about/careers/applications/jobs/results/90093189238530758-software-engineer-ii-agent-development)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![LeetCode](https://img.shields.io/badge/LeetCode-Practice-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](#)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#license)

---

## 📋 About This Repository

This repository contains a **42-day structured preparation plan** for the Google SWE II, Agent Development position. Every day includes theory, practice problems, and hands-on coding exercises organized as Jupyter notebooks.

### 🎯 Target Role

| Field | Details |
|-------|---------|
| **Position** | Software Engineer II, Agent Development |
| **Company** | Google |
| **Team** | Agent Development Kit (ADK) |
| **Focus** | Open-source SDKs, AI agent lifecycle tooling |
| **Level** | L4 (Mid-level) |

### 📌 Role Responsibilities

- Design, develop, and maintain quality, open-source SDKs for the **Agent Development Kit (ADK)** framework
- Build and improve tooling to support the **AI agent development lifecycle** (testing, debugging, deployment, observability)
- Collaborate with internal and external developers to translate needs into **new features**
- Work with cloud teams for **deployment and management of AI agents** on Google Cloud Platform

### 📌 Minimum Qualifications

- Bachelor's degree or equivalent practical experience
- 1 year of experience with software development (Python, C, C++, Java, JavaScript)
- 1 year of experience with data structures and algorithms

### 📌 Preferred Qualifications

- Experience with AI, machine learning, LLMs, or AI agents
- Experience building applications for enterprise needs (AI safety, data residency, system integration)
- Understanding of the needs of Cloud customers
- Ability to bridge the gap between AI technology and real-world use cases

---

## 📂 Repository Structure

```
road-to-google/
│
├── README.md                          # This file
├── ROADMAP.md                         # Detailed 6-week roadmap
├── CHECKLIST.md                       # Complete preparation checklist
├── PRESENTATION.md                    # Interview presentation deck
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Git ignore rules
│
├── week-01-fundamentals/              # DSA Foundations
│   ├── day-01-arrays-and-strings.ipynb
│   ├── day-02-hashmaps-and-sets.ipynb
│   ├── day-03-two-pointers.ipynb
│   ├── day-04-sliding-window.ipynb
│   ├── day-05-stacks-and-queues.ipynb
│   ├── day-06-linked-lists.ipynb
│   └── day-07-review-and-mock.ipynb
│
├── week-02-intermediate-dsa/          # Intermediate DSA
│   ├── day-08-binary-search.ipynb
│   ├── day-09-trees-basics.ipynb
│   ├── day-10-trees-advanced.ipynb
│   ├── day-11-heaps-priority-queues.ipynb
│   ├── day-12-recursion-backtracking.ipynb
│   ├── day-13-sorting-algorithms.ipynb
│   └── day-14-review-and-mock.ipynb
│
├── week-03-advanced-dsa/              # Advanced DSA
│   ├── day-15-graphs-bfs-dfs.ipynb
│   ├── day-16-graphs-shortest-path.ipynb
│   ├── day-17-dynamic-programming-1d.ipynb
│   ├── day-18-dynamic-programming-2d.ipynb
│   ├── day-19-tries-and-advanced-strings.ipynb
│   ├── day-20-greedy-algorithms.ipynb
│   └── day-21-review-and-mock.ipynb
│
├── week-04-system-design/             # System Design
│   ├── day-22-system-design-fundamentals.ipynb
│   ├── day-23-designing-distributed-systems.ipynb
│   ├── day-24-designing-an-agent-orchestrator.ipynb
│   ├── day-25-designing-an-sdk-platform.ipynb
│   ├── day-26-observability-and-monitoring.ipynb
│   ├── day-27-cloud-deployment-patterns.ipynb
│   └── day-28-review-and-mock.ipynb
│
├── week-05-agent-development/         # Role-Specific: Agent Development
│   ├── day-29-llm-fundamentals.ipynb
│   ├── day-30-agent-architectures.ipynb
│   ├── day-31-google-adk-deep-dive.ipynb
│   ├── day-32-tool-use-and-function-calling.ipynb
│   ├── day-33-testing-debugging-agents.ipynb
│   ├── day-34-agent-deployment-observability.ipynb
│   └── day-35-review-and-mock.ipynb
│
├── week-06-behavioral-and-final/      # Behavioral + Final Prep
│   ├── day-36-behavioral-interview-prep.ipynb
│   ├── day-37-googleyness-and-leadership.ipynb
│   ├── day-38-system-design-final.ipynb
│   ├── day-39-coding-final-hard.ipynb
│   ├── day-40-mock-interview-full.ipynb
│   ├── day-41-role-fit-and-portfolio.ipynb
│   └── day-42-final-review-and-application.ipynb
│
├── behavioral/                        # Behavioral Interview Resources
│   ├── star-stories.md                # STAR method story bank
│   ├── googleyness-questions.md       # Googleyness & Leadership questions
│   └── behavioral-prep.md            # Full behavioral preparation guide
│
├── system-design/                     # System Design Resources
│   ├── fundamentals.md                # Core system design concepts
│   ├── agent-systems.md               # Agent-specific system design
│   └── practice-problems.md           # System design practice problems
│
├── role-specific/                     # Agent Development Resources
│   ├── adk-preparation.md             # ADK deep dive
│   ├── agent-engineering.md           # Agent engineering fundamentals
│   ├── portfolio-projects.md          # Suggested portfolio projects
│   └── enterprise-ai.md              # Enterprise AI considerations
│
└── leetcode/                          # LeetCode Problem Lists
    ├── plan.md                        # Complete LeetCode plan
    ├── google-tagged.md               # Google-tagged problems
    └── topic-wise.md                  # Problems organized by topic
```

---

## 🗓️ 6-Week Overview

| Week | Focus Area | Days | Key Outcomes |
|------|-----------|------|-------------|
| **Week 1** | DSA Foundations | 1-7 | Arrays, HashMaps, Two Pointers, Sliding Window, Stacks, Linked Lists |
| **Week 2** | Intermediate DSA | 8-14 | Binary Search, Trees, Heaps, Recursion, Sorting |
| **Week 3** | Advanced DSA | 15-21 | Graphs, Dynamic Programming, Tries, Greedy |
| **Week 4** | System Design | 22-28 | Distributed Systems, Agent Orchestrator, SDK Design, Cloud |
| **Week 5** | Agent Development | 29-35 | LLMs, Agent Architectures, ADK, Testing, Deployment |
| **Week 6** | Behavioral & Final | 36-42 | Behavioral, Googleyness, Mock Interviews, Application |

### 📚 Supplementary Materials
For topics that cross-cut multiple weeks or provide deep-dives into CS fundamentals:

| Folder | Contents |
|--------|----------|
| `supplementary-material/` | Deep dives into OS, Math, and Advanced Algorithms |
| `interview-questions-deep-dive.ipynb` | Specific behavioral and probabilistic questions |
| `operating-systems-and-concurrency.ipynb` | Threads, Locks, Deadlocks, Context Switching |
| `probability-and-combinatorics.ipynb` | N choose K, Expected Value, Bayes' Theorem |
| `np-complete-and-heuristics.ipynb` | TSP, Knapsack, and Heuristic strategies |

---

## 🗺️ The 6-Week Roadmap

### Week 1: Fundamentals & Basic Data Structures
- Arrays, Hash Tables, Linked Lists, Stacks, Queues.
- Big O Notation (Time/Space Complexity).
- Edge Cases & Corner Cases.

### Week 2: Intermediate DSA
- Trees (BST, BFS/DFS).
- Heaps & Priority Queues.
- Recursion & Backtracking.
- Sorting Algorithms & Interval Merging.

### Week 3: Advanced DSA & Graph Theory
- Graphs (BFS/DFS, Matrix vs Adjacency List).
- Connectivity, Cycle Detection, and Shortest Paths (Dijkstra).
- Dynamic Programming (1D & 2D).
- Tries (Prefix Trees).
- Greedy Algorithms.

### Week 4: System Design & Infrastructure
- Distributed Systems, Load Balancing, Caching, CDNs.
- Databases (SQL vs NoSQL, Sharding, Replication).
- API Design, SDK Development, and Backward Compatibility.
- Observability (Logging, Metrics, Tracing).
- Cloud Deployment (K8s, Docker, CI/CD).
- **Operating Systems**: Processes, Threads, Concurrency, Mutexes, Locks.

### Week 5: Agent Development & LLMs
- LLM Fundamentals (Tokenization, Prompt Engineering).
- Agent Architectures (ReAct, Multi-Agent Orchestration).
- Google ADK Deep Dive & Tool Use.
- Testing, Debugging, and Safety Guardrails for AI.

### Week 6: Behavioral & Final Polish
- STAR Method & Behavioral Interviewing.
- Googleyness & Leadership (GCA).
- Full Mock Interviews (Coding, Design, Behavioral).
- Role-Specific Pitch & Portfolio Optimization.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Jupyter Notebook or JupyterLab
- Git

### Setup

```bash
# Clone this repository
git clone https://github.com/YOUR_USERNAME/road-to-google.git
cd road-to-google

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

### Daily Workflow

1. Open the notebook for today's challenge
2. Read the **Theory** section carefully
3. Attempt each **Practice Problem** before looking at solutions
4. Complete the **Daily Challenge** at the end
5. Update the checklist in `CHECKLIST.md`
6. Commit your progress

---

## 📊 Progress Tracking

Track your daily progress using the checkboxes in [CHECKLIST.md](./CHECKLIST.md).

```
Day 01: ✅ Arrays and Strings — Completed 3/3 problems
Day 02: 🔄 HashMaps and Sets — In progress
Day 03: ⬜ Two Pointers — Not started
```

---

## 📚 Key Resources

| Resource | Purpose |
|----------|---------|
| [LeetCode](https://leetcode.com) | Algorithm practice |
| [NeetCode](https://neetcode.io) | Curated problem sets |
| [System Design Primer](https://github.com/donnemartin/system-design-primer) | System design fundamentals |
| [Google ADK Docs](https://google.github.io/adk-docs/) | Agent Development Kit |
| [Google ADK GitHub](https://github.com/google/adk-python) | ADK source code |
| [Designing Data-Intensive Apps](https://dataintensive.net/) | Distributed systems |
| [Tech Interview Handbook](https://www.techinterviewhandbook.org/) | Interview prep |
| [Cracking the Coding Interview](http://www.crackingthecodinginterview.com/) | Classic interview prep |

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

> *"The only way to do great work is to love what you do."* — Steve Jobs

**Good luck on your journey to Google! 🎯**


# Useful links
* [Grok Test](https://grok.com/assessment/4)
* https://github.com/google/adk-python
* https://github.com/google/gemini-python
* https://gemini.google.com/share/6e2d6ffd8647
* https://gemini.google.com/share/d7bff38c84ec
* https://github.com/google/adk-docs
* https://docs.google.com/document/d/1tzei5oAvaRp5HregWCscxb7CL_7IugZYclgGwTGQ0Fs/edit?tab=t.0
