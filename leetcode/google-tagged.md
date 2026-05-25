# 🏷️ Google-Tagged LeetCode Problems

> Problems most frequently asked at Google interviews.
> Focus on these for maximum interview ROI.

---

## Tier 1: Must Solve (Asked 10+ times at Google)

| #   | Problem                                                                                     | Difficulty | Topic         | Key Skill                      |
| --- | ------------------------------------------------------------------------------------------- | ---------- | ------------- | ------------------------------ |
| 1   | [Two Sum](https://leetcode.com/problems/two-sum/)                                           | Easy       | HashMap       | Hash table lookup              |
| 42  | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)                   | Hard       | Two Pointers  | Multi-approach thinking        |
| 56  | [Merge Intervals](https://leetcode.com/problems/merge-intervals/)                           | Medium     | Sorting       | Interval handling              |
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/)                       | Medium     | Graph         | BFS/DFS on grids               |
| 295 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Hard       | Heap          | Dual heap design               |
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/)                                   | Medium     | DP            | Classic DP                     |
| 394 | [Decode String](https://leetcode.com/problems/decode-string/)                               | Medium     | Stack         | Nested parsing                 |
| 560 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)               | Medium     | Prefix Sum    | Prefix sum + HashMap           |
| 359 | [Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/)                   | Easy       | Design        | HashTable / Queue cleanup      |
| 528 | [Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/)           | Medium     | Binary Search | Prefix sum + Cumulative lookup |

## Tier 2: Highly Likely (Asked 5-10 times)

| #    | Problem                                                                                                                         | Difficulty | Topic            | Key Skill                             |
| ---- | ------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------------- | ------------------------------------- |
| 3    | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium     | Sliding Window   | Dynamic window size tracking          |
| 5    | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)                                   | Medium     | DP/Expand        | Expansion around center               |
| 15   | [3Sum](https://leetcode.com/problems/3sum/)                                                                                     | Medium     | Two Pointers     | Sorting + Two-pointer search          |
| 20   | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)                                                           | Easy       | Stack            | Last-In-First-Out evaluation          |
| 23   | [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)                                                     | Hard       | Heap             | Min-heap tracking                     |
| 33   | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)                                 | Medium     | Binary Search    | Modified condition checks             |
| 46   | [Permutations](https://leetcode.com/problems/permutations/)                                                                     | Medium     | Backtracking     | State space tree generation           |
| 76   | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)                                             | Hard       | Sliding Window   | Two-pointer frequency map             |
| 127  | [Word Ladder](https://leetcode.com/problems/word-ladder/)                                                                       | Hard       | BFS              | Shortest path on unweighted graph     |
| 207  | [Course Schedule](https://leetcode.com/problems/course-schedule/)                                                               | Medium     | Topological Sort | Cycle detection (DFS/Kahn's)          |
| 210  | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)                                                         | Medium     | Topological Sort | Linear dependency ordering            |
| 238  | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)                                     | Medium     | Arrays           | Prefix & Suffix running products      |
| 297  | [Serialize/Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)                       | Hard       | Tree             | Structural serialization APIs         |
| 347  | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)                                               | Medium     | Heap             | Bucket sort or Min-Heap tracking      |
| 399  | [Evaluate Division](https://leetcode.com/problems/evaluate-division/)                                                           | Medium     | Graph            | Equations modeled as graphs (DFS/BFS) |
| 438  | [Find All Anagrams in String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)                                     | Medium     | Sliding Window   | Fixed-size window mapping             |
| 1146 | [Snapshot Array](https://leetcode.com/problems/snapshot-array/)                                                                 | Medium     | Design           | Binary search over versioned history  |
| 1293 | [Shortest Path in a Grid with Obstacles](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/)     | Hard       | Graph            | 3D state tracking BFS                 |
| 2096 | [Step-By-Step Directions](https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/)            | Medium     | Tree             | Lowest Common Ancestor (LCA) paths    |

## Tier 3: Good to Know (Asked 3-5 times)

| #    | Problem                                                                                                     | Difficulty | Topic            | Key Skill                                    |
| ---- | ----------------------------------------------------------------------------------------------------------- | ---------- | ---------------- | -------------------------------------------- |
| 11   | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)                       | Medium     | Two Pointers     | Inside-out boundary narrowing                |
| 17   | [Letter Combinations of Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Medium     | Backtracking     | Combinatorial mapping recursion              |
| 22   | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)                                 | Medium     | Backtracking     | Valid state filtering constraints            |
| 39   | [Combination Sum](https://leetcode.com/problems/combination-sum/)                                           | Medium     | Backtracking     | Deduplication via index tracking             |
| 49   | [Group Anagrams](https://leetcode.com/problems/group-anagrams/)                                             | Medium     | HashMap          | Categorization via sorted keys               |
| 68   | [Text Justification](https://leetcode.com/problems/text-justification/)                                     | Hard       | String           | Complex rule-based line parsing              |
| 79   | [Word Search](https://leetcode.com/problems/word-search/)                                                   | Medium     | Backtracking     | In-place grid cell marking                   |
| 84   | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)             | Hard       | Stack            | Monotonic stack tracking                     |
| 98   | [Validate BST](https://leetcode.com/problems/validate-binary-search-tree/)                                  | Medium     | Tree             | Dynamic range constraint tracking            |
| 102  | [Binary Tree Level Order](https://leetcode.com/problems/binary-tree-level-order-traversal/)                 | Medium     | BFS              | Queue-based layer isolation                  |
| 128  | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)                 | Medium     | HashSet          | Fast lookup & sequence boundaries            |
| 146  | [LRU Cache](https://leetcode.com/problems/lru-cache/)                                                       | Medium     | Design           | Doubly Linked List + HashMap                 |
| 198  | [House Robber](https://leetcode.com/problems/house-robber/)                                                 | Medium     | DP               | Subproblem recurrence mapping                |
| 215  | [Kth Largest Element](https://leetcode.com/problems/kth-largest-element-in-an-array/)                       | Medium     | Heap/Quickselect | Pivot-based partitioning                     |
| 226  | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)                                     | Easy       | Tree             | Structural swapping recursion                |
| 300  | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)             | Medium     | DP               | Binary search state optimization             |
| 489  | [Robot Room Cleaner](https://leetcode.com/problems/robot-room-cleaner/)                                     | Hard       | Backtracking     | Backtracking with structural API constraints |
| 543  | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)                           | Easy       | Tree             | Global state mutation via bottom-up DFS      |
| 763  | [Partition Labels](https://leetcode.com/problems/partition-labels/)                                         | Medium     | Greedy           | Last occurrence boundary matching            |
| 843  | [Guess the Word](https://leetcode.com/problems/guess-the-word/)                                             | Hard       | Minimax          | Eliminating candidates algorithmically       |
| 2034 | [Stock Price Fluctuation](https://leetcode.com/problems/stock-price-fluctuation/)                           | Medium     | Design           | HashMap paired with Heaps/TreeMaps           |