# [Gemini Visualizer](https://gemini.google.com/share/e99164b7d2de)

## 1. Two Pointers (Converging)

### When to Use & Alternatives

* **Use when:** The input array/string is **sorted** and you need to find a pair, triplet, or reverse elements matching a target.
* **Alternative:** If the array is *unversorted*, use a **Hash Map** to trade space ($O(N)$) for time ($O(N)$) instead of sorting it first.

### Complexity

* **Time Complexity:** $O(N)$
* **Space Complexity:** $O(1)$

```python
def two_pointers(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Check whether the current pair satisfies the problem condition.
        if is_valid(arr[left], arr[right]):
            return process(arr[left], arr[right])

        # Move the pointer that can help satisfy the condition.
        if should_move_left(arr[left], arr[right]):
            left += 1
        else:
            right -= 1

    return default_result()

```

---

## 2. Sliding Window (Variable Size)

### When to Use & Alternatives

* **Use when:** You need to find the **longest/shortest subarray or substring** that satisfies a specific condition (e.g., maximum sum, unique characters).
* **Alternative:** If the window size is fixed (e.g., "find max sum of $K$ consecutive elements"), remove the `while` loop and maintain a static distance between `left` and `right`.

### Complexity

* **Time Complexity:** $O(N)$ (Each element is visited at most twice: once by `right`, once by `left`).
* **Space Complexity:** $O(K)$ where $K$ is the number of distinct elements in the window (e.g., tracking frequencies in a hash map).

```python
def sliding_window(arr):
    left = 0
    answer = initialize_answer()
    state = {}  # Or set(), used to track window criteria
    
    for right in range(len(arr)):
        # 1. Add the right element to the current window.
        add(state, arr[right])
        
        # 2. Shrink the window until the condition becomes valid again.
        while not window_is_valid(state):
            remove(state, arr[left])
            left += 1
            
        # 3. Update the answer using the current valid window.
        answer = update_answer(answer, left, right, state)
        
    return answer

```

---

## 3. Binary Search

### When to Use & Alternatives

* **Use when:** The array is **sorted**, or you are searching for a specific monotonic threshold/boundary (e.g., "Find the minimum speed to finish eating fruits within $H$ hours").
* **Alternative:** Linear search ($O(N)$) if the array cannot be sorted or logic isn't monotonic.

### Complexity

* **Time Complexity:** $O(\log N)$
* **Space Complexity:** $O(1)$

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Prevents overflow
        
        if is_match(arr[mid], target):
            return mid
        elif go_right(arr[mid], target):
            left = mid + 1
        else:
            right = mid - 1
            
    return not_found()

```

---

## 4. Breadth-First Search (BFS)

### When to Use & Alternatives

* **Use when:** Finding the **shortest path** in an unweighted graph/grid, traversing a tree level-by-level, or expanding nodes in layers.
* **Alternative:** Depth-First Search (DFS) if you need to explore paths deeply, backtrack, or keep the queue footprint smaller on narrow graphs.

### Complexity

* **Time Complexity:** $O(V + E)$ where $V$ is vertices and $E$ is edges.
* **Space Complexity:** $O(V)$ to store the queue and visited set.

### BFS Template 1: Graph or Tree Level Order

```python
from collections import deque

def bfs_level_order(start_node):
    queue = deque([start_node])
    visited = {start_node}

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            if is_target(node):
                return handle_match(node)

            for neighbor in get_neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        after_level()

    return not_found()

```

### BFS Template 2: Shortest Path With Distance

```python
from collections import deque

def bfs_shortest_path(start_node, target):
    queue = deque([(start_node, 0)])
    visited = {start_node}

    while queue:
        node, distance = queue.popleft()

        if node == target:
            return distance

        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return -1

```

### BFS Template 3: Matrix or Grid

```python
from collections import deque

def bfs_grid(grid, start_r, start_c):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start_r, start_c)])
    visited = {(start_r, start_c)}

    while queue:
        r, c = queue.popleft()

        if is_target_cell(grid[r][c]):
            return handle_match((r, c))

        for dr, dc in directions():
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc, rows, cols) and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc))

    return not_found()

```

---

## 5. Depth-First Search (DFS)

### When to Use & Alternatives

* **Use when:** You need to visit every node, count connected components, explore all paths deeply, or generate combinations of states.
* **Alternative:** BFS if you specifically need the shortest path in an unweighted graph/grid.

### Complexity

* **Time Complexity:** $O(R \times C)$ where $R$ is rows and $C$ is columns.
* **Space Complexity:** $O(R \times C)$ worst-case for the recursive call stack.

### DFS Template 1: Recursive Graph or Tree

```python
def dfs_recursive(node, visited):
    if node in visited:
        return

    visited.add(node)

    if is_target(node):
        handle_match(node)

    for neighbor in get_neighbors(node):
        dfs_recursive(neighbor, visited)

```

### DFS Template 2: Recursive Matrix or Grid

```python
def dfs_grid(grid, r, c, visited):
    rows, cols = len(grid), len(grid[0])

    if not in_bounds(r, c, rows, cols):
        return
    if (r, c) in visited:
        return
    if not is_valid_cell(grid[r][c]):
        return

    visited.add((r, c))
    mark_visited(grid, r, c)

    for dr, dc in directions():
        dfs_grid(grid, r + dr, c + dc, visited)

```

### DFS Template 3: Connected Components

```python
def count_components(graph):
    visited = set()
    components = 0

    for node in graph:
        if node not in visited:
            dfs_recursive(node, visited)
            components += 1

    return components

```

### DFS Template 4: Iterative Stack

```python
def dfs_iterative(start_node):
    stack = [start_node]
    visited = set()

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)

        if is_target(node):
            return handle_match(node)

        for neighbor in reversed(get_neighbors(node)):
            if neighbor not in visited:
                stack.append(neighbor)

    return not_found()

```

---

## 6. Backtracking

### When to Use & Alternatives

* **Use when:** You need to generate **all possible configurations** (permutations, combinations, subsets, or N-Queens solutions).
* **Alternative:** Dynamic Programming (if you only need to *count* or find the *min/max* value of paths, rather than returning the paths themselves).

### Complexity

* **Time Complexity:** $O(2^N)$ for subsets, $O(N!)$ for permutations.
* **Space Complexity:** $O(N)$ for the recursion stack.

```python
def backtracking(items):
    res = []
    
    def backtrack(start, path):
        # 1. Accept the current partial solution if needed.
        if should_record(path):
            res.append(list(path))
        
        # 2. Iterate through the available choices.
        for i in range(start, len(items)):
            # Make a choice.
            path.append(items[i])
            
            # Recurse with the next available choices.
            backtrack(i + 1, path)
            
            # Undo the choice.
            path.pop()
            
    backtrack(0, [])
    return res

```

---

## 7. Monotonic Stack

### When to Use & Alternatives

* **Use when:** You need to find the **next greater element** or **previous smaller element** for every index in an array (e.g., Daily Temperatures).
* **Alternative:** A nested loop ($O(N^2)$), which will usually result in a Time Limit Exceeded (TLE) error.

### Complexity

* **Time Complexity:** $O(N)$ (Each index is pushed and popped at most once).
* **Space Complexity:** $O(N)$

```python
def monotonic_stack(arr):
    res = initialize_result(len(arr))
    stack = []  # Stores indices
    
    for i in range(len(arr)):
        # Maintain the chosen monotonic property.
        while stack and should_pop(arr[stack[-1]], arr[i]):
            prev_index = stack.pop()
            res[prev_index] = process_pair(arr[prev_index], arr[i])
            
        stack.append(i)
        
    return res

```

---

## 8. Top K Elements (Heap / Priority Queue)

### When to Use & Alternatives

* **Use when:** You need to find the $K$ largest, smallest, or most frequent items in an unsorted collection.
* **Alternative:** Sort the entire array ($O(N \log N)$). Using a heap drops this time down significantly.

### Complexity

* **Time Complexity:** $O(N \log K)$
* **Space Complexity:** $O(K)$

```python
import heapq

def top_k(nums, k):
    # Initialize the heap used to keep only the best k elements.
    min_heap = []
    
    for num in nums:
        heapq.heappush(min_heap, num)
        
        # Keep the heap restricted to k elements.
        if len(min_heap) > k:
            heapq.heappop(min_heap)
            
    # Return the selected elements in heap form or sorted form as needed.
    return min_heap

```

---

## 9. Dynamic Programming

### When to Use & Alternatives

* **Use when:** The problem has **overlapping subproblems** and an **optimal substructure**. Typical signals are paths, subsequences, counting ways, or min/max decisions.
* **Alternative:** Use recursion or greedy only if the state space is tiny or the choice is provably local.

### Complexity

* **Time Complexity:** Usually $O(N)$, $O(N^2)$, or $O(N \times M)$ depending on the state dimensions.
* **Space Complexity:** Usually $O(N)$, $O(N \times M)$, or $O(1)$ with state compression.

```python
def dynamic_programming(items):
    n = len(items)
    dp = initialize_dp(n)

    # Base cases.
    dp[0] = base_case_0()
    if n > 1:
        dp[1] = base_case_1()

    for i in range(2, n):
        dp[i] = transition(dp, items, i)

    return dp[n - 1]

```

```python
def dynamic_programming_optimized(items):
    prev2 = base_case_0()
    prev1 = base_case_1()

    for i in range(2, len(items)):
        current = transition_optimized(prev2, prev1, items, i)
        prev2, prev1 = prev1, current

    return prev1

```
