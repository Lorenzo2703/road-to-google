# 🗺️ Detailed 6-Week Preparation Roadmap

> Google Software Engineer, Google Cloud, SRE — Personalized Week-by-Week Plan

---

## Phase 0: Before You Start (Days -3 to -1)

### 🎯 Objective
Set up your environment, assess your current level, and commit to the plan.

### ✅ Required Actions
1. **Self-Assessment**: Take a diagnostic LeetCode contest or solve 5 medium problems to gauge your starting level
2. **Environment Setup**: Install Python 3.10+, Jupyter, set up this repository
3. **Account Setup**: Create/update accounts on LeetCode, NeetCode, and Google Cloud (free tier)
4. **Study Schedule**: Block 3-4 hours daily in your calendar for the next 6 weeks
5. **CV Review**: Read the job description 3 times, highlight keywords, save them

### 📊 Expected Outcome
- Know your baseline (e.g., "I can solve 60% of mediums in 30 min")
- Have a working development environment
- Have a clear daily schedule

### ⚠️ Common Mistakes
- Starting without a clear schedule → you'll lose consistency
- Not reading the job description carefully → you'll prepare for the wrong things
- Trying to do everything at once → burnout in week 2

### 💡 If You Get Stuck
- Can't install something? Use Google Colab as fallback
- Not sure about your level? Start with Week 1 regardless — it's designed to ramp up

---

## Week 1: DSA Foundations (Days 1-7)

### 🎯 Main Objective
Build a rock-solid foundation in the most frequently tested data structures and patterns at Google.

### 📅 Daily Breakdown

| Day | Topic | Key Concepts | LeetCode Problems | Time |
|-----|-------|-------------|-------------------|------|
| 1 | Arrays & Strings | Array traversal, string manipulation, in-place ops | Two Sum, Valid Anagram, Product of Array Except Self | 3-4h |
| 2 | HashMaps & Sets | Hash tables, frequency counting, grouping | Group Anagrams, Top K Frequent Elements, Contains Duplicate | 3-4h |
| 3 | Two Pointers | Sorted arrays, partitioning, converging pointers | 3Sum, Container With Most Water, Trapping Rain Water | 3-4h |
| 4 | Sliding Window | Fixed/variable window, substring problems | Longest Substring Without Repeating Characters, Minimum Window Substring | 3-4h |
| 5 | Stacks & Queues | Monotonic stacks, bracket matching, BFS prep | Valid Parentheses, Daily Temperatures, Evaluate Reverse Polish Notation | 3-4h |
| 6 | Linked Lists | Pointer manipulation, fast/slow pointers, reversal | Reverse Linked List, Merge Two Sorted Lists, Linked List Cycle | 3-4h |
| 7 | Review & Mock | Timed practice, review weak areas | 2 random mediums (45 min each) + review | 3-4h |

### 🧠 Skills to Improve
- Time complexity analysis (Big-O)
- Space complexity optimization
- Pattern recognition for common problem types
- Writing clean, bug-free code under time pressure

---

## Week 2: Intermediate DSA (Days 8-14)

### 🎯 Main Objective
Master intermediate data structures that appear in 60%+ of Google coding interviews.

### 📅 Daily Breakdown

| Day | Topic | Key Concepts | LeetCode Problems | Time |
|-----|-------|-------------|-------------------|------|
| 8 | Binary Search | Classic binary search, search in rotated array | Binary Search, Search in Rotated Sorted Array | 3-4h |
| 9 | Trees Basics | BST operations, DFS traversals, tree properties | Invert Binary Tree, Maximum Depth, Validate BST | 3-4h |
| 10 | Trees Advanced | LCA, serialization, path problems | Lowest Common Ancestor, Binary Tree Level Order Traversal | 3-4h |
| 11 | Heaps & Priority Queues | Min/max heaps, k-th element, merge k lists | Kth Largest Element, Find Median from Data Stream | 3-4h |
| 12 | Recursion & Backtracking | Permutations, combinations, constraint satisfaction | Subsets, Combination Sum, N-Queens | 3-4h |
| 13 | Sorting Algorithms | Merge sort, quick sort, custom comparators | Sort Colors, Merge Intervals, Largest Number | 3-4h |
| 14 | Review & Mock | Full mock interview simulation | 2 mediums + 1 easy (Google-tagged) | 4h |

---

## Week 3: Advanced DSA (Days 15-21)

### 🎯 Main Objective
Tackle the hardest topics that differentiate strong candidates at Google.

### 📅 Daily Breakdown

| Day | Topic | Key Concepts | LeetCode Problems | Time |
|-----|-------|-------------|-------------------|------|
| 15 | Graphs: BFS & DFS | Graph traversal, connected components, cycle detection | Number of Islands, Clone Graph, Course Schedule | 3-4h |
| 16 | Graphs: Shortest Path | Dijkstra, topological sort, union-find | Network Delay Time, Course Schedule II | 3-4h |
| 17 | DP: 1D | Fibonacci-style, house robber, climbing stairs | Climbing Stairs, House Robber, LIS | 3-4h |
| 18 | DP: 2D | Grid problems, string DP, knapsack | Unique Paths, Longest Common Subsequence | 3-4h |
| 19 | Tries & Strings | Trie implementation, prefix matching, KMP | Implement Trie, Word Search II | 3-4h |
| 20 | Greedy Algorithms | Activity selection, interval scheduling | Jump Game, Non-overlapping Intervals | 3-4h |
| 21 | Review & Mock | Hard problem practice + full mock | 1 Hard + 2 Mediums (Google-tagged) timed | 4h |

---

## Week 4: System Design (Days 22-28)

### 🎯 Main Objective
Prepare for the system design interview with focus on massive scale, distributed systems, and Google Cloud.

### 📅 Daily Breakdown

| Day | Topic | Key Concepts | Practice Question | Time |
|-----|-------|-------------|------------------|------|
| 22 | SD Fundamentals | Load balancing, caching, databases, CAP theorem | Design a URL shortener | 3-4h |
| 23 | Distributed Systems | Consistency, partitioning, replication, message queues | Design a distributed task queue | 3-4h |
| 24 | Caching & Load Balancing | Cache invalidation, reverse proxies, consistent hashing | Design a CDN | 4h |
| 25 | Databases & Sharding | Relational vs NoSQL, sharding strategies, Paxos/Raft | Design a global key-value store | 4h |
| 26 | Observability & Monitoring | Logging, tracing, metrics, debugging distributed systems | Design a distributed monitoring system | 3-4h |
| 27 | Cloud Deployment | GCP services, Kubernetes, CI/CD | Design deployment pipeline on GCP | 3-4h |
| 28 | Review & Mock | Full system design mock interview | Design YouTube (45 min) | 4h |

### 🧠 Skills to Improve
- Structuring a system design answer (requirements → high-level → deep dive → trade-offs)
- Discussing trade-offs clearly, emphasizing reliability and fault tolerance (critical for SRE)
- System performance limits and bottlenecks

---

## Week 5: Cloud SRE — Role-Specific (Days 29-35)

### 🎯 Main Objective
Deep-dive into SRE principles, OS internals, networking, and the Google SRE culture.

### 📅 Daily Breakdown

| Day | Topic | Key Concepts | Hands-On Project / Study | Time |
|-----|-------|-------------|-----------------|------|
| 29 | Linux Internals | File systems, I/O, process management, memory | Systems debugging and performance analysis | 4h |
| 30 | Networking | TCP/IP, DNS, HTTP/2, BGP, Load balancing | Debugging network issues (tcpdump, strace) | 4h |
| 31 | SLIs, SLOs, SLAs | Defining reliability targets, error budgets | Draft SLOs for a sample microservice | 4h |
| 32 | Incident Response | Troubleshooting methodology, on-call, postmortems | Write a blameless postmortem for a simulated outage | 4h |
| 33 | Capacity Planning | Queuing theory, load testing, auto-scaling | Perform load testing on a dummy service | 4h |
| 34 | Automation & Toil | Automating operations, infrastructure as code | Write a Terraform/Ansible script for GCP deployment | 4h |
| 35 | Review & Mock | SRE interview scenarios | Practice NALSD (Non-Abstract Large System Design) | 4h |

### 🧠 Skills to Improve
- Treating operations as a software problem.
- Deep troubleshooting from the application layer down to the kernel and network.
- Embracing risk and managing it via error budgets.

---

## Week 6: Behavioral & Final Preparation (Days 36-42)

### 🎯 Main Objective
Polish your behavioral interview skills, complete final mock interviews, and prepare your application.

### 📅 Daily Breakdown

| Day | Topic | Key Concepts | Activity | Time |
|-----|-------|-------------|---------|------|
| 36 | Behavioral Interview Prep | STAR method, story bank, Google values | Write 8-10 STAR stories | 4h |
| 37 | Googleyness & Leadership | Collaboration, ambiguity, impact, learning | Practice behavioral Q&A out loud | 4h |
| 38 | System Design Final | End-to-end system design practice | 2 full system design mocks (45 min each) | 4h |
| 39 | Coding Final (Hard) | Hard problem solving under pressure | Solve 3 Hard LeetCode problems (45 min each) | 4h |
| 40 | Mock Interview — Full | Simulate complete Google interview loop | Coding + System Design + Behavioral (3 rounds) | 5h |
| 41 | Role Fit & Portfolio | Present your SRE mentality | Prepare your "Why Google" and "Why this role" answers | 3h |
| 42 | Final Review & Application | Polish CV, submit application, final checklist | Submit application, review everything | 3h |

---

## 📈 Success Metrics

By the end of this 6-week plan, you should be able to:

| Metric | Target |
|--------|--------|
| LeetCode Easy | Solve in < 10 minutes, 95%+ success rate |
| LeetCode Medium | Solve in < 25 minutes, 75%+ success rate |
| LeetCode Hard | Solve in < 45 minutes, 40%+ success rate |
| System/SRE Design | Complete a design emphasizing reliability in 35 min |
| Behavioral | 8-10 STAR stories, fluent delivery |
| SRE Knowledge | Deep understanding of Linux, Networking, and SRE book concepts |
