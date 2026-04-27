# 📋 Complete LeetCode Plan — SRE Edition

> 120+ problems organized by week, difficulty, and Google SRE relevance.

---

## Week 1: Foundations (30 problems)

### Day 1: Arrays & Strings (5)
| # | Problem | Difficulty | Pattern | Google Sreq |
|---|---------|-----------|---------|-------------|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | HashMap lookup | ⭐⭐⭐⭐⭐ |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | Frequency count | ⭐⭐⭐ |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | Prefix/suffix | ⭐⭐⭐⭐⭐ |
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | Kadane's variant | ⭐⭐⭐⭐ |
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Medium | Kadane's | ⭐⭐⭐⭐ |

### Day 5: Stacks & Queues (5) — *High SRE Relevance*
| # | Problem | Difficulty | Pattern | SRE Focus |
|---|---------|-----------|---------|-----------|
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | Stack matching | Parsing/Validation |
| 155 | [Min Stack](https://leetcode.com/problems/min-stack/) | Medium | Dual stack | Resource Tracking |
| 739 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium | Monotonic stack | Metrics Analysis |
| 150 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Medium | Stack eval | Expression Parsing |
| 84 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Hard | Monotonic stack | Area/Capacity |

---

## Week 2: Intermediate (30 problems)

### Day 13: Sorting & Simulation
| # | Problem | Difficulty | Topic |
|---|---------|-----------|-------|
| 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | Resource Scheduling |
| 57 | [Insert Interval](https://leetcode.com/problems/insert-interval/) | Medium | Availability Windows |
| 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | Medium | Data Partitioning |
| 621 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Medium | CPU Scheduling |

---

## Week 4: System & Data Structure Design

These are critical for SRE coding rounds where you often build a system component.

| # | Problem | Difficulty | Topic |
|---|---------|-----------|-------|
| 146 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium | Cache Management |
| 460 | [LFU Cache](https://leetcode.com/problems/lfu-cache/) | Hard | Advanced Caching |
| 355 | [Design Twitter](https://leetcode.com/problems/design-twitter/) | Medium | System Simulation |
| 380 | [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | Medium | Data Structure Design |
| 208 | [Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | Prefix Search |

---

## Week 5: Graphs & Networking

SREs handle network topologies and service dependencies.

| # | Problem | Difficulty | Topic |
|---|---------|-----------|-------|
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | Connectivity |
| 207 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | Dependency Graph |
| 210 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Medium | Topological Sort |
| 743 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | Shortest Path (Dijkstra) |
| 1514 | [Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) | Medium | Network Reliability |

---

## Google SRE Must-Solve (Top 10)

1. **[LRU Cache](https://leetcode.com/problems/lru-cache/)** (Medium) — Designing efficient memory usage.
2. **[Merge Intervals](https://leetcode.com/problems/merge-intervals/)** (Medium) — Handling overlapping time periods.
3. **[Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)** (Medium) — Resolving service dependencies.
4. **[Network Delay Time](https://leetcode.com/problems/network-delay-time/)** (Medium) — Calculating latency in a network.
5. **[Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)** (Hard) — Real-time metrics processing.
6. **[Decode String](https://leetcode.com/problems/decode-string/)** (Medium) — Parsing log/config data.
7. **[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)** (Easy) — Syntax validation.
8. **[Number of Islands](https://leetcode.com/problems/number-of-islands/)** (Medium) — Cluster/region analysis.
9. **[Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)** (Medium) — Pattern matching in telemetry.
10. **[Word Search II](https://leetcode.com/problems/word-search-ii/)** (Hard) — High-performance string matching.
