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
            "- [ ] Complete all practice problems\n",
            "- [ ] Review optimal solutions and time/space complexities\n"
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
    # WEEK 2
    8: {"title": "Binary Search", "topic": "Week 2 — Intermediate DSA", "theory": "Binary Search is an O(log n) algorithm for finding an element in a sorted array.\n\nKey Templates:\n1. Exact Match: `while left <= right`\n2. Lower Bound: `while left < right`\n\nBe careful with overflow: `mid = left + (right - left) // 2`.", "is_coding": True, "problems": [
        {"name": "Binary Search", "desc": "Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.", "code": "class Solution:\n    def search(self, nums: list[int], target: int) -> int:\n        left, right = 0, len(nums) - 1\n        while left <= right:\n            mid = left + (right - left) // 2\n            if nums[mid] == target:\n                return mid\n            elif nums[mid] < target:\n                left = mid + 1\n            else:\n                right = mid - 1\n        return -1"},
        {"name": "Search in Rotated Sorted Array", "desc": "Search for a target in an array that has been rotated.", "code": "class Solution:\n    def search(self, nums: list[int], target: int) -> int:\n        pass"}
    ]},
    9: {"title": "Trees Basics", "topic": "Week 2 — Intermediate DSA", "theory": "Binary Trees and Binary Search Trees (BST).\n\nTraversals:\n- Inorder: Left, Root, Right (Yields sorted elements in BST)\n- Preorder: Root, Left, Right\n- Postorder: Left, Right, Root\n- Level Order: BFS using a Queue.", "is_coding": True, "problems": [
        {"name": "Maximum Depth of Binary Tree", "desc": "Find the maximum depth of a binary tree.", "code": "class TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\nclass Solution:\n    def maxDepth(self, root: TreeNode) -> int:\n        pass"},
        {"name": "Invert Binary Tree", "desc": "Invert a binary tree (Google classic).", "code": "class Solution:\n    def invertTree(self, root: TreeNode) -> TreeNode:\n        pass"}
    ]},
    10: {"title": "Trees Advanced", "topic": "Week 2 — Intermediate DSA", "theory": "Advanced Tree topics:\n- Lowest Common Ancestor (LCA)\n- Trie (Prefix Tree)\n- Serialization/Deserialization", "is_coding": True, "problems": [
        {"name": "Lowest Common Ancestor of a Binary Tree", "desc": "Find the LCA of two nodes in a binary tree.", "code": "class Solution:\n    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':\n        pass"},
        {"name": "Serialize and Deserialize Binary Tree", "desc": "Design an algorithm to serialize and deserialize a binary tree.", "code": "class Codec:\n    def serialize(self, root):\n        pass\n    def deserialize(self, data):\n        pass"}
    ]},
    11: {"title": "Heaps & Priority Queues", "topic": "Week 2 — Intermediate DSA", "theory": "Heaps are used to keep track of the K largest or smallest elements.\n\nPython `heapq` module:\n- `heapq.heapify(arr)`\n- `heapq.heappush(heap, val)`\n- `heapq.heappop(heap)`\n\nRemember: Python's heapq is a MIN HEAP by default.", "is_coding": True, "problems": [
        {"name": "Kth Largest Element in an Array", "desc": "Find the kth largest element in an unsorted array.", "code": "import heapq\n\nclass Solution:\n    def findKthLargest(self, nums: list[int], k: int) -> int:\n        pass"},
        {"name": "Top K Frequent Elements", "desc": "Given an integer array nums and an integer k, return the k most frequent elements.", "code": "class Solution:\n    def topKFrequent(self, nums: list[int], k: int) -> list[int]:\n        pass"}
    ]},
    12: {"title": "Recursion & Backtracking", "topic": "Week 2 — Intermediate DSA", "theory": "Backtracking is a general algorithm for finding all (or some) solutions to some computational problems, notably constraint satisfaction problems.\n\nTemplate:\n```python\ndef backtrack(path, options):\n    if is_complete(path):\n        results.append(path)\n        return\n    for option in options:\n        if is_valid(option):\n            path.append(option)\n            backtrack(path, updated_options)\n            path.pop()\n```", "is_coding": True, "problems": [
        {"name": "Subsets", "desc": "Given an integer array nums of unique elements, return all possible subsets (the power set).", "code": "class Solution:\n    def subsets(self, nums: list[int]) -> list[list[int]]:\n        pass"},
        {"name": "Word Search", "desc": "Given an m x n grid of characters board and a string word, return true if word exists in the grid.", "code": "class Solution:\n    def exist(self, board: list[list[str]], word: str) -> bool:\n        pass"}
    ]},
    13: {"title": "Sorting Algorithms", "topic": "Week 2 — Intermediate DSA", "theory": "Understand fundamental sorting algorithms:\n- Merge Sort: O(N log N) time, O(N) space. Stable.\n- Quick Sort: O(N log N) average time, O(N^2) worst case. O(log N) space.\n- Counting Sort / Bucket Sort: O(N) time for restricted domain of inputs.", "is_coding": True, "problems": [
        {"name": "Sort Colors", "desc": "Given an array nums with n objects colored red, white, or blue, sort them in-place.", "code": "class Solution:\n    def sortColors(self, nums: list[int]) -> None:\n        pass"},
        {"name": "Merge Intervals", "desc": "Merge all overlapping intervals.", "code": "class Solution:\n    def merge(self, intervals: list[list[int]]) -> list[list[int]]:\n        pass"}
    ]},
    14: {"title": "Review & Mock (Week 2)", "topic": "Week 2 — Intermediate DSA", "theory": "Review week 2 topics: Trees, Heaps, Backtracking, Sorting, Binary Search.\nPerform a 45-minute timed mock interview.", "is_coding": True, "problems": [
        {"name": "Task Scheduler", "desc": "Given a characters array tasks and an integer n, find the least number of units of times that the CPU will take to finish all the given tasks.", "code": "class Solution:\n    def leastInterval(self, tasks: list[str], n: int) -> int:\n        pass"}
    ]},

    # WEEK 3
    15: {"title": "Graphs: BFS & DFS", "topic": "Week 3 — Advanced DSA", "theory": "Graph representations: Adjacency List, Adjacency Matrix.\n\n- DFS is good for exploring paths, finding connected components.\n- BFS is good for finding the shortest path in an unweighted graph.", "is_coding": True, "problems": [
        {"name": "Number of Islands", "desc": "Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.", "code": "class Solution:\n    def numIslands(self, grid: list[list[str]]) -> int:\n        pass"},
        {"name": "Clone Graph", "desc": "Return a deep copy (clone) of a graph.", "code": "class Solution:\n    def cloneGraph(self, node: 'Node') -> 'Node':\n        pass"}
    ]},
    16: {"title": "Graphs: Shortest Path & MST", "topic": "Week 3 — Advanced DSA", "theory": "Shortest Path:\n- Dijkstra's Algorithm (non-negative weights)\n- Bellman-Ford (negative weights)\n\nMST:\n- Prim's Algorithm\n- Kruskal's Algorithm (with Union Find)", "is_coding": True, "problems": [
        {"name": "Network Delay Time", "desc": "Find the time it takes for all nodes to receive a signal (Dijkstra).", "code": "class Solution:\n    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:\n        pass"}
    ]},
    17: {"title": "Dynamic Programming 1D", "topic": "Week 3 — Advanced DSA", "theory": "Dynamic Programming = Recursion + Memoization.\nBreak a problem down into overlapping subproblems.\nIdentify the state variables and the transition function.", "is_coding": True, "problems": [
        {"name": "Climbing Stairs", "desc": "How many distinct ways can you climb to the top?", "code": "class Solution:\n    def climbStairs(self, n: int) -> int:\n        pass"},
        {"name": "Coin Change", "desc": "Return the fewest number of coins that you need to make up that amount.", "code": "class Solution:\n    def coinChange(self, coins: list[int], amount: int) -> int:\n        pass"}
    ]},
    18: {"title": "Dynamic Programming 2D", "topic": "Week 3 — Advanced DSA", "theory": "2D DP problems usually involve a grid or two strings.\nState: `dp[i][j]`.\nCommon patterns: Longest Common Subsequence, Edit Distance, Grid Traversal.", "is_coding": True, "problems": [
        {"name": "Longest Common Subsequence", "desc": "Return the length of their longest common subsequence.", "code": "class Solution:\n    def longestCommonSubsequence(self, text1: str, text2: str) -> int:\n        pass"}
    ]},
    19: {"title": "Tries and Advanced Strings", "topic": "Week 3 — Advanced DSA", "theory": "Trie (Prefix Tree) is an efficient information retrieval data structure.\nO(M) time complexity for search, where M is the key length.", "is_coding": True, "problems": [
        {"name": "Implement Trie (Prefix Tree)", "desc": "Implement the Trie class.", "code": "class Trie:\n    def __init__(self):\n        pass\n    def insert(self, word: str) -> None:\n        pass\n    def search(self, word: str) -> bool:\n        pass\n    def startsWith(self, prefix: str) -> bool:\n        pass"}
    ]},
    20: {"title": "Greedy Algorithms", "topic": "Week 3 — Advanced DSA", "theory": "Greedy algorithms make the locally optimal choice at each stage.\nOften requires sorting or a priority queue.\nHard to prove correctness, but simple to implement.", "is_coding": True, "problems": [
        {"name": "Jump Game", "desc": "Return true if you can reach the last index, or false otherwise.", "code": "class Solution:\n    def canJump(self, nums: list[int]) -> bool:\n        pass"},
        {"name": "Gas Station", "desc": "Return the starting gas station's index if you can travel around the circuit.", "code": "class Solution:\n    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:\n        pass"}
    ]},
    21: {"title": "Review & Mock (Week 3)", "topic": "Week 3 — Advanced DSA", "theory": "Review Week 3 concepts: Graphs, DP, Tries, Greedy.\nPerform a 45-minute timed mock interview.", "is_coding": True, "problems": [
        {"name": "Course Schedule", "desc": "Determine if you can finish all courses (Topological Sort).", "code": "class Solution:\n    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:\n        pass"}
    ]},

    # WEEK 4
    22: {"title": "System Design Fundamentals", "topic": "Week 4 — System Design", "theory": "Key Concepts:\n- Vertical vs Horizontal Scaling\n- CAP Theorem\n- Load Balancing (L4 vs L7)\n- Caching (Memcached, Redis)\n- Database Types (SQL vs NoSQL)\n\nRead the System Design Primer.", "is_coding": False, "problems": [
        {"name": "Design a URL Shortener", "desc": "Discuss API design, database schema, and scaling for a TinyURL service."}
    ]},
    23: {"title": "Designing Distributed Systems", "topic": "Week 4 — System Design", "theory": "Key Concepts:\n- Sharding and Partitioning\n- Replication (Master-Slave, Master-Master)\n- Consistent Hashing\n- Message Queues (Kafka, RabbitMQ)", "is_coding": False, "problems": [
        {"name": "Design a Distributed Key-Value Store", "desc": "Discuss consistent hashing, replication, and handling node failures."}
    ]},
    24: {"title": "Designing an Agent Orchestrator", "topic": "Week 4 — System Design", "theory": "Role Specific: Agent Orchestrator.\nHow do you manage long-running LLM agent tasks?\n- Use async workers (Celery, Temporal)\n- State management (saving intermediate agent scratchpads)\n- Handling API rate limits and retries", "is_coding": False, "problems": [
        {"name": "Design an Agent Task Queue", "desc": "Design a system that accepts complex prompts, spins up agents to fulfill them, and streams back the results."}
    ]},
    25: {"title": "Designing an SDK Platform", "topic": "Week 4 — System Design", "theory": "Role Specific: SDK Design.\nWhen building an SDK like Google ADK:\n- Consistent interfaces across languages (Python, TS)\n- Versioning and backward compatibility\n- Extensibility (plugin architecture)", "is_coding": False, "problems": [
        {"name": "Design the Agent Development Kit (ADK) API", "desc": "Draft the public API for an SDK that allows developers to define tools, memory, and LLM providers for an agent."}
    ]},
    26: {"title": "Observability & Monitoring", "topic": "Week 4 — System Design", "theory": "The 3 Pillars of Observability:\n1. Logs\n2. Metrics\n3. Traces\n\nFor LLMs/Agents, tracing is critical to see the 'thought process' (e.g., LangSmith, Arize).", "is_coding": False, "problems": [
        {"name": "Design a Tracing System for LLM Agents", "desc": "How do you collect and visualize the multi-step reasoning of thousands of concurrent agents?"}
    ]},
    27: {"title": "Cloud Deployment Patterns", "topic": "Week 4 — System Design", "theory": "Deploying on GCP/AWS:\n- Docker and Kubernetes\n- Serverless (Cloud Run, Lambda)\n- CI/CD Pipelines\n- Blue/Green and Canary Deployments", "is_coding": False, "problems": [
        {"name": "Deploying an Agent Application", "desc": "Discuss the architecture for deploying a scalable, highly available agent API on Google Cloud Platform."}
    ]},
    28: {"title": "Review & Mock (Week 4)", "topic": "Week 4 — System Design", "theory": "Review System Design concepts. Do a full 45-minute mock system design interview.", "is_coding": False, "problems": [
        {"name": "Mock SD Interview: Design a Chat Application", "desc": "Design WhatsApp or Google Chat, focusing on real-time messaging and agent integration (e.g., a chatbot participant)."}
    ]},

    # WEEK 5
    29: {"title": "LLM Fundamentals", "topic": "Week 5 — Agent Development", "theory": "Role Specific: LLMs.\n- Tokenization\n- Context Windows\n- Generation Parameters (Temperature, Top-P, Top-K)\n- Embeddings and Vector Databases", "is_coding": True, "problems": [
        {"name": "Simple Token Counting", "desc": "Write a mock function to estimate token count.", "code": "def estimate_tokens(text: str) -> int:\n    # Approx 4 characters per token\n    return len(text) // 4"}
    ]},
    30: {"title": "Agent Architectures", "topic": "Week 5 — Agent Development", "theory": "Role Specific: Agents.\n- ReAct (Reason + Act)\n- Plan and Execute\n- Reflexion / Self-Correction\n- Agent Memory (Short-term/Context vs Long-term/RAG)", "is_coding": True, "problems": [
        {"name": "Implement a simple ReAct loop", "desc": "Write a mock loop that alternates between thinking and acting.", "code": "def react_loop(prompt: str, max_steps=5):\n    for step in range(max_steps):\n        # 1. Generate Thought\n        # 2. Generate Action\n        # 3. Execute Action & Get Observation\n        pass"}
    ]},
    31: {"title": "Google ADK Deep Dive", "topic": "Week 5 — Agent Development", "theory": "Google Agent Development Kit (ADK) concepts:\n- Core abstractions\n- Integration with Gemini models\n- How it differs from LangChain/LlamaIndex\nRead the open-source repository documentation.", "is_coding": True, "problems": [
        {"name": "ADK Boilerplate", "desc": "Write a script that initializes an agent using the ADK format.", "code": "# Pseudocode for ADK agent\nimport google.generativeai as genai\n\ndef create_agent():\n    pass"}
    ]},
    32: {"title": "Tool Use & Function Calling", "topic": "Week 5 — Agent Development", "theory": "Function Calling (Tool Use) allows LLMs to output structured JSON to execute code.\nKey challenge: Writing deterministic schemas for stochastic models.", "is_coding": True, "problems": [
        {"name": "Define a JSON Schema for a Tool", "desc": "Write a JSON schema representing a tool that fetches weather.", "code": "weather_tool_schema = {\n    \"name\": \"get_weather\",\n    \"description\": \"Get the current weather in a location\",\n    \"parameters\": {\n        # Add schema here\n    }\n}"}
    ]},
    33: {"title": "Testing & Debugging Agents", "topic": "Week 5 — Agent Development", "theory": "Testing non-deterministic systems:\n- Evaluating output quality (LLM-as-a-judge)\n- Asserting structural constraints (JSON output)\n- Unit testing tools independently of the LLM", "is_coding": True, "problems": [
        {"name": "Mock LLM-as-a-judge", "desc": "Write a function that compares an agent's output against a rubric.", "code": "def evaluate_output(output: str, rubric: str) -> bool:\n    pass"}
    ]},
    34: {"title": "Agent Deployment & Observability", "topic": "Week 5 — Agent Development", "theory": "Managing agents in production:\n- Cost tracking per token\n- Latency optimization\n- Handling context window exhaustion", "is_coding": True, "problems": [
        {"name": "Cost Estimator", "desc": "Calculate the cost of an agent trajectory.", "code": "def calculate_cost(prompt_tokens: int, completion_tokens: int) -> float:\n    # Assume $0.50 per 1M prompt, $1.50 per 1M completion\n    pass"}
    ]},
    35: {"title": "Review & Mock (Week 5)", "topic": "Week 5 — Agent Development", "theory": "Review Week 5 concepts: Agents, LLMs, Tool Use, ADK.\nPractice answering domain-specific interview questions.", "is_coding": True, "problems": [
        {"name": "Build a Calculator Agent", "desc": "Implement a simple agent that can add, subtract, multiply, and divide using tools.", "code": "class CalculatorAgent:\n    def __init__(self):\n        pass\n    def run(self, query: str):\n        pass"}
    ]},

    # WEEK 6
    36: {"title": "Behavioral Interview Prep", "topic": "Week 6 — Behavioral & Final", "theory": "The STAR Method:\n- Situation: Set the scene\n- Task: What was the goal or problem?\n- Action: What did YOU do?\n- Result: What was the outcome? (Metrics matter)", "is_coding": False, "problems": [
        {"name": "Draft 3 STAR Stories", "desc": "1. A time you solved a complex technical problem.\n2. A time you had a conflict with a coworker.\n3. A time you had to learn a new technology quickly."}
    ]},
    37: {"title": "Googleyness & Leadership", "topic": "Week 6 — Behavioral & Final", "theory": "Googleyness principles:\n- Thriving in ambiguity\n- Valuing feedback\n- Challenging the status quo safely\n- Putting the user first\n- Doing the right thing", "is_coding": False, "problems": [
        {"name": "Scenario Question", "desc": "How would you handle a situation where a core dependency (like a model API) goes down, and you have an upcoming release?"}
    ]},
    38: {"title": "System Design Final Mock", "topic": "Week 6 — Behavioral & Final", "theory": "Final System Design Polish. Focus on communicating trade-offs clearly and driving the discussion.", "is_coding": False, "problems": [
        {"name": "Design Google Drive", "desc": "Focus on file chunking, sync conflict resolution, and metadata storage."}
    ]},
    39: {"title": "Coding Final (Hard)", "topic": "Week 6 — Behavioral & Final", "theory": "Tackling Leetcode Hard problems. Don't panic, break it down, talk out loud.", "is_coding": True, "problems": [
        {"name": "Word Search II", "desc": "Given an m x n board of characters and a list of strings words, return all words on the board.", "code": "class Solution:\n    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:\n        pass"}
    ]},
    40: {"title": "Mock Interview Full", "topic": "Week 6 — Behavioral & Final", "theory": "Simulate a full Google onsite loop:\n1. Coding (45m)\n2. Coding (45m)\n3. System Design (45m)\n4. Behavioral / Leadership (45m)", "is_coding": False, "problems": [
        {"name": "Execute Mock Loop", "desc": "Find a friend or use an AI interviewer to do a full 4-hour simulation."}
    ]},
    41: {"title": "Role Fit & Portfolio", "topic": "Week 6 — Behavioral & Final", "theory": "Prepare your narrative for the 'Agent Development' role. Why you? Why this team?\nHighlight your open-source contributions, SDK experience, and LLM projects.", "is_coding": False, "problems": [
        {"name": "Elevator Pitch", "desc": "Draft a 2-minute introduction that perfectly aligns your background with the ADK team."}
    ]},
    42: {"title": "Final Review & Application", "topic": "Week 6 — Behavioral & Final", "theory": "Final review of your cheat sheets. Rest well before the interview.\nEnsure your resume matches the target job description perfectly.", "is_coding": False, "problems": [
        {"name": "Checklist Completion", "desc": "Verify all items in CHECKLIST.md are marked as done."}
    ]}
}

def main():
    paths = {
        8: 'week-02-intermediate-dsa/day-08-binary-search.ipynb',
        9: 'week-02-intermediate-dsa/day-09-trees-basics.ipynb',
        10: 'week-02-intermediate-dsa/day-10-trees-advanced.ipynb',
        11: 'week-02-intermediate-dsa/day-11-heaps-priority-queues.ipynb',
        12: 'week-02-intermediate-dsa/day-12-recursion-backtracking.ipynb',
        13: 'week-02-intermediate-dsa/day-13-sorting-algorithms.ipynb',
        14: 'week-02-intermediate-dsa/day-14-review-and-mock.ipynb',
        15: 'week-03-advanced-dsa/day-15-graphs-bfs-dfs.ipynb',
        16: 'week-03-advanced-dsa/day-16-graphs-shortest-path.ipynb',
        17: 'week-03-advanced-dsa/day-17-dynamic-programming-1d.ipynb',
        18: 'week-03-advanced-dsa/day-18-dynamic-programming-2d.ipynb',
        19: 'week-03-advanced-dsa/day-19-tries-and-advanced-strings.ipynb',
        20: 'week-03-advanced-dsa/day-20-greedy-algorithms.ipynb',
        21: 'week-03-advanced-dsa/day-21-review-and-mock.ipynb',
        22: 'week-04-system-design/day-22-system-design-fundamentals.ipynb',
        23: 'week-04-system-design/day-23-designing-distributed-systems.ipynb',
        24: 'week-04-system-design/day-24-designing-an-agent-orchestrator.ipynb',
        25: 'week-04-system-design/day-25-designing-an-sdk-platform.ipynb',
        26: 'week-04-system-design/day-26-observability-and-monitoring.ipynb',
        27: 'week-04-system-design/day-27-cloud-deployment-patterns.ipynb',
        28: 'week-04-system-design/day-28-review-and-mock.ipynb',
        29: 'week-05-agent-development/day-29-llm-fundamentals.ipynb',
        30: 'week-05-agent-development/day-30-agent-architectures.ipynb',
        31: 'week-05-agent-development/day-31-google-adk-deep-dive.ipynb',
        32: 'week-05-agent-development/day-32-tool-use-and-function-calling.ipynb',
        33: 'week-05-agent-development/day-33-testing-debugging-agents.ipynb',
        34: 'week-05-agent-development/day-34-agent-deployment-observability.ipynb',
        35: 'week-05-agent-development/day-35-review-and-mock.ipynb',
        36: 'week-06-behavioral-and-final/day-36-behavioral-interview-prep.ipynb',
        37: 'week-06-behavioral-and-final/day-37-googleyness-and-leadership.ipynb',
        38: 'week-06-behavioral-and-final/day-38-system-design-final.ipynb',
        39: 'week-06-behavioral-and-final/day-39-coding-final-hard.ipynb',
        40: 'week-06-behavioral-and-final/day-40-mock-interview-full.ipynb',
        41: 'week-06-behavioral-and-final/day-41-role-fit-and-portfolio.ipynb',
        42: 'week-06-behavioral-and-final/day-42-final-review-and-application.ipynb',
    }

    for day, info in DATA.items():
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
