# 🗺️ Detailed 6-Week Preparation Roadmap

> Google SWE II, Agent Development — Personalized Week-by-Week Plan

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

### 📊 Expected Outcomes
- Solve Easy problems in < 10 minutes
- Solve Medium problems in < 25 minutes
- Identify problem patterns within 2 minutes of reading

### ⚠️ Common Mistakes
- Jumping to code without thinking through the approach
- Not considering edge cases (empty arrays, single element, duplicates)
- Memorizing solutions instead of understanding patterns
- Spending > 45 minutes on a single problem without looking at hints

### 💡 Practical Advice
- **Before coding**: Verbalize your approach, write pseudocode
- **After solving**: Review the optimal solution, note the pattern
- **If stuck > 20 min**: Look at hints, not the full solution
- **Track patterns**: Keep a note of which pattern each problem uses

### 🔧 If You Get Stuck
- Can't solve a Medium? Try the Easy version of the same pattern first
- Don't understand a pattern? Watch NeetCode's video explanation
- Feeling slow? Speed comes with practice — focus on correctness first

---

## Week 2: Intermediate DSA (Days 8-14)

### 🎯 Main Objective
Master intermediate data structures that appear in 60%+ of Google coding interviews.

### 📅 Daily Breakdown

| Day | Topic | Key Concepts | LeetCode Problems | Time |
|-----|-------|-------------|-------------------|------|
| 8 | Binary Search | Classic binary search, search in rotated array, search space | Binary Search, Search in Rotated Sorted Array, Koko Eating Bananas | 3-4h |
| 9 | Trees Basics | BST operations, DFS traversals, tree properties | Invert Binary Tree, Maximum Depth, Validate BST | 3-4h |
| 10 | Trees Advanced | LCA, serialization, path problems | Lowest Common Ancestor, Binary Tree Level Order Traversal, Path Sum III | 3-4h |
| 11 | Heaps & Priority Queues | Min/max heaps, k-th element, merge k lists | Kth Largest Element, Merge K Sorted Lists, Find Median from Data Stream | 3-4h |
| 12 | Recursion & Backtracking | Permutations, combinations, constraint satisfaction | Subsets, Combination Sum, N-Queens | 3-4h |
| 13 | Sorting Algorithms | Merge sort, quick sort, custom comparators | Sort Colors, Merge Intervals, Largest Number | 3-4h |
| 14 | Review & Mock | Full mock interview simulation | 2 mediums + 1 easy (Google-tagged) in 45 min each | 4h |

### 🧠 Skills to Improve
- Recursive thinking and tree traversal fluency
- Heap operations and when to use them
- Binary search on answer (search space reduction)
- Sorting as a preprocessing step

### 📊 Expected Outcomes
- Solve tree problems confidently
- Apply binary search to non-obvious problems
- Handle backtracking without getting lost in recursion

### ⚠️ Common Mistakes
- Off-by-one errors in binary search (use templates!)
- Not considering null nodes in tree problems
- Forgetting to sort before applying two-pointer/binary search
- Inefficient backtracking (not pruning early)

### 💡 Practical Advice
- **Binary Search**: Always use the template `lo, hi = 0, len-1` with `while lo <= hi`
- **Trees**: Draw the tree before coding. Trace through with examples
- **Backtracking**: Draw the decision tree, understand what to add/remove

### 🔧 If You Get Stuck
- Trees confusing? Practice 5 basic DFS/BFS problems before advancing
- Binary search off-by-one? Use NeetCode's binary search template
- Backtracking overwhelming? Start with Subsets (simplest backtracking problem)

---

## Week 3: Advanced DSA (Days 15-21)

### 🎯 Main Objective
Tackle the hardest topics that differentiate strong candidates at Google L4.

### 📅 Daily Breakdown

| Day | Topic | Key Concepts | LeetCode Problems | Time |
|-----|-------|-------------|-------------------|------|
| 15 | Graphs: BFS & DFS | Graph traversal, connected components, cycle detection | Number of Islands, Clone Graph, Course Schedule | 3-4h |
| 16 | Graphs: Shortest Path | Dijkstra, topological sort, union-find | Network Delay Time, Course Schedule II, Redundant Connection | 3-4h |
| 17 | DP: 1D | Fibonacci-style, house robber, climbing stairs | Climbing Stairs, House Robber, Longest Increasing Subsequence | 3-4h |
| 18 | DP: 2D | Grid problems, string DP, knapsack | Unique Paths, Longest Common Subsequence, Coin Change | 3-4h |
| 19 | Tries & Strings | Trie implementation, prefix matching, KMP | Implement Trie, Word Search II, Longest Common Prefix | 3-4h |
| 20 | Greedy Algorithms | Activity selection, interval scheduling, optimal choices | Jump Game, Non-overlapping Intervals, Task Scheduler | 3-4h |
| 21 | Review & Mock | Hard problem practice + full mock | 1 Hard + 2 Mediums (Google-tagged) timed | 4h |

### 🧠 Skills to Improve
- Graph modeling (converting real problems to graph problems)
- DP state definition and transition
- Greedy proof of correctness
- Trie efficiency for prefix-based operations

### 📊 Expected Outcomes
- Model and solve graph problems fluently
- Define DP states and transitions for medium problems
- Know when greedy works vs. when you need DP
- Implement a Trie from scratch in < 10 minutes

### ⚠️ Common Mistakes
- Not building the adjacency list correctly in graph problems
- Wrong DP state definition (leads to incorrect transitions)
- Assuming greedy works without proving it
- Using brute force for string problems that need Trie

### 💡 Practical Advice
- **Graphs**: Always clarify: directed vs undirected, weighted vs unweighted, cycles allowed?
- **DP**: Start with recursion + memoization, then convert to bottom-up if needed
- **Greedy**: If you can't prove it's optimal, it probably isn't — use DP instead
- **Tries**: Practice implementing from scratch until it's second nature

### 🔧 If You Get Stuck
- Graphs: Use BFS for shortest path (unweighted), DFS for connected components
- DP: If you can't define the state, try `dp[i] = best answer considering first i elements`
- Ask: "What subproblems do I need to solve?" → that's your DP definition

---

## Week 4: System Design (Days 22-28)

### 🎯 Main Objective
Prepare for the system design interview with focus on agent-related architectures and Google Cloud.

### 📅 Daily Breakdown

| Day | Topic | Key Concepts | Practice Question | Time |
|-----|-------|-------------|------------------|------|
| 22 | SD Fundamentals | Load balancing, caching, databases, CAP theorem | Design a URL shortener | 3-4h |
| 23 | Distributed Systems | Consistency, partitioning, replication, message queues | Design a distributed task queue | 3-4h |
| 24 | Agent Orchestrator | Multi-agent coordination, tool routing, state management | Design a multi-agent orchestration platform | 4h |
| 25 | SDK Platform Design | API design, versioning, plugin architecture, DX | Design an open-source SDK for AI agents | 4h |
| 26 | Observability & Monitoring | Logging, tracing, metrics, debugging distributed agents | Design an agent observability platform | 3-4h |
| 27 | Cloud Deployment | GCP services, Kubernetes, serverless, CI/CD | Design agent deployment pipeline on GCP | 3-4h |
| 28 | Review & Mock | Full system design mock interview | Design Google ADK from scratch (45 min) | 4h |

### 🧠 Skills to Improve
- Structuring a system design answer (requirements → high-level → deep dive → trade-offs)
- Estimating scale (back-of-envelope calculations)
- Discussing trade-offs clearly
- Designing for agent-specific concerns (tool calls, LLM latency, state management)

### 📊 Expected Outcomes
- Complete a system design in 35-40 minutes with clear structure
- Discuss 3+ trade-offs for each design decision
- Relate system design concepts to agent development

### ⚠️ Common Mistakes
- Jumping to the solution without gathering requirements
- Not discussing trade-offs (this is what Google evaluates most!)
- Ignoring non-functional requirements (scalability, latency, cost)
- Not relating to the agent development role

### 💡 Practical Advice
- **Structure**: Use the framework: Clarify → Estimate → High-Level Design → Deep Dive → Trade-offs
- **Agent-Specific**: Always consider: How do agents maintain state? How do you handle LLM failures? How do you observe agent behavior?
- **Google Cloud**: Know GCP services: Cloud Run, GKE, Pub/Sub, BigQuery, Vertex AI, Cloud Functions
- **Practice talking**: Do system design out loud, not just on paper

### 🔧 If You Get Stuck
- Can't estimate? Use powers of 10 and round aggressively
- Don't know a component? Describe what it needs to do, not the specific technology
- Design too complex? Start with a single-server design and scale from there

---

## Week 5: Agent Development — Role-Specific (Days 29-35)

### 🎯 Main Objective
Deep-dive into everything related to agent development, ADK, and the specific skills Google is looking for.

### 📅 Daily Breakdown

| Day | Topic | Key Concepts | Hands-On Project | Time |
|-----|-------|-------------|-----------------|------|
| 29 | LLM Fundamentals | Transformers, attention, tokenization, prompting | Build a prompt engineering toolkit | 4h |
| 30 | Agent Architectures | ReAct, CoT, tool-use, multi-agent patterns | Implement a ReAct agent from scratch | 4h |
| 31 | Google ADK Deep Dive | ADK architecture, agent types, tools, sessions | Build a multi-tool agent with ADK | 4h |
| 32 | Tool Use & Function Calling | Function calling, tool schemas, error handling | Create custom tools with validation | 4h |
| 33 | Testing & Debugging Agents | Unit testing agents, mocking LLMs, eval frameworks | Build an agent testing harness | 4h |
| 34 | Agent Deployment & Observability | Containerization, tracing, metrics, GCP integration | Deploy an agent to Cloud Run | 4h |
| 35 | Review & Mock | Complete agent development project | End-to-end agent with ADK, tested and deployed | 4h |

### 🧠 Skills to Improve
- Understanding how LLMs work at a practical level
- Building agents that use tools effectively
- Testing non-deterministic AI systems
- Deploying and monitoring agents in production

### 📊 Expected Outcomes
- Build a working agent using Google ADK
- Write tests for agent workflows
- Deploy an agent to a cloud environment
- Discuss agent architectures fluently in an interview

### ⚠️ Common Mistakes
- Treating agents as simple API wrappers (they're not!)
- Not handling LLM failures and edge cases
- Ignoring cost and latency in agent design
- Not testing agent behavior systematically

### 💡 Practical Advice
- **Read the ADK source code**: It's open-source, and understanding it shows initiative
- **Build something**: Having a real project to discuss in the interview is invaluable
- **Think enterprise**: Google's customers are enterprises — think about security, compliance, scale
- **Study the ADK GitHub issues**: They reveal what features are being worked on

### 🔧 If You Get Stuck
- ADK hard to set up? Start with the official quickstart guide
- LLMs confusing? Focus on practical usage, not mathematical theory
- Can't deploy? Use Google Cloud's free tier or local Docker

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
| 41 | Role Fit & Portfolio | Present your projects, articulate your fit | Prepare your "Why Google" and "Why this role" answers | 3h |
| 42 | Final Review & Application | Polish CV, submit application, final checklist | Submit application, review everything | 3h |

### 🧠 Skills to Improve
- Storytelling under pressure
- Communicating technical decisions clearly
- Presenting yourself as a strong fit for this specific role
- Managing interview anxiety

### 📊 Expected Outcomes
- 8-10 polished STAR stories ready to deploy
- Confident system design presentation ability
- Consistent Medium problem solving in < 25 min
- A compelling "Why Google + Why Agent Development" narrative

### ⚠️ Common Mistakes
- Not practicing behavioral answers out loud
- Generic "Why Google" answers ("great culture, great pay")
- Not connecting your experience to the specific role
- Cramming new topics in the last week

### 💡 Practical Advice
- **Record yourself**: Record your behavioral answers and review them
- **Get feedback**: Do at least 2 mock interviews with friends or online platforms (Pramp, Interviewing.io)
- **Sleep well**: The last 3 days should be light review, not intensive study
- **Have questions ready**: Prepare 5+ thoughtful questions for your interviewer about ADK and agent development

### 🔧 If You Get Stuck
- Can't find mock interview partners? Use Pramp (free) or Interviewing.io
- Behavioral stories feel weak? Focus on impact and learning, not the complexity of the project
- Anxiety? Remember: the interviewer wants you to succeed. They're looking for signals, not perfection

---

## 📈 Success Metrics

By the end of this 6-week plan, you should be able to:

| Metric | Target |
|--------|--------|
| LeetCode Easy | Solve in < 10 minutes, 95%+ success rate |
| LeetCode Medium | Solve in < 25 minutes, 75%+ success rate |
| LeetCode Hard | Solve in < 45 minutes, 40%+ success rate |
| System Design | Complete a design in 35 min with clear trade-offs |
| Behavioral | 8-10 STAR stories, fluent delivery |
| Agent Development | Built, tested, and deployed at least 1 agent project |
| Google Knowledge | Deep understanding of ADK, GCP, and agent ecosystem |

---

## 📎 Appendix: Recommended Daily Schedule

```
08:00 - 08:30  Review yesterday's notes
08:30 - 10:00  Theory (read notebook theory section)
10:00 - 10:15  Break
10:15 - 12:00  LeetCode practice (timed problems)
12:00 - 13:00  Lunch
13:00 - 14:30  Hands-on project / System design practice
14:30 - 14:45  Break
14:45 - 16:00  Review, flashcards, behavioral practice
16:00 - 16:30  Update progress tracker, plan next day
```

> **Adjust to your schedule.** The key is consistency, not the specific hours. 3-4 focused hours daily beats 8 hours of distracted studying.
