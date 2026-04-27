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
                "## 📚 Theory: Networking Mastery\n",
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
            f"## 📝 Day {day} Mastery Checklist\n",
            "\n",
            "- [ ] Explain why a 3nd-way handshake is necessary for reliability.\n",
            "- [ ] Describe the impact of TCP Window Scaling on high-latency links.\n",
            "- [ ] Debug a 'Connection Refused' vs a 'Connection Timeout'.\n",
            "- [ ] Explain the role of Anycast in Google's Global Load Balancer.\n"
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

# --- Day 30 CONTENT ---
DAY_30_THEORY = """
### 1. The TCP State Machine
Understanding the transition between states is key to debugging:
- **SYN_SENT**: Waiting for SYN-ACK. (Check firewall/routing if stuck here).
- **ESTABLISHED**: Connection ready.
- **FIN_WAIT**: Process finished, waiting for remote to close.
- **TIME_WAIT**: Connection closed, but port held for 2MSL to catch stray packets. (High churn problem).

### 2. TCP Congestion Control
How does TCP know how fast to send?
- **Slow Start**: Start small, double window size every RTT.
- **Packet Loss**: Traditionally seen as congestion (Cubic/Reno).
- **BBR (Bottleneck Bandwidth and RTT)**: Google's algorithm that uses model-based congestion control instead of loss-based. Results in much higher throughput on lossy links.

### 3. DNS & GSLB
- **Recursive Resolvers**: The 'middlemen' (e.g., 8.8.8.8).
- **Edns-client-subnet (ECS)**: Allows resolvers to pass the user's subnet to the Authoritative server.
- **Global Server Load Balancing (GSLB)**: Authoritative DNS servers return different IPs based on the ECS, directing users to the closest Google Front End (GFE).

### 4. MTU and Fragmentation
- **MTU (Maximum Transmission Unit)**: Usually 1500 bytes for Ethernet.
- **Fragmentation**: When a packet is too large for a hop. In IPv6, routers don't fragment; they send a 'Packet Too Big' ICMP message back.
- **Path MTU Discovery (PMTUD)**: How hosts find the smallest MTU along a path.
"""

DAY_30_PROBLEMS = [
    {
        "name": "TCP Header Parser",
        "desc": "Write a mock function that extracts the Source Port, Destination Port, and Flags from a hex string representing a TCP header.",
        "code": """def parse_tcp_header(hex_header):
    # TCP header is 20 bytes min
    # Source port: first 2 bytes
    # Dest port: next 2 bytes
    src_port = int(hex_header[0:4], 16)
    dst_port = int(hex_header[4:8], 16)
    # Flags are in the 14th byte (offset 26-28 in hex string)
    flags = int(hex_header[26:28], 16)
    return {
        "src_port": src_port,
        "dst_port": dst_port,
        "flags": bin(flags)
    }

# Example TCP header hex (simplified)
example = "0db501bb3a2e73f00000000050027210"
print(parse_tcp_header(example))"""
    },
    {
        "name": "BGP Route Selection",
        "desc": "If two BGP paths have the same AS-Path length, what is the next tie-breaker in the decision process? (Hint: It's often Local Preference or Origin).",
        "code": "# Discussion: 1. Weight, 2. Local Pref, 3. Self-Originated, 4. AS-Path, 5. Origin, 6. MED..."
    }
]

if __name__ == '__main__':
    create_notebook(
        path='week-05-cloud-sre/day-30-networking-fundamentals.ipynb',
        title="Networking: Protocols & Routing",
        day=30,
        topic="Week 5 — Cloud SRE",
        theory_md=DAY_30_THEORY,
        problems=DAY_30_PROBLEMS
    )
    print("Regenerated Day 30 with extreme detail.")
