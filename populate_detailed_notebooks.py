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
                "## 📚 Theory\n",
                "\n"
            ] + [line + "\n" for line in theory_md.split("\n")]
        }
    ]
    
    if is_coding and problems:
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 🔨 Practice Problems\n"]
        })
        for i, prob in enumerate(problems, 1):
            cells.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"### Problem {i}: {prob['name']}\n", "\n"] + [line + "\n" for line in prob.get('desc', '').split('\n')]
            })
            cells.append({
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [line + "\n" for line in prob.get('code', 'def solve():\n    pass').split('\n')]
            })
    elif not is_coding and problems:
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 🧠 Exercises / Discussion\n"]
        })
        for i, prob in enumerate(problems, 1):
            cells.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"### {prob['name']}\n", "\n"] + [line + "\n" for line in prob.get('desc', '').split('\n')]
            })

    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            f"## 📝 Day {day} Review\n",
            "\n",
            "- [ ] Understand the core concepts of today's theory\n",
            "- [ ] Complete all practice problems/exercises\n",
            "- [ ] Review optimal solutions and trade-offs\n"
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

DATA = {
    # WEEK 5 — CLOUD SRE DEEP DIVE
    29: {
        "title": "Linux Internals for SREs",
        "topic": "Week 5 — Cloud SRE",
        "theory": (
            "An SRE must understand the operating system to debug performance and reliability issues.\n\n"
            "### 1. The Kernel & System Calls\n"
            "- The Kernel manages hardware. Applications interact with it via **System Calls** (syscalls).\n"
            "- **strace**: A critical tool for tracing syscalls (e.g., `open`, `read`, `write`, `fork`, `execve`).\n"
            "- **Signals**: Inter-process communication (e.g., `SIGTERM` for graceful shutdown, `SIGKILL` for immediate stop).\n\n"
            "### 2. Processes vs. Threads\n"
            "- **Process**: Independent execution unit with its own memory space.\n"
            "- **Thread**: Lightweight unit within a process, sharing memory space. Understanding the GIL in Python.\n"
            "- **Context Switching**: The overhead of moving from one process/thread to another.\n\n"
            "### 3. Memory & The OOM Killer\n"
            "- **Virtual Memory**: How Linux maps application memory to physical RAM.\n"
            "- **OOM (Out of Memory) Killer**: When memory is exhausted, the kernel kills processes based on an `oom_score`.\n\n"
            "### 4. The /proc File System\n"
            "- A virtual file system reflecting the kernel's state. `cat /proc/loadavg`, `cat /proc/meminfo`."
        ),
        "is_coding": True,
        "problems": [
            {
                "name": "Analyze System Load",
                "desc": "Write a script that reads `/proc/loadavg` and alerts if the 1-minute load average exceeds the number of CPU cores.",
                "code": (
                    "import os\n"
                    "def check_load():\n"
                    "    num_cores = os.cpu_count()\n"
                    "    with open('/proc/loadavg', 'r') as f:\n"
                    "        load_1min = float(f.read().split()[0])\n"
                    "    \n"
                    "    if load_1min > num_cores:\n"
                    "        print(f'CRITICAL: Load ({load_1min}) exceeds core count ({num_cores})')\n"
                    "    else:\n"
                    "        print(f'OK: Load is {load_1min}')\n"
                    "\n"
                    "check_load()"
                )
            },
            {
                "name": "Identify Memory Leaks",
                "desc": "How would you use `top` and `pmap` to determine if a process has a memory leak?",
                "code": "# Discussion: Look for RSS (Resident Set Size) growing continuously over time."
            }
        ]
    },
    30: {
        "title": "Networking Fundamentals",
        "topic": "Week 5 — Cloud SRE",
        "theory": (
            "Reliability often depends on the network between services.\n\n"
            "### 1. TCP/IP Deep Dive\n"
            "- **Three-Way Handshake**: SYN, SYN-ACK, ACK. Understanding the impact on latency.\n"
            "- **Congestion Control**: How TCP manages bandwidth (Slow Start, Congestion Avoidance).\n"
            "- **TIME_WAIT**: Why high-traffic servers run out of ephemeral ports.\n\n"
            "### 2. DNS (The Hidden Failure Point)\n"
            "- Recursive vs. Iterative lookups.\n"
            "- TTL (Time to Live) and its role in regional failover. Why low TTL is good for SRE, but bad for latency.\n\n"
            "### 3. Load Balancing (L4 vs L7)\n"
            "- **L4 (Transport)**: Fast, routes based on IP/Port. No awareness of application data.\n"
            "- **L7 (Application)**: Slower, but can route based on headers, cookies, or URL paths (Critical for Canary releases)."
        ),
        "is_coding": True,
        "problems": [
            {
                "name": "DNS Health Checker",
                "desc": "Write a script that verifies if a list of domains resolves to a specific IP range (e.g., your VIPs).",
                "code": (
                    "import socket\n"
                    "def verify_dns(domain, expected_prefix):\n"
                    "    try:\n"
                    "        ip = socket.gethostbyname(domain)\n"
                    "        return ip.startswith(expected_prefix)\n"
                    "    except socket.gaierror:\n"
                    "        return False"
                )
            },
            {
                "name": "HTTP Latency Analyzer",
                "desc": "Use `requests` to measure the time taken for 'Time to First Byte' (TTFB) vs 'Total Time'.",
                "code": (
                    "import requests\n"
                    "import time\n"
                    "def measure_latency(url):\n"
                    "    start = time.time()\n"
                    "    r = requests.get(url)\n"
                    "    total_time = time.time() - start\n"
                    "    print(f'Total Time: {total_time:.4f}s')\n"
                    "    print(f'Status: {r.status_code}')"
                )
            }
        ]
    },
    31: {
        "title": "SLIs, SLOs, and SLAs",
        "topic": "Week 5 — Cloud SRE",
        "theory": (
            "If you can't measure it, you can't improve it.\n\n"
            "### 1. Definitions\n"
            "- **SLI (Indicator)**: A quantitative measure (e.g., % of 200 OK responses).\n"
            "- **SLO (Objective)**: A target value for an SLI (e.g., 99.9% success rate).\n"
            "- **SLA (Agreement)**: A legal contract with consequences (usually money) for missing an SLO.\n\n"
            "### 2. Error Budgets\n"
            "- The budget for unreliability. `Budget = 1 - SLO`.\n"
            "- **Burn Rate**: How fast you are consuming your error budget. A burn rate of 1 means you'll hit exactly 0 budget at the end of the window.\n\n"
            "### 3. Choosing the right SLIs\n"
            "- Request-driven: Availability, Latency, Quality.\n"
            "- Storage: Durability, Availability, Latency.\n"
            "- Pipeline: Throughput, Freshness."
        ),
        "is_coding": False,
        "problems": [
            {
                "name": "Calculate the Error Budget",
                "desc": "For a service with 10 million requests per month and a 99.9% availability SLO, how many failed requests are allowed before the budget is exhausted?"
            },
            {
                "name": "SLO Burn Rate Alerting",
                "desc": "If you lose 5% of your 30-day error budget in 1 hour, what is your burn rate? Should you alert a human or just log it?"
            }
        ]
    },
    32: {
        "title": "Incident Response & Postmortems",
        "topic": "Week 5 — Cloud SRE",
        "theory": (
            "Failure is inevitable; how you handle it defines an SRE.\n\n"
            "### 1. Incident Lifecycle\n"
            "1. **Detection**: Monitoring alerts a human.\n"
            "2. **Triage**: Is it global? Is it just one customer?\n"
            "3. **Mitigation**: Stop the bleeding (Rollback, Scale up, Load shed).\n"
            "4. **Resolution**: Fix the root cause.\n\n"
            "### 2. Roles in an Incident\n"
            "- **Incident Commander (IC)**: In charge of the response. Does not fix code.\n"
            "- **Operations Lead**: Hands on the keyboard.\n"
            "- **Communications Lead**: Updates stakeholders/users.\n\n"
            "### 3. Blameless Postmortems\n"
            "- Focus on *how* the system failed, not *who* failed it.\n"
            "- Identify 'Action Items' (P0/P1) to prevent recurrence."
        ),
        "is_coding": False,
        "problems": [
            {
                "name": "Scenario: The 500 Spike",
                "desc": "At 2:00 PM, your checkout service spikes from 0.01% to 15% error rate. You just pushed a new release. What is your first action?"
            },
            {
                "name": "Drafting a Postmortem",
                "desc": "What are the 5 essential sections of a Google-style blameless postmortem?"
            }
        ]
    },
    33: {
        "title": "Capacity Planning & Efficiency",
        "topic": "Week 5 — Cloud SRE",
        "theory": (
            "Ensuring you have enough resources without wasting money.\n\n"
            "### 1. Utilization vs. Saturation\n"
            "- **Utilization**: The percentage of a resource being used (e.g., 70% CPU).\n"
            "- **Saturation**: The point at which requests start queueing (The 'Knee' of the curve).\n\n"
            "### 2. Little's Law\n"
            "- `L = λW` (Items in system = Arrival rate * Time spent in system).\n"
            "- Helps estimate how many concurrent requests a server can handle before latency spikes.\n\n"
            "### 3. Load Testing\n"
            "- **Stress Testing**: Find the point where the system breaks.\n"
            "- **Soak Testing**: Find memory leaks or resource exhaustion over long periods."
        ),
        "is_coding": True,
        "problems": [
            {
                "name": "Calculate Concurrency Limits",
                "desc": "If a server handles 500 requests/sec and each request takes 200ms on average, how many concurrent requests are active on average?",
                "code": "def littles_law(arrival_rate, avg_time):\n    return arrival_rate * avg_time\n\nprint(f'Average active requests: {littles_law(500, 0.2)}')"
            },
            {
                "name": "Predicting Scale",
                "desc": "Your traffic grows 10% month-over-month. You are currently at 60% CPU utilization. In how many months will you hit 90%?"
            }
        ]
    },
    34: {
        "title": "Automation & Eliminating Toil",
        "topic": "Week 5 — Cloud SRE",
        "theory": (
            "SREs hate doing the same thing twice.\n\n"
            "### 1. Defining Toil\n"
            "- Manual, repetitive, automatable, tactical work that scales with the service size.\n"
            "- SRE goal: Keep toil < 50% of your time.\n\n"
            "### 2. Infrastructure as Code (IaC)\n"
            "- **Terraform**: Declarative infrastructure management. 'Describe the end state'.\n"
            "- **Ansible/Puppet**: Configuration management.\n\n"
            "### 3. GitOps\n"
            "- Using Git as the 'Source of Truth' for both code and infrastructure. Merge requests trigger deployments."
        ),
        "is_coding": True,
        "problems": [
            {
                "name": "Automated Log Rotation Script",
                "desc": "Write a script that finds files in a directory ending in `.log`, compresses them if they are > 100MB, and deletes them if they are older than 30 days.",
                "code": (
                    "import os\n"
                    "import time\n"
                    "import gzip\n\n"
                    "def cleanup_toil(log_dir):\n"
                    "    now = time.time()\n"
                    "    for filename in os.listdir(log_dir):\n"
                    "        if not filename.endswith('.log'): continue\n"
                    "        path = os.path.join(log_dir, filename)\n"
                    "        \n"
                    "        # Delete if > 30 days\n"
                    "        if os.stat(path).st_mtime < now - (30 * 86400):\n"
                    "            os.remove(path)\n"
                    "            continue\n"
                    "            \n"
                    "        # Compress if > 100MB\n"
                    "        if os.path.getsize(path) > 100 * 1024 * 1024:\n"
                    "            with open(path, 'rb') as f_in:\n"
                    "                with gzip.open(path + '.gz', 'wb') as f_out:\n"
                    "                    f_out.writelines(f_in)\n"
                    "            os.remove(path)"
                )
            }
        ]
    },
    35: {
        "title": "Review & SRE Mock Interview",
        "topic": "Week 5 — Cloud SRE",
        "theory": (
            "Final review of systems fundamentals and SRE principles.\n\n"
            "### Focus Areas:\n"
            "1. **Troubleshooting**: 'The service is slow, what do you check?'\n"
            "2. **Design**: 'Design a system that can lose a whole datacenter without downtime.'\n"
            "3. **SRE Philosophy**: 'Why do we want a non-zero error budget?'"
        ),
        "is_coding": False,
        "problems": [
            {
                "name": "Mock Scenario: The Slow DB",
                "desc": "Your P99 latency is spiking from 200ms to 5s. CPU on the DB is low, but disk I/O is high. What is your hypothesis?"
            },
            {
                "name": "SRE Culture Question",
                "desc": "A developer team wants to bypass the SLO check to launch a feature. As their SRE, how do you handle this?"
            }
        ]
    }
}

# Ensure all days from 1 to 42 are covered in paths
def main():
    # Simplified paths for this example, focusing on the ones we updated
    paths = {
        29: 'week-05-cloud-sre/day-29-linux-internals.ipynb',
        30: 'week-05-cloud-sre/day-30-networking-fundamentals.ipynb',
        31: 'week-05-cloud-sre/day-31-slis-slos-slas.ipynb',
        32: 'week-05-cloud-sre/day-32-incident-response.ipynb',
        33: 'week-05-cloud-sre/day-33-capacity-planning.ipynb',
        34: 'week-05-cloud-sre/day-34-automation-and-toil.ipynb',
        35: 'week-05-cloud-sre/day-35-review-and-mock.ipynb',
    }

    # Add back the other weeks to DATA if not present to avoid errors if the script runs for all
    # (In a real scenario, we'd have the full DATA dictionary)
    
    for day, info in DATA.items():
        if day in paths:
            create_notebook(
                path=paths[day],
                title=info['title'],
                day=day,
                topic=info['topic'],
                theory_md=info['theory'],
                problems=info['problems'],
                is_coding=info.get('is_coding', True)
            )
            print(f"Generated {paths[day]}")

if __name__ == '__main__':
    main()
