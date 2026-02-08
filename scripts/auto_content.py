#!/usr/bin/env python3
"""
auto_content.py
===============
Algorithmic content generator for LeetCode problems.
Auto-generates mermaid diagrams, pseudocode, approach text, complexity analysis,
and step-by-step animations for every problem based on topic tags and code structure.

This eliminates the need to hand-craft KB entries for every problem.
"""

# ═══════════════════════════════════════════════════════════════════
# PATTERN CLASSIFIER
# ═══════════════════════════════════════════════════════════════════

# Priority-ordered list of (tag_set, pattern_name)
# First match wins; more specific combos come first.
PATTERN_RULES = [
    # --- Very specific combos first ---
    ({"Topological Sort"},                  "topological_sort"),
    ({"Trie"},                              "trie"),
    ({"Union Find"},                        "union_find"),
    ({"Union-Find"},                        "union_find"),
    ({"Monotonic Stack"},                   "monotonic_stack"),
    ({"Monotonic Queue"},                   "monotonic_queue"),
    ({"Sliding Window"},                    "sliding_window"),
    ({"Segment Tree"},                      "segment_tree"),
    ({"Binary Indexed Tree"},               "binary_indexed_tree"),
    ({"Quickselect"},                       "quickselect"),
    ({"Merge Sort"},                        "merge_sort"),
    ({"Reservoir Sampling"},                "reservoir_sampling"),
    ({"Ordered Set"},                       "ordered_set"),
    ({"Line Sweep", "Sweep Line"},          "line_sweep"),
    ({"Doubly-Linked List"},                "linked_list"),
    ({"Linked List"},                       "linked_list"),
    ({"Heap (Priority Queue)"},             "heap"),
    ({"Backtracking"},                      "backtracking"),
    ({"Binary Search Tree"},                "bst"),
    ({"Binary Search"},                     "binary_search"),
    ({"Shortest Path"},                     "shortest_path"),
    ({"Depth-First Search", "Tree"},        "dfs_tree"),
    ({"Breadth-First Search", "Tree"},      "bfs_tree"),
    ({"Depth-First Search", "Graph"},       "dfs_graph"),
    ({"Breadth-First Search", "Graph"},     "bfs_graph"),
    ({"Depth-First Search", "Matrix"},      "dfs_matrix"),
    ({"Breadth-First Search", "Matrix"},    "bfs_matrix"),
    ({"Depth-First Search", "Binary Tree"}, "dfs_tree"),
    ({"Breadth-First Search", "Binary Tree"}, "bfs_tree"),
    ({"Depth-First Search"},                "dfs_graph"),
    ({"Breadth-First Search"},              "bfs_graph"),
    ({"Tree", "Binary Tree"},              "tree_traversal"),
    ({"Tree"},                              "tree_traversal"),
    ({"Binary Tree"},                       "tree_traversal"),
    ({"Graph", "Graph Theory"},             "graph_general"),
    ({"Graph"},                             "graph_general"),
    ({"Graph Theory"},                      "graph_general"),
    ({"Dynamic Programming", "Matrix"},     "dp_2d"),
    ({"Dynamic Programming", "String"},     "dp_string"),
    ({"Dynamic Programming", "Bitmask"},    "dp_bitmask"),
    ({"Dynamic Programming"},               "dp_1d"),
    ({"Memoization"},                       "dp_1d"),
    ({"Greedy", "Sorting"},                 "greedy_sort"),
    ({"Greedy"},                            "greedy"),
    ({"Two Pointers", "Sorting"},           "two_pointer_sorted"),
    ({"Two Pointers"},                      "two_pointer"),
    ({"Stack"},                             "stack"),
    ({"Queue"},                             "queue"),
    ({"Prefix Sum"},                        "prefix_sum"),
    ({"Bit Manipulation"},                  "bit_manipulation"),
    ({"Divide and Conquer"},                "divide_conquer"),
    ({"Sorting"},                           "sorting"),
    ({"Counting Sort"},                     "sorting"),
    ({"Bucket Sort"},                       "sorting"),
    ({"Radix Sort"},                        "sorting"),
    ({"Design", "Data Stream"},             "design_stream"),
    ({"Design"},                            "design"),
    ({"Simulation"},                        "simulation"),
    ({"Iterator"},                          "design"),
    ({"Randomized"},                        "randomized"),
    ({"Hash Table", "Array"},               "hash_map"),
    ({"Hash Table", "String"},              "hash_map_string"),
    ({"Hash Table"},                        "hash_map"),
    ({"Matrix"},                            "matrix"),
    ({"Geometry"},                          "geometry"),
    ({"Number Theory"},                     "number_theory"),
    ({"Combinatorics"},                     "combinatorics"),
    ({"Math"},                              "math"),
    ({"String Matching"},                   "string_matching"),
    ({"String"},                            "string"),
    ({"Enumeration"},                       "enumeration"),
    ({"Counting"},                          "counting"),
    ({"Recursion"},                         "recursion"),
    ({"Array"},                             "array"),
    ({"Bitmask"},                           "bit_manipulation"),
]


def classify_pattern(tags):
    """Classify a problem into an algorithm pattern based on its tags."""
    tag_set = set(tags) if tags else set()
    for required_tags, pattern in PATTERN_RULES:
        if isinstance(required_tags, set):
            if required_tags & tag_set:  # any overlap
                # For multi-tag rules (len > 1), require ALL tags
                if len(required_tags) > 1:
                    if required_tags <= tag_set:
                        return pattern
                else:
                    return pattern
        elif required_tags in tag_set:
            return pattern
    return "general"


# ═══════════════════════════════════════════════════════════════════
# PATTERN METADATA DATABASE
# ═══════════════════════════════════════════════════════════════════

PATTERNS = {

# ─── Hash Map ───
"hash_map": {
    "name": "Hash Map Lookup",
    "time": "O(n)",
    "space": "O(n)",
    "approach": "Use a hash map (dictionary) to store elements for O(1) lookup. "
                "Iterate through the input, checking membership or counting frequencies in the map.",
    "pseudocode": (
        "1. Initialize hash map\n"
        "2. Iterate through elements:\n"
        "   a. Check if target/complement exists in map\n"
        "   b. If found: process result\n"
        "   c. Otherwise: store element in map\n"
        "3. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Initialize hash map] --> B[For each element]
    B --> C{Target in map?}
    C -- Yes --> D[Process / return result]
    C -- No --> E[Store element in map]
    E --> B
    D --> F[Return answer]
```""",
},

"hash_map_string": {
    "name": "Hash Map String Processing",
    "time": "O(n)",
    "space": "O(n)",
    "approach": "Use a hash map to count character frequencies or map characters/strings for O(1) lookups. "
                "Process the string in one or two passes.",
    "pseudocode": (
        "1. Build frequency map / char-to-index map\n"
        "2. Iterate through string:\n"
        "   a. Look up character in map\n"
        "   b. Update counts or mappings\n"
        "3. Return result based on map state"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Build character frequency map] --> B[Iterate through string]
    B --> C{Lookup char in map}
    C --> D[Update map / counters]
    D --> E{All chars processed?}
    E -- No --> B
    E -- Yes --> F[Return result from map]
```""",
},

# ─── Two Pointers ───
"two_pointer": {
    "name": "Two Pointers",
    "time": "O(n)",
    "space": "O(1)",
    "approach": "Use two pointers moving through the data structure. "
                "Depending on the problem, pointers may move toward each other (converging), "
                "in the same direction (fast/slow), or independently.",
    "pseudocode": (
        "1. Initialize left = 0, right = n-1 (or two independent pointers)\n"
        "2. While pointers haven't crossed:\n"
        "   a. Evaluate condition at pointer positions\n"
        "   b. Move left pointer right or right pointer left\n"
        "3. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[left = 0, right = n-1] --> B{left < right?}
    B -- Yes --> C[Evaluate at left, right]
    C --> D{Condition met?}
    D -- Yes --> E[Record result]
    D -- No --> F{Adjust which pointer?}
    F --> G[Move left right]
    F --> H[Move right left]
    G --> B
    H --> B
    E --> I[Return answer]
    B -- No --> I
```""",
},

"two_pointer_sorted": {
    "name": "Two Pointers on Sorted Array",
    "time": "O(n log n)",
    "space": "O(1)",
    "approach": "Sort the array first, then use two pointers converging from both ends. "
                "Move the left pointer right to increase the sum, or the right pointer left to decrease it.",
    "pseudocode": (
        "1. Sort the array\n"
        "2. left = 0, right = n-1\n"
        "3. While left < right:\n"
        "   a. Compute current = arr[left] + arr[right]\n"
        "   b. If current == target: found\n"
        "   c. If current < target: left++\n"
        "   d. If current > target: right--\n"
        "4. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Sort array] --> B[left=0, right=n-1]
    B --> C{left < right?}
    C -- Yes --> D[sum = arr_left + arr_right]
    D --> E{sum == target?}
    E -- Yes --> F[Found - return result]
    E -- No --> G{sum < target?}
    G -- Yes --> H[left++]
    G -- No --> I[right--]
    H --> C
    I --> C
    C -- No --> J[Not found]
```""",
},

# ─── Sliding Window ───
"sliding_window": {
    "name": "Sliding Window",
    "time": "O(n)",
    "space": "O(k)",
    "approach": "Maintain a window over the data using two pointers. "
                "Expand the right boundary to include new elements, and shrink the left boundary "
                "when the window constraint is violated. Track the optimal window.",
    "pseudocode": (
        "1. Initialize left = 0, result = initial_value\n"
        "2. For right in range(n):\n"
        "   a. Add element at right to window state\n"
        "   b. While window is invalid:\n"
        "      - Remove element at left from window state\n"
        "      - left++\n"
        "   c. Update result = best of (result, window size/value)\n"
        "3. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[left=0, window state empty] --> B[Expand: right pointer moves right]
    B --> C[Add arr_right to window]
    C --> D{Window valid?}
    D -- No --> E[Shrink: remove arr_left, left++]
    E --> D
    D -- Yes --> F[Update best result]
    F --> G{right < n-1?}
    G -- Yes --> B
    G -- No --> H[Return best result]
```""",
},

# ─── Binary Search ───
"binary_search": {
    "name": "Binary Search",
    "time": "O(log n)",
    "space": "O(1)",
    "approach": "Use binary search to halve the search space each iteration. "
                "Define the search range [lo, hi], compute mid, and decide which half to keep "
                "based on the problem's monotonic condition.",
    "pseudocode": (
        "1. lo = lower_bound, hi = upper_bound\n"
        "2. While lo <= hi (or lo < hi):\n"
        "   a. mid = (lo + hi) // 2\n"
        "   b. If condition(mid) is satisfied: record answer, search left half\n"
        "   c. Else: search right half\n"
        "3. Return answer"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[lo = lower bound, hi = upper bound] --> B{lo <= hi?}
    B -- Yes --> C[mid = lo + hi / 2]
    C --> D{Check condition at mid}
    D -- Target found --> E[Return mid]
    D -- Go left --> F[hi = mid - 1]
    D -- Go right --> G[lo = mid + 1]
    F --> B
    G --> B
    B -- No --> H[Return lo or -1]
```""",
},

# ─── Linked List ───
"linked_list": {
    "name": "Linked List",
    "time": "O(n)",
    "space": "O(1)",
    "approach": "Traverse or manipulate the linked list using pointer techniques. "
                "Common patterns: dummy head node for edge cases, fast/slow pointers for cycle detection "
                "or middle finding, in-place reversal, and merge operations.",
    "pseudocode": (
        "1. Create dummy head if needed\n"
        "2. Initialize pointer(s) at head\n"
        "3. Traverse / modify list:\n"
        "   a. Process current node\n"
        "   b. Adjust next pointers as needed\n"
        "   c. Move to next node\n"
        "4. Return dummy.next or result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Create dummy head node] --> B[curr = head]
    B --> C{curr is not null?}
    C -- Yes --> D[Process current node]
    D --> E[Adjust pointers / links]
    E --> F[curr = curr.next]
    F --> C
    C -- No --> G[Return dummy.next or result]
```""",
},

# ─── Stack ───
"stack": {
    "name": "Stack",
    "time": "O(n)",
    "space": "O(n)",
    "approach": "Use a stack (LIFO) to process elements. Push elements when they might be needed later; "
                "pop when a matching or resolving condition is found. "
                "Common uses: parentheses matching, expression evaluation, next greater element.",
    "pseudocode": (
        "1. Initialize empty stack\n"
        "2. For each element:\n"
        "   a. While stack is not empty and condition met:\n"
        "      - Pop and process top element\n"
        "   b. Push current element onto stack\n"
        "3. Process remaining elements in stack if needed\n"
        "4. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Initialize empty stack] --> B[For each element]
    B --> C{Stack not empty AND condition?}
    C -- Yes --> D[Pop top element]
    D --> E[Process popped element]
    E --> C
    C -- No --> F[Push current element]
    F --> G{More elements?}
    G -- Yes --> B
    G -- No --> H[Return result]
```""",
},

# ─── Monotonic Stack ───
"monotonic_stack": {
    "name": "Monotonic Stack",
    "time": "O(n)",
    "space": "O(n)",
    "approach": "Maintain a stack where elements are always in monotonic order (increasing or decreasing). "
                "When a new element violates the monotonic property, pop elements and compute results "
                "(e.g., next greater/smaller element, spans, areas).",
    "pseudocode": (
        "1. Initialize empty stack, result array\n"
        "2. For each element (index i):\n"
        "   a. While stack not empty and arr[i] breaks monotonic order:\n"
        "      - Pop index j from stack\n"
        "      - result[j] = compute(i, j)\n"
        "   b. Push i onto stack\n"
        "3. Handle remaining elements in stack\n"
        "4. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Stack = empty, result = default] --> B[For each element at index i]
    B --> C{Stack top violates monotonic order?}
    C -- Yes --> D[Pop index j from stack]
    D --> E["result[j] = f(i, j)"]
    E --> C
    C -- No --> F[Push i onto stack]
    F --> G{More elements?}
    G -- Yes --> B
    G -- No --> H[Handle remaining stack items]
    H --> I[Return result]
```""",
},

"monotonic_queue": {
    "name": "Monotonic Queue / Deque",
    "time": "O(n)",
    "space": "O(k)",
    "approach": "Use a deque to maintain a monotonic window of elements. "
                "Remove from the back to maintain order, remove from the front when elements leave the window.",
    "pseudocode": (
        "1. Initialize deque\n"
        "2. For each element:\n"
        "   a. Remove from back while deque back <= current\n"
        "   b. Add current to back\n"
        "   c. Remove from front if outside window\n"
        "   d. Front of deque is the window max/min\n"
        "3. Return results"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Initialize deque] --> B[For each element i]
    B --> C[Remove from back while back <= arr_i]
    C --> D[Push i to back]
    D --> E[Remove front if outside window]
    E --> F["Window max/min = deque front"]
    F --> G{More elements?}
    G -- Yes --> B
    G -- No --> H[Return results]
```""",
},

# ─── Queue / BFS ───
"queue": {
    "name": "Queue / BFS",
    "time": "O(n)",
    "space": "O(n)",
    "approach": "Use a queue (FIFO) for level-order or breadth-first processing. "
                "Enqueue starting elements, then process level by level.",
    "pseudocode": (
        "1. Initialize queue with starting element(s)\n"
        "2. While queue is not empty:\n"
        "   a. Dequeue front element\n"
        "   b. Process element\n"
        "   c. Enqueue valid neighbors/children\n"
        "3. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Enqueue starting elements] --> B{Queue not empty?}
    B -- Yes --> C[Dequeue front element]
    C --> D[Process element]
    D --> E[Enqueue valid neighbors]
    E --> B
    B -- No --> F[Return result]
```""",
},

# ─── Tree Traversal ───
"tree_traversal": {
    "name": "Tree Traversal",
    "time": "O(n)",
    "space": "O(h)",
    "approach": "Traverse the tree using DFS (preorder, inorder, or postorder) or BFS (level-order). "
                "At each node, compute or accumulate a value and recurse on children.",
    "pseudocode": (
        "1. Define recursive function traverse(node):\n"
        "   a. Base case: if node is null, return default\n"
        "   b. Recurse on left child\n"
        "   c. Process current node\n"
        "   d. Recurse on right child\n"
        "   e. Return combined result\n"
        "2. Call traverse(root)"
    ),
    "mermaid": """```mermaid
flowchart TD
    A["traverse(node)"] --> B{node is null?}
    B -- Yes --> C[Return base value]
    B -- No --> D[left = traverse node.left]
    D --> E[Process current node value]
    E --> F[right = traverse node.right]
    F --> G[Return combined left, node, right]
```""",
},

"dfs_tree": {
    "name": "DFS Tree Traversal",
    "time": "O(n)",
    "space": "O(h)",
    "approach": "Perform depth-first search on the tree. Recurse on left and right subtrees, "
                "combining results bottom-up. Track state (path, depth, sum) during traversal.",
    "pseudocode": (
        "1. Define dfs(node, state):\n"
        "   a. Base case: if null, return default\n"
        "   b. Process node with current state\n"
        "   c. left_result = dfs(node.left, updated_state)\n"
        "   d. right_result = dfs(node.right, updated_state)\n"
        "   e. Return combine(left_result, right_result)\n"
        "2. Return dfs(root, initial_state)"
    ),
    "mermaid": """```mermaid
flowchart TD
    A["dfs(node, state)"] --> B{node is null?}
    B -- Yes --> C[Return base case]
    B -- No --> D[Process node with state]
    D --> E["left = dfs(node.left, state')"]
    E --> F["right = dfs(node.right, state')"]
    F --> G["Return combine(left, right)"]
```""",
},

"bfs_tree": {
    "name": "BFS Level-Order Traversal",
    "time": "O(n)",
    "space": "O(w)",
    "approach": "Traverse the tree level by level using a queue. "
                "Process all nodes at the current depth before moving to the next level.",
    "pseudocode": (
        "1. If root is null, return empty\n"
        "2. Queue = [root]\n"
        "3. While queue not empty:\n"
        "   a. level_size = len(queue)\n"
        "   b. For i in range(level_size):\n"
        "      - node = dequeue\n"
        "      - Process node\n"
        "      - Enqueue node.left, node.right if not null\n"
        "4. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A["Queue = [root]"] --> B{Queue not empty?}
    B -- Yes --> C[level_size = len queue]
    C --> D[Process level_size nodes]
    D --> E[Enqueue children of each node]
    E --> F[Record level result]
    F --> B
    B -- No --> G[Return all level results]
```""",
},

"bst": {
    "name": "Binary Search Tree",
    "time": "O(h)",
    "space": "O(h)",
    "approach": "Leverage BST property: left < root < right. "
                "Navigate left for smaller values, right for larger values. "
                "Inorder traversal yields sorted order.",
    "pseudocode": (
        "1. Start at root\n"
        "2. Compare target with current node:\n"
        "   a. If target < node.val: go left\n"
        "   b. If target > node.val: go right\n"
        "   c. If equal: found\n"
        "3. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Start at root] --> B{node is null?}
    B -- Yes --> C[Not found / insert here]
    B -- No --> D{target vs node.val?}
    D -- Less --> E[Go to node.left]
    D -- Greater --> F[Go to node.right]
    D -- Equal --> G[Found target node]
    E --> B
    F --> B
```""",
},

# ─── Graph Traversals ───
"dfs_graph": {
    "name": "DFS Graph Traversal",
    "time": "O(V + E)",
    "space": "O(V)",
    "approach": "Explore the graph depth-first using recursion or a stack. "
                "Mark nodes as visited to avoid cycles. Process each node and explore all unvisited neighbors.",
    "pseudocode": (
        "1. Initialize visited set\n"
        "2. Define dfs(node):\n"
        "   a. Mark node as visited\n"
        "   b. Process node\n"
        "   c. For each neighbor of node:\n"
        "      - If not visited: dfs(neighbor)\n"
        "3. Call dfs(start) for each unvisited node"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Initialize visited set] --> B["dfs(node)"]
    B --> C[Mark node visited]
    C --> D[Process node]
    D --> E[For each neighbor]
    E --> F{Neighbor visited?}
    F -- No --> G["dfs(neighbor)"]
    G --> E
    F -- Yes --> E
    E --> H{More neighbors?}
    H -- No --> I[Backtrack / return]
```""",
},

"bfs_graph": {
    "name": "BFS Graph Traversal",
    "time": "O(V + E)",
    "space": "O(V)",
    "approach": "Explore the graph breadth-first using a queue. "
                "Process nodes level by level; BFS finds shortest paths in unweighted graphs.",
    "pseudocode": (
        "1. Initialize queue with start node(s), visited set\n"
        "2. While queue not empty:\n"
        "   a. Dequeue node\n"
        "   b. Process node\n"
        "   c. For each unvisited neighbor:\n"
        "      - Mark visited, enqueue\n"
        "3. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Queue = start nodes, visited = start] --> B{Queue not empty?}
    B -- Yes --> C[Dequeue node]
    C --> D[Process node]
    D --> E[For each neighbor]
    E --> F{Already visited?}
    F -- No --> G[Mark visited, enqueue]
    F -- Yes --> E
    G --> E
    E --> B
    B -- No --> H[Return result]
```""",
},

"dfs_matrix": {
    "name": "DFS on Matrix / Grid",
    "time": "O(m * n)",
    "space": "O(m * n)",
    "approach": "Treat the grid as a graph where each cell connects to its 4 (or 8) neighbors. "
                "DFS from target cells, marking visited to avoid revisiting.",
    "pseudocode": (
        "1. For each cell (r, c) in grid:\n"
        "   a. If cell meets start condition:\n"
        "      - Call dfs(r, c)\n"
        "2. dfs(r, c):\n"
        "   a. If out of bounds or visited or invalid: return\n"
        "   b. Mark cell visited\n"
        "   c. Recurse on 4 neighbors: up, down, left, right\n"
        "3. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[For each cell in grid] --> B{Matches start condition?}
    B -- Yes --> C["dfs(r, c)"]
    B -- No --> A
    C --> D{Out of bounds or visited?}
    D -- Yes --> E[Return]
    D -- No --> F[Mark visited, process cell]
    F --> G["dfs(r+1,c), dfs(r-1,c)"]
    G --> H["dfs(r,c+1), dfs(r,c-1)"]
    H --> I[Return result]
```""",
},

"bfs_matrix": {
    "name": "BFS on Matrix / Grid",
    "time": "O(m * n)",
    "space": "O(m * n)",
    "approach": "Breadth-first search on the grid. Enqueue all starting cells, then expand level by level. "
                "BFS on grids finds shortest distance from source(s).",
    "pseudocode": (
        "1. Enqueue all source cells, mark visited\n"
        "2. distance = 0\n"
        "3. While queue not empty:\n"
        "   a. Process all cells at current distance\n"
        "   b. For each cell, enqueue unvisited neighbors\n"
        "   c. distance++\n"
        "4. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Enqueue source cells] --> B{Queue not empty?}
    B -- Yes --> C[Process current level]
    C --> D[For each cell in level]
    D --> E[Check 4 neighbors]
    E --> F{Valid and unvisited?}
    F -- Yes --> G[Mark visited, enqueue]
    F -- No --> E
    G --> E
    D --> H[distance++]
    H --> B
    B -- No --> I[Return distances]
```""",
},

"graph_general": {
    "name": "Graph Algorithm",
    "time": "O(V + E)",
    "space": "O(V + E)",
    "approach": "Build an adjacency list/matrix from the input. "
                "Apply graph traversal (DFS/BFS), shortest path, or connectivity algorithm as needed.",
    "pseudocode": (
        "1. Build adjacency list from edges\n"
        "2. Initialize visited/distance arrays\n"
        "3. Apply traversal algorithm:\n"
        "   - DFS/BFS for reachability\n"
        "   - Dijkstra/Bellman-Ford for shortest path\n"
        "   - Union-Find for connectivity\n"
        "4. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Build adjacency list] --> B[Initialize visited / state]
    B --> C[Choose traversal strategy]
    C --> D[Visit nodes via DFS or BFS]
    D --> E[Process each node and edges]
    E --> F{All nodes processed?}
    F -- No --> D
    F -- Yes --> G[Return result]
```""",
},

"shortest_path": {
    "name": "Shortest Path",
    "time": "O(E log V)",
    "space": "O(V + E)",
    "approach": "Use Dijkstra's algorithm (weighted, non-negative) or BFS (unweighted) "
                "to find shortest paths. Use a min-heap / priority queue for Dijkstra.",
    "pseudocode": (
        "1. Build adjacency list with weights\n"
        "2. dist[start] = 0, all others = INF\n"
        "3. Priority queue: push (0, start)\n"
        "4. While queue not empty:\n"
        "   a. Pop (d, u) with minimum distance\n"
        "   b. If d > dist[u]: skip (stale)\n"
        "   c. For each neighbor v with weight w:\n"
        "      - If dist[u] + w < dist[v]:\n"
        "        dist[v] = dist[u] + w, push (dist[v], v)\n"
        "5. Return dist[target]"
    ),
    "mermaid": """```mermaid
flowchart TD
    A["dist = [INF,...], dist[start]=0"] --> B["Heap = [(0, start)]"]
    B --> C{Heap not empty?}
    C -- Yes --> D["Pop (d, u) minimum"]
    D --> E{d > dist_u? stale?}
    E -- Yes --> C
    E -- No --> F[For each neighbor v]
    F --> G{dist_u + w < dist_v?}
    G -- Yes --> H[Update dist_v, push to heap]
    G -- No --> F
    H --> F
    F --> C
    C -- No --> I[Return dist array]
```""",
},

# ─── Union-Find ───
"union_find": {
    "name": "Union-Find / Disjoint Set",
    "time": "O(n * alpha(n))",
    "space": "O(n)",
    "approach": "Use Union-Find with path compression and union by rank to efficiently manage "
                "connected components. Find(x) returns the root of x's component; Union(x,y) merges two components.",
    "pseudocode": (
        "1. parent[i] = i for all nodes (each is its own set)\n"
        "2. find(x): follow parent pointers to root (with path compression)\n"
        "3. union(x, y): merge sets of x and y by rank\n"
        "4. Process edges/operations:\n"
        "   a. For each edge (u, v): union(u, v)\n"
        "5. Answer queries using find()"
    ),
    "mermaid": """```mermaid
flowchart TD
    A["parent[i] = i for all nodes"] --> B[For each edge or query]
    B --> C{"Operation type?"}
    C -- Union --> D["find root of u and v"]
    D --> E{Same root?}
    E -- Yes --> F[Already connected / cycle]
    E -- No --> G[Merge smaller tree under larger]
    C -- Find --> H[Follow parent to root]
    H --> I[Path compression: flatten tree]
    G --> B
    F --> B
    I --> J[Return root]
```""",
},

# ─── Topological Sort ───
"topological_sort": {
    "name": "Topological Sort",
    "time": "O(V + E)",
    "space": "O(V + E)",
    "approach": "Order nodes in a DAG so every edge u->v has u before v. "
                "Use Kahn's algorithm (BFS with in-degree tracking) or DFS-based ordering.",
    "pseudocode": (
        "1. Compute in-degree for every node\n"
        "2. Enqueue all nodes with in-degree 0\n"
        "3. While queue not empty:\n"
        "   a. Dequeue node u, add to result order\n"
        "   b. For each neighbor v of u:\n"
        "      - Decrease in-degree of v\n"
        "      - If in-degree becomes 0: enqueue v\n"
        "4. If result size != V: cycle exists\n"
        "5. Return topological order"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Compute in-degree for each node] --> B[Enqueue nodes with in-degree 0]
    B --> C{Queue not empty?}
    C -- Yes --> D[Dequeue node u]
    D --> E[Add u to result order]
    E --> F[For each neighbor v of u]
    F --> G[in-degree_v -= 1]
    G --> H{in-degree_v == 0?}
    H -- Yes --> I[Enqueue v]
    H -- No --> F
    I --> F
    F --> C
    C -- No --> J{Result size == V?}
    J -- Yes --> K[Return topological order]
    J -- No --> L[Cycle detected]
```""",
},

# ─── Trie ───
"trie": {
    "name": "Trie / Prefix Tree",
    "time": "O(L) per operation",
    "space": "O(N * L)",
    "approach": "Build a trie (prefix tree) where each node represents a character. "
                "Insert words character by character, and search by following child pointers. "
                "Supports efficient prefix matching.",
    "pseudocode": (
        "1. TrieNode: children = {}, is_end = False\n"
        "2. Insert(word):\n"
        "   - For each char: create child if absent, move to child\n"
        "   - Mark last node as end\n"
        "3. Search(word):\n"
        "   - For each char: if child absent return False, move to child\n"
        "   - Return node.is_end\n"
        "4. StartsWith(prefix): same as search but return True at end"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Root TrieNode] --> B{"Insert / Search / Prefix?"}
    B -- Insert --> C[For each character in word]
    C --> D{Child exists?}
    D -- No --> E[Create new TrieNode child]
    D -- Yes --> F[Move to child]
    E --> F
    F --> G{More characters?}
    G -- Yes --> C
    G -- No --> H[Mark is_end = True]
    B -- Search --> I[For each character in word]
    I --> J{Child exists?}
    J -- No --> K[Return False]
    J -- Yes --> L[Move to child]
    L --> M{More chars?}
    M -- Yes --> I
    M -- No --> N[Return node.is_end]
```""",
},

# ─── Heap / Priority Queue ───
"heap": {
    "name": "Heap / Priority Queue",
    "time": "O(n log n)",
    "space": "O(n)",
    "approach": "Use a min-heap or max-heap to efficiently access the smallest/largest element. "
                "Push elements and pop the top to process in priority order.",
    "pseudocode": (
        "1. Initialize heap (min or max)\n"
        "2. Push initial elements onto heap\n"
        "3. While heap not empty and condition:\n"
        "   a. Pop top element (min or max)\n"
        "   b. Process element\n"
        "   c. Push new elements if needed\n"
        "4. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Initialize heap] --> B[Push starting elements]
    B --> C{Heap not empty?}
    C -- Yes --> D[Pop min or max element]
    D --> E[Process element]
    E --> F{Push new elements?}
    F -- Yes --> G[Push to heap]
    F -- No --> C
    G --> C
    C -- No --> H[Return result]
```""",
},

# ─── Dynamic Programming ───
"dp_1d": {
    "name": "Dynamic Programming (1D)",
    "time": "O(n)",
    "space": "O(n)",
    "approach": "Break the problem into overlapping subproblems. Define dp[i] as the optimal value "
                "for the subproblem ending at or considering index i. Build the solution bottom-up, "
                "using previously computed dp values.",
    "pseudocode": (
        "1. Define dp[i] = optimal value for subproblem i\n"
        "2. Base case: dp[0] = initial value\n"
        "3. For i from 1 to n:\n"
        "   a. dp[i] = recurrence(dp[i-1], dp[i-2], ...)\n"
        "4. Return dp[n] or max/min of dp"
    ),
    "mermaid": """```mermaid
flowchart TD
    A["Define dp[i] meaning"] --> B["Base case: dp[0]"]
    B --> C[For i = 1 to n]
    C --> D["dp[i] = f(dp[i-1], dp[i-2], ...)"]
    D --> E{i < n?}
    E -- Yes --> C
    E -- No --> F["Return dp[n] or aggregate"]
```""",
},

"dp_2d": {
    "name": "Dynamic Programming (2D Grid/Matrix)",
    "time": "O(m * n)",
    "space": "O(m * n)",
    "approach": "Use a 2D DP table where dp[i][j] represents the optimal value for the subproblem "
                "defined by rows 0..i and columns 0..j. Fill row by row or column by column.",
    "pseudocode": (
        "1. Create dp[m][n] table\n"
        "2. Initialize base cases (first row, first column)\n"
        "3. For i from 1 to m-1:\n"
        "   For j from 1 to n-1:\n"
        "     dp[i][j] = recurrence(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])\n"
        "4. Return dp[m-1][n-1]"
    ),
    "mermaid": """```mermaid
flowchart TD
    A["Create dp[m][n]"] --> B[Initialize base: row 0, col 0]
    B --> C[For each row i]
    C --> D[For each column j]
    D --> E["dp[i][j] = f(dp[i-1][j], dp[i][j-1], ...)"]
    E --> F{More columns?}
    F -- Yes --> D
    F -- No --> G{More rows?}
    G -- Yes --> C
    G -- No --> H["Return dp[m-1][n-1]"]
```""",
},

"dp_string": {
    "name": "Dynamic Programming (String)",
    "time": "O(m * n)",
    "space": "O(m * n)",
    "approach": "Compare or match two strings using a 2D DP table. "
                "dp[i][j] represents the answer for substrings s1[0..i-1] and s2[0..j-1]. "
                "Common patterns: LCS, edit distance, regex matching.",
    "pseudocode": (
        "1. Create dp[m+1][n+1]\n"
        "2. Initialize base cases\n"
        "3. For i from 1 to m:\n"
        "   For j from 1 to n:\n"
        "     If s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1] + 1\n"
        "     Else: dp[i][j] = best of (dp[i-1][j], dp[i][j-1], dp[i-1][j-1])\n"
        "4. Return dp[m][n]"
    ),
    "mermaid": """```mermaid
flowchart TD
    A["dp[m+1][n+1] = 0"] --> B[For i = 1 to m]
    B --> C[For j = 1 to n]
    C --> D{"s1[i-1] == s2[j-1]?"}
    D -- Yes --> E["dp[i][j] = dp[i-1][j-1] + 1"]
    D -- No --> F["dp[i][j] = max(dp[i-1][j], dp[i][j-1])"]
    E --> G{More chars?}
    F --> G
    G -- Yes --> C
    G -- No --> H["Return dp[m][n]"]
```""",
},

"dp_bitmask": {
    "name": "Dynamic Programming (Bitmask)",
    "time": "O(2^n * n)",
    "space": "O(2^n)",
    "approach": "Use bitmask to represent subsets of n elements. dp[mask] = optimal value when "
                "the selected subset is represented by mask. Iterate over all masks and transitions.",
    "pseudocode": (
        "1. dp[0] = base case\n"
        "2. For mask from 0 to 2^n - 1:\n"
        "   a. For each bit i not set in mask:\n"
        "      - new_mask = mask | (1 << i)\n"
        "      - dp[new_mask] = best of dp[new_mask], dp[mask] + cost(i)\n"
        "3. Return dp[(1 << n) - 1]"
    ),
    "mermaid": """```mermaid
flowchart TD
    A["dp[0] = base case"] --> B[For each bitmask state]
    B --> C[For each unset bit i]
    C --> D["new_mask = mask | 1 left-shift i"]
    D --> E["dp[new_mask] = best(dp[new_mask], dp[mask] + cost)"]
    E --> C
    C --> F{All masks processed?}
    F -- No --> B
    F -- Yes --> G["Return dp[all bits set]"]
```""",
},

# ─── Backtracking ───
"backtracking": {
    "name": "Backtracking",
    "time": "O(k^n) or O(n!)",
    "space": "O(n)",
    "approach": "Explore all possible solutions by building candidates incrementally. "
                "At each step, make a choice and recurse. If the choice leads to a dead end, "
                "undo the choice (backtrack) and try the next option.",
    "pseudocode": (
        "1. Define backtrack(path, choices):\n"
        "   a. If path is a complete solution: add to results\n"
        "   b. For each choice in choices:\n"
        "      - If choice is valid:\n"
        "        * Add choice to path\n"
        "        * backtrack(path, remaining_choices)\n"
        "        * Remove choice from path (backtrack)\n"
        "2. Call backtrack([], all_choices)"
    ),
    "mermaid": """```mermaid
flowchart TD
    A["backtrack(path, choices)"] --> B{Path complete?}
    B -- Yes --> C[Add path to results]
    B -- No --> D[For each valid choice]
    D --> E[Add choice to path]
    E --> F["backtrack(path, remaining)"]
    F --> G[Remove choice from path]
    G --> D
    D --> H{All choices tried}
    H --> I[Return]
```""",
},

# ─── Greedy ───
"greedy": {
    "name": "Greedy",
    "time": "O(n log n)",
    "space": "O(1)",
    "approach": "Make the locally optimal choice at each step, trusting it leads to a global optimum. "
                "Greedy works when the problem has the greedy-choice property and optimal substructure.",
    "pseudocode": (
        "1. Sort or organize data for greedy ordering\n"
        "2. Initialize result\n"
        "3. For each element in greedy order:\n"
        "   a. If element satisfies constraint:\n"
        "      - Take the greedy choice\n"
        "      - Update result and state\n"
        "4. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Sort / organize for greedy order] --> B[Initialize result]
    B --> C[For each element in order]
    C --> D{Satisfies constraint?}
    D -- Yes --> E[Take greedy choice]
    E --> F[Update result and state]
    D -- No --> G[Skip element]
    F --> C
    G --> C
    C --> H[Return result]
```""",
},

"greedy_sort": {
    "name": "Greedy with Sorting",
    "time": "O(n log n)",
    "space": "O(n)",
    "approach": "Sort the input by a key criterion, then greedily process elements in sorted order. "
                "The sorting ensures the greedy choice is always optimal.",
    "pseudocode": (
        "1. Sort elements by key (start time, weight, etc.)\n"
        "2. Initialize result, tracking variables\n"
        "3. For each element in sorted order:\n"
        "   a. Apply greedy selection rule\n"
        "   b. Update result\n"
        "4. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A["Sort by key (e.g., end time)"] --> B[Initialize result]
    B --> C[For each element in sorted order]
    C --> D{Greedy condition met?}
    D -- Yes --> E[Select element]
    E --> F[Update tracking state]
    D -- No --> G[Skip]
    F --> C
    G --> C
    C --> H[Return result]
```""",
},

# ─── Prefix Sum ───
"prefix_sum": {
    "name": "Prefix Sum",
    "time": "O(n)",
    "space": "O(n)",
    "approach": "Build a prefix sum array where prefix[i] = sum of elements 0..i-1. "
                "Any subarray sum [l..r] = prefix[r+1] - prefix[l]. "
                "Combine with hash map for O(n) subarray sum queries.",
    "pseudocode": (
        "1. Build prefix sum array: prefix[0]=0, prefix[i]=prefix[i-1]+arr[i-1]\n"
        "2. Use prefix sums to answer queries:\n"
        "   - Subarray sum [l..r] = prefix[r+1] - prefix[l]\n"
        "   - Or use hash map to find prefix[j]-prefix[i] == target\n"
        "3. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A["prefix[0] = 0"] --> B[For i = 1 to n]
    B --> C["prefix[i] = prefix[i-1] + arr[i-1]"]
    C --> D{Query type?}
    D -- Range sum --> E["sum(l,r) = prefix[r+1] - prefix[l]"]
    D -- Find target --> F["Use hash map: check prefix - target"]
    E --> G[Return result]
    F --> G
```""",
},

# ─── Bit Manipulation ───
"bit_manipulation": {
    "name": "Bit Manipulation",
    "time": "O(n) or O(log n)",
    "space": "O(1)",
    "approach": "Operate on individual bits using bitwise operators (AND, OR, XOR, shift). "
                "Common tricks: x & (x-1) removes lowest set bit, x ^ x = 0, XOR all elements to find unique.",
    "pseudocode": (
        "1. Apply bitwise operations:\n"
        "   - XOR all elements to cancel paired bits\n"
        "   - Use bitmask to track state\n"
        "   - Shift and mask to extract/set individual bits\n"
        "2. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Initialize result = 0 or mask] --> B[For each element or bit position]
    B --> C[Apply bitwise operation]
    C --> D["AND / OR / XOR / SHIFT"]
    D --> E[Update result or mask]
    E --> F{More elements?}
    F -- Yes --> B
    F -- No --> G[Return result]
```""",
},

# ─── Divide and Conquer ───
"divide_conquer": {
    "name": "Divide and Conquer",
    "time": "O(n log n)",
    "space": "O(n)",
    "approach": "Split the problem into smaller subproblems, solve them recursively, "
                "and combine the results. The key is the merge/combine step.",
    "pseudocode": (
        "1. Base case: if input size <= 1, return trivial answer\n"
        "2. Divide: split input into two halves\n"
        "3. Conquer: recursively solve left and right\n"
        "4. Combine: merge solutions from left and right\n"
        "5. Return combined result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A["solve(arr, lo, hi)"] --> B{Base case: lo >= hi?}
    B -- Yes --> C[Return trivial result]
    B -- No --> D[mid = lo + hi / 2]
    D --> E["left = solve(arr, lo, mid)"]
    E --> F["right = solve(arr, mid+1, hi)"]
    F --> G["Combine(left, right)"]
    G --> H[Return combined result]
```""",
},

# ─── Sorting ───
"sorting": {
    "name": "Sorting",
    "time": "O(n log n)",
    "space": "O(n)",
    "approach": "Sort the data to enable efficient processing. After sorting, use techniques like "
                "binary search, two pointers, or linear scan to solve the problem.",
    "pseudocode": (
        "1. Sort the input array\n"
        "2. Process sorted data:\n"
        "   - Use binary search for lookups\n"
        "   - Use two pointers for pair finding\n"
        "   - Scan for adjacent patterns\n"
        "3. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Sort input array] --> B[Process sorted data]
    B --> C{Problem type?}
    C -- Search --> D[Binary search in sorted array]
    C -- Pairs --> E[Two pointers from both ends]
    C -- Adjacent --> F[Linear scan for patterns]
    D --> G[Return result]
    E --> G
    F --> G
```""",
},

# ─── Merge Sort ───
"merge_sort": {
    "name": "Merge Sort",
    "time": "O(n log n)",
    "space": "O(n)",
    "approach": "Recursively split the array into halves until single elements, then merge sorted halves. "
                "Also used to count inversions or solve order-dependent problems.",
    "pseudocode": (
        "1. If len <= 1: return arr\n"
        "2. Split into left, right halves\n"
        "3. Recursively sort left and right\n"
        "4. Merge: compare front elements, build sorted result\n"
        "5. Return merged result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A["mergeSort(arr)"] --> B{len <= 1?}
    B -- Yes --> C[Return arr]
    B -- No --> D[Split into left, right]
    D --> E["left = mergeSort(left half)"]
    E --> F["right = mergeSort(right half)"]
    F --> G["Merge left and right"]
    G --> H[Return sorted array]
```""",
},

"quickselect": {
    "name": "Quickselect",
    "time": "O(n) average",
    "space": "O(1)",
    "approach": "Find the kth element by partitioning: pick a pivot, partition elements around it, "
                "then recurse only into the partition containing kth position.",
    "pseudocode": (
        "1. Pick pivot element\n"
        "2. Partition: elements < pivot | pivot | elements > pivot\n"
        "3. If pivot is at position k: return pivot\n"
        "4. If k < pivot position: recurse left\n"
        "5. If k > pivot position: recurse right"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Pick pivot] --> B[Partition around pivot]
    B --> C{Pivot at position k?}
    C -- Yes --> D[Return pivot]
    C -- "k < pivot pos" --> E[Recurse left partition]
    C -- "k > pivot pos" --> F[Recurse right partition]
    E --> A
    F --> A
```""",
},

# ─── Math / Number Theory / Geometry ───
"math": {
    "name": "Math",
    "time": "O(n) or O(sqrt(n))",
    "space": "O(1)",
    "approach": "Apply mathematical properties, formulas, or number-theoretic concepts. "
                "Look for patterns, modular arithmetic, or closed-form solutions.",
    "pseudocode": (
        "1. Identify the mathematical pattern or formula\n"
        "2. Apply computation:\n"
        "   - Modular arithmetic for large numbers\n"
        "   - GCD/LCM for divisibility\n"
        "   - Sieve for primes\n"
        "3. Handle edge cases\n"
        "4. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Identify mathematical pattern] --> B[Apply formula or computation]
    B --> C{Edge cases?}
    C -- Yes --> D[Handle special cases]
    C -- No --> E[Compute result]
    D --> E
    E --> F[Return answer]
```""",
},

"number_theory": {
    "name": "Number Theory",
    "time": "O(sqrt(n)) or O(n log log n)",
    "space": "O(n)",
    "approach": "Apply number theory: prime checking, factorization, GCD, modular exponentiation, "
                "sieve of Eratosthenes, or Euler's totient.",
    "pseudocode": (
        "1. Apply number-theoretic algorithm:\n"
        "   - Sieve for primes up to n\n"
        "   - GCD via Euclidean algorithm\n"
        "   - Modular exponentiation\n"
        "2. Process results\n"
        "3. Return answer"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Input number n] --> B{Algorithm type?}
    B -- Primality --> C[Check divisors up to sqrt n]
    B -- GCD --> D["gcd(a,b) = gcd(b, a mod b)"]
    B -- Sieve --> E[Mark multiples of each prime]
    C --> F[Return result]
    D --> F
    E --> F
```""",
},

"geometry": {
    "name": "Geometry",
    "time": "O(n^2) or O(n log n)",
    "space": "O(n)",
    "approach": "Apply geometric formulas: distance, area, cross product, convex hull, line intersection. "
                "Handle floating-point precision carefully.",
    "pseudocode": (
        "1. Parse geometric objects (points, lines, shapes)\n"
        "2. Apply geometric operations:\n"
        "   - Distance formula\n"
        "   - Cross/dot product\n"
        "   - Area computation\n"
        "3. Handle precision and edge cases\n"
        "4. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Parse geometric objects] --> B[Apply geometric formula]
    B --> C{Computation type?}
    C -- Distance --> D["sqrt((x2-x1)^2 + (y2-y1)^2)"]
    C -- Area --> E["abs(cross product) / 2"]
    C -- Intersection --> F[Solve linear equations]
    D --> G[Return result]
    E --> G
    F --> G
```""",
},

"combinatorics": {
    "name": "Combinatorics",
    "time": "O(n) or O(n^2)",
    "space": "O(n)",
    "approach": "Count or enumerate combinations, permutations, or arrangements. "
                "Use factorials, Pascal's triangle, or inclusion-exclusion principle.",
    "pseudocode": (
        "1. Identify combinatorial structure\n"
        "2. Compute using:\n"
        "   - nCr = n! / (r! * (n-r)!)\n"
        "   - Pascal's triangle for binomial coefficients\n"
        "   - Inclusion-exclusion for overlapping sets\n"
        "3. Apply modular arithmetic if needed\n"
        "4. Return count"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Identify combinatorial formula] --> B{Method?}
    B -- "nCr" --> C["Compute n! / r!(n-r)!"]
    B -- "Pascal" --> D[Build triangle row by row]
    B -- Inclusion-Exclusion --> E["A union B = A + B - A intersect B"]
    C --> F[Return count mod 10^9+7]
    D --> F
    E --> F
```""",
},

"counting": {
    "name": "Counting",
    "time": "O(n)",
    "space": "O(n)",
    "approach": "Count occurrences of elements using a hash map, array, or counter. "
                "Process counts to determine the answer.",
    "pseudocode": (
        "1. Count frequency of each element\n"
        "2. Process frequency table:\n"
        "   - Find elements with specific counts\n"
        "   - Sort by frequency\n"
        "   - Apply conditions on counts\n"
        "3. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Count frequencies of elements] --> B[Process frequency table]
    B --> C{What to find?}
    C -- Most frequent --> D[Return max count element]
    C -- Unique --> E[Return elements with count 1]
    C -- Threshold --> F[Filter by count condition]
    D --> G[Return result]
    E --> G
    F --> G
```""",
},

# ─── Design / Simulation ───
"design": {
    "name": "Design",
    "time": "O(1) per operation",
    "space": "O(n)",
    "approach": "Design a data structure or system that supports specific operations efficiently. "
                "Choose appropriate underlying data structures (hash map, linked list, heap, etc.).",
    "pseudocode": (
        "1. Choose data structures for internal state\n"
        "2. Implement constructor: initialize state\n"
        "3. Implement each operation:\n"
        "   - Maintain invariants\n"
        "   - Optimize for target time complexity\n"
        "4. Handle edge cases"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Constructor: initialize internal state] --> B{Operation called?}
    B -- op1 --> C[Process operation 1]
    C --> D[Update internal state]
    B -- op2 --> E[Process operation 2]
    E --> D
    B -- query --> F[Read from internal state]
    D --> G[Maintain invariants]
    F --> H[Return result]
```""",
},

"design_stream": {
    "name": "Data Stream Design",
    "time": "O(log n) per operation",
    "space": "O(n)",
    "approach": "Design for streaming data: elements arrive one at a time and queries must be answered "
                "efficiently. Use sorted structures, heaps, or running aggregations.",
    "pseudocode": (
        "1. Initialize: sorted list, heap, or aggregation state\n"
        "2. addNum(val):\n"
        "   - Insert into sorted structure\n"
        "   - Update running stats\n"
        "3. query():\n"
        "   - Read from maintained state\n"
        "   - Return in O(1) or O(log n)"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Init sorted structure / heap] --> B{Operation?}
    B -- Add element --> C[Insert into structure]
    C --> D[Rebalance / update stats]
    B -- Query --> E[Read from maintained state]
    D --> F[Ready for next operation]
    E --> G[Return result]
```""",
},

"simulation": {
    "name": "Simulation",
    "time": "O(n) or O(n * k)",
    "space": "O(n)",
    "approach": "Simulate the process described in the problem step by step. "
                "Follow the rules exactly, tracking state at each step.",
    "pseudocode": (
        "1. Initialize state (grid, pointers, counters)\n"
        "2. For each step / iteration:\n"
        "   a. Apply the transformation rules\n"
        "   b. Update state\n"
        "   c. Check termination condition\n"
        "3. Return final state or result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Initialize state] --> B[Apply transformation rules]
    B --> C[Update state]
    C --> D{Termination condition?}
    D -- No --> B
    D -- Yes --> E[Return final state]
```""",
},

"randomized": {
    "name": "Randomized Algorithm",
    "time": "O(n) or varies",
    "space": "O(n)",
    "approach": "Use randomization for expected-case efficiency. "
                "Random sampling, Fisher-Yates shuffle, or reservoir sampling.",
    "pseudocode": (
        "1. Set up data structure for random access\n"
        "2. On query:\n"
        "   - Generate random index/number\n"
        "   - Return corresponding element\n"
        "3. Ensure uniform distribution"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Initialize data structure] --> B{Operation?}
    B -- Insert --> C[Add element to structure]
    B -- Random pick --> D[Generate random index]
    D --> E[Return element at index]
    C --> F[Maintain uniform access]
```""",
},

# ─── Matrix ───
"matrix": {
    "name": "Matrix / 2D Array",
    "time": "O(m * n)",
    "space": "O(1) extra",
    "approach": "Process the matrix row by row or column by column. "
                "Common patterns: rotation, spiral traversal, in-place modification, transposition.",
    "pseudocode": (
        "1. For each row i:\n"
        "   For each column j:\n"
        "     Process cell (i, j) based on neighbors or rules\n"
        "2. Handle boundary conditions\n"
        "3. Return modified matrix or computed result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A["For each row i = 0 to m-1"] --> B["For each col j = 0 to n-1"]
    B --> C["Process cell (i, j)"]
    C --> D[Apply transformation rule]
    D --> E{More columns?}
    E -- Yes --> B
    E -- No --> F{More rows?}
    F -- Yes --> A
    F -- No --> G[Return result]
```""",
},

# ─── String ───
"string": {
    "name": "String Processing",
    "time": "O(n)",
    "space": "O(n)",
    "approach": "Process the string character by character. Common techniques: "
                "two pointers, sliding window, hash map for frequencies, stack for matching.",
    "pseudocode": (
        "1. Initialize result / tracking state\n"
        "2. Iterate through string characters:\n"
        "   a. Process character based on rules\n"
        "   b. Update state (counters, pointers, stack)\n"
        "3. Build and return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Initialize state] --> B[For each character in string]
    B --> C[Process character]
    C --> D[Update state / counters]
    D --> E{More characters?}
    E -- Yes --> B
    E -- No --> F[Build result from state]
    F --> G[Return result]
```""",
},

"string_matching": {
    "name": "String Matching",
    "time": "O(n + m)",
    "space": "O(m)",
    "approach": "Find pattern occurrences in text. Use KMP, Rabin-Karp, or Z-algorithm "
                "for efficient matching beyond brute force.",
    "pseudocode": (
        "1. Preprocess pattern (build failure function / hash)\n"
        "2. Scan text with pattern:\n"
        "   a. Compare characters\n"
        "   b. On mismatch: use preprocessed data to skip\n"
        "   c. On full match: record position\n"
        "3. Return matches"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Preprocess pattern] --> B[Scan text position by position]
    B --> C{Characters match?}
    C -- Yes --> D[Advance both pointers]
    D --> E{Full pattern matched?}
    E -- Yes --> F[Record match position]
    E -- No --> B
    C -- No --> G[Use failure function to skip]
    G --> B
    F --> B
```""",
},

# ─── Segment Tree / BIT ───
"segment_tree": {
    "name": "Segment Tree",
    "time": "O(n log n) build, O(log n) query/update",
    "space": "O(n)",
    "approach": "Build a segment tree for range queries (sum, min, max) with point or range updates. "
                "Each node covers a range; queries are answered by combining relevant segments.",
    "pseudocode": (
        "1. Build segment tree from array (O(n))\n"
        "2. Query(l, r):\n"
        "   - If node range within [l,r]: return node value\n"
        "   - If no overlap: return identity\n"
        "   - Else: combine query(left_child) and query(right_child)\n"
        "3. Update(i, val): update leaf and propagate up"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Build segment tree from array] --> B{"Query or Update?"}
    B -- "Query(l,r)" --> C{Node range in query range?}
    C -- Fully inside --> D[Return node value]
    C -- No overlap --> E[Return identity]
    C -- Partial --> F[Query both children, combine]
    B -- "Update(i,v)" --> G[Update leaf node]
    G --> H[Propagate changes up to root]
```""",
},

"binary_indexed_tree": {
    "name": "Binary Indexed Tree / Fenwick Tree",
    "time": "O(n log n) build, O(log n) query/update",
    "space": "O(n)",
    "approach": "Efficient prefix sum queries and point updates using a BIT. "
                "Each index stores a partial sum determined by the lowest set bit.",
    "pseudocode": (
        "1. Initialize BIT array of size n+1\n"
        "2. Update(i, delta): add delta to index i, propagate (i += i & -i)\n"
        "3. Query(i): sum from 1 to i, traverse (i -= i & -i)\n"
        "4. Range sum(l, r) = query(r) - query(l-1)"
    ),
    "mermaid": """```mermaid
flowchart TD
    A["BIT array, size n+1"] --> B{Operation?}
    B -- "Update(i, delta)" --> C["Add delta at i"]
    C --> D["i += i AND -i (parent)"]
    D --> E{i <= n?}
    E -- Yes --> C
    B -- "Query(i)" --> F["Sum from 1 to i"]
    F --> G["Add BIT[i], i -= i AND -i"]
    G --> H{i > 0?}
    H -- Yes --> G
    H -- No --> I[Return sum]
```""",
},

# ─── Line Sweep ───
"line_sweep": {
    "name": "Line Sweep / Sweep Line",
    "time": "O(n log n)",
    "space": "O(n)",
    "approach": "Process events (interval starts/ends) in sorted order along a line. "
                "Maintain active set of intervals. Detect overlaps, compute unions, or find intersections.",
    "pseudocode": (
        "1. Create events: (time, type) for each interval start/end\n"
        "2. Sort events by time\n"
        "3. Sweep through events:\n"
        "   - On start: add to active set\n"
        "   - On end: remove from active set\n"
        "   - Track active count or intervals\n"
        "4. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Create start/end events] --> B[Sort events by time]
    B --> C[For each event]
    C --> D{Start or end?}
    D -- Start --> E[Add to active set]
    D -- End --> F[Remove from active set]
    E --> G[Update max overlap / result]
    F --> G
    G --> C
    C --> H[Return result]
```""",
},

# ─── Reservoir Sampling / Ordered Set ───
"reservoir_sampling": {
    "name": "Reservoir Sampling",
    "time": "O(n)",
    "space": "O(k)",
    "approach": "Select k random items from a stream of unknown length with uniform probability. "
                "Keep a reservoir of k items; replace items with decreasing probability.",
    "pseudocode": (
        "1. Fill reservoir with first k items\n"
        "2. For each subsequent item i (i >= k):\n"
        "   a. Generate random j in [0, i]\n"
        "   b. If j < k: replace reservoir[j] with item i\n"
        "3. Return reservoir"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Fill reservoir with first k items] --> B[For each new item i]
    B --> C["Random j in [0, i]"]
    C --> D{j < k?}
    D -- Yes --> E["reservoir[j] = item i"]
    D -- No --> F[Skip item]
    E --> B
    F --> B
```""",
},

"ordered_set": {
    "name": "Ordered Set / SortedList",
    "time": "O(n log n)",
    "space": "O(n)",
    "approach": "Maintain elements in sorted order for efficient insertion, deletion, and rank queries. "
                "Use balanced BST, skip list, or sorted container.",
    "pseudocode": (
        "1. Initialize sorted container\n"
        "2. For each operation:\n"
        "   - Insert: add element in sorted position O(log n)\n"
        "   - Delete: remove element O(log n)\n"
        "   - Query: find kth element, count, or range O(log n)\n"
        "3. Return results"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Initialize sorted container] --> B{Operation?}
    B -- Insert --> C[Add in sorted position]
    B -- Delete --> D[Remove element]
    B -- Query --> E[Find by rank or range]
    C --> F[Container stays sorted]
    D --> F
    E --> G[Return query result]
```""",
},

# ─── Catch-all ───
"array": {
    "name": "Array Processing",
    "time": "O(n)",
    "space": "O(1)",
    "approach": "Process the array with a linear scan, tracking state variables. "
                "Look for patterns: running maximum/minimum, counting, or transformations.",
    "pseudocode": (
        "1. Initialize tracking variables\n"
        "2. Iterate through array:\n"
        "   a. Update tracking state\n"
        "   b. Check conditions\n"
        "   c. Update result\n"
        "3. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Initialize variables] --> B[For each element in array]
    B --> C[Update tracking state]
    C --> D{Condition met?}
    D -- Yes --> E[Update result]
    D -- No --> F[Continue]
    E --> B
    F --> B
    B --> G[Return result]
```""",
},

"enumeration": {
    "name": "Enumeration",
    "time": "O(n^2) or O(2^n)",
    "space": "O(n)",
    "approach": "Enumerate all possible candidates or subsets and check each one. "
                "Apply pruning to skip invalid branches early.",
    "pseudocode": (
        "1. For each candidate / subset:\n"
        "   a. Check if it satisfies constraints\n"
        "   b. If valid: update best result\n"
        "   c. Prune impossible branches\n"
        "2. Return best result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Enumerate candidates] --> B[Check constraints]
    B --> C{Valid?}
    C -- Yes --> D[Update best result]
    C -- No --> E[Prune and skip]
    D --> A
    E --> A
    A --> F[Return best result]
```""",
},

"recursion": {
    "name": "Recursion",
    "time": "O(n) or O(2^n)",
    "space": "O(n)",
    "approach": "Solve the problem by breaking it into smaller instances of the same problem. "
                "Define base case(s) and recursive step. Use memoization if subproblems overlap.",
    "pseudocode": (
        "1. Base case: return known answer for smallest input\n"
        "2. Recursive step:\n"
        "   a. Break into smaller subproblem(s)\n"
        "   b. Recursively solve subproblem(s)\n"
        "   c. Combine results\n"
        "3. Return combined result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A["solve(problem)"] --> B{Base case?}
    B -- Yes --> C[Return known answer]
    B -- No --> D[Break into subproblems]
    D --> E["result1 = solve(sub1)"]
    E --> F["result2 = solve(sub2)"]
    F --> G[Combine results]
    G --> H[Return combined]
```""",
},

"general": {
    "name": "General Algorithm",
    "time": "O(n)",
    "space": "O(n)",
    "approach": "Analyze the problem constraints and apply an appropriate algorithmic technique. "
                "Read through the examples to identify the pattern.",
    "pseudocode": (
        "1. Parse and understand the input format\n"
        "2. Identify the algorithmic pattern\n"
        "3. Apply the appropriate technique\n"
        "4. Handle edge cases\n"
        "5. Return result"
    ),
    "mermaid": """```mermaid
flowchart TD
    A[Parse input] --> B[Identify pattern]
    B --> C[Apply algorithm]
    C --> D{Edge cases?}
    D -- Yes --> E[Handle special cases]
    D -- No --> F[Compute result]
    E --> F
    F --> G[Return answer]
```""",
},

}  # end PATTERNS


# ═══════════════════════════════════════════════════════════════════
# ANIMATION TEMPLATES
# ═══════════════════════════════════════════════════════════════════

ANIMATION_PATTERNS = {

"binary_search": """**Binary Search Step-by-Step:**

**Frame 1: Initial search space**
```mermaid
graph LR
    subgraph SearchSpace [Full Array]
        A0["[0]"] --- A1["[1]"] --- A2["[2]"] --- A3["[3]"] --- A4["[4]"]
    end
    L["lo=0"] --- M["mid=2"] --- H["hi=4"]
```

**Frame 2: Compare mid, narrow search**
```mermaid
graph LR
    subgraph SearchSpace [Narrowed]
        A0["[0]"] --- A1["[1]"]
    end
    L["lo=0"] --- M["mid=0"] --- H["hi=1"]
    N["Eliminated right half"]
```

**Frame 3: Found target**
```mermaid
graph LR
    subgraph SearchSpace [Found]
        A1["[1] MATCH"]
    end
    R["Return index 1"]
```
""",

"sliding_window": """**Sliding Window Step-by-Step:**

**Frame 1: Initial window (left=0, right=0)**
```mermaid
graph LR
    subgraph Window [Window]
        W0["[a]"]
    end
    O0[b] --- O1[c] --- O2[a] --- O3[b]
    S["State: {a:1}, size=1"]
```

**Frame 2: Expand right (right=2)**
```mermaid
graph LR
    subgraph Window [Window]
        W0["[a]"] --- W1["[b]"] --- W2["[c]"]
    end
    O0[a] --- O1[b]
    S["State: {a:1,b:1,c:1}, size=3"]
```

**Frame 3: Violation - shrink left**
```mermaid
graph LR
    O0[a]
    subgraph Window [Window]
        W0["[b]"] --- W1["[c]"] --- W2["[a]"]
    end
    O1[b]
    S["Removed duplicate, left++"]
```

**Frame 4: Continue expanding**
```mermaid
graph LR
    O0[a] --- O1[b]
    subgraph Window [Window]
        W0["[c]"] --- W1["[a]"] --- W2["[b]"]
    end
    S["Best window size = 3"]
```
""",

"bfs_graph": """**BFS Level-by-Level Traversal:**

**Frame 1: Start BFS from source**
```mermaid
graph TD
    S(("S dist=0"))
    A((A)) --- B((B)) --- C((C))
    S --- A
    S --- B
    Q["Queue: [S]"]
```

**Frame 2: Process level 0, enqueue neighbors**
```mermaid
graph TD
    S(("S DONE dist=0"))
    A(("A dist=1"))
    B(("B dist=1"))
    C((C))
    S --- A
    S --- B
    B --- C
    Q["Queue: [A, B]"]
```

**Frame 3: Process level 1**
```mermaid
graph TD
    S(("S DONE"))
    A(("A DONE dist=1"))
    B(("B DONE dist=1"))
    C(("C dist=2"))
    S --- A
    S --- B
    B --- C
    Q["Queue: [C]"]
```

**Frame 4: All nodes reached**
```mermaid
graph TD
    S(("S dist=0"))
    A(("A dist=1"))
    B(("B dist=1"))
    C(("C dist=2"))
    R["Max distance = 2"]
```
""",

"dfs_tree": """**DFS Tree Traversal Step-by-Step:**

**Frame 1: Start at root**
```mermaid
graph TD
    A(("1 CURRENT"))
    A --- B((2))
    A --- C((3))
    B --- D((4))
    B --- E((5))
    S["Stack: [1]"]
```

**Frame 2: Go left - visit node 2**
```mermaid
graph TD
    A(("1 visited"))
    A --- B(("2 CURRENT"))
    A --- C((3))
    B --- D((4))
    B --- E((5))
    S["Stack: [1, 2]"]
```

**Frame 3: Go left - visit node 4 (leaf)**
```mermaid
graph TD
    A(("1 visited"))
    A --- B(("2 visited"))
    A --- C((3))
    B --- D(("4 CURRENT leaf"))
    B --- E((5))
    S["Stack: [1, 2, 4] -> backtrack"]
```

**Frame 4: Backtrack, visit node 5, then node 3**
```mermaid
graph TD
    A(("1 visited"))
    A --- B(("2 visited"))
    A --- C(("3 CURRENT"))
    B --- D(("4 visited"))
    B --- E(("5 visited"))
    S["All nodes visited, DFS complete"]
```
""",

"dfs_matrix": """**DFS on Grid (Island/Flood Fill):**

**Frame 1: Find first land cell**
```mermaid
graph TD
    subgraph Grid
        R0["1  1  0"]
        R1["1  0  0"]
        R2["0  0  1"]
    end
    S["Start DFS at (0,0)"]
```

**Frame 2: DFS explores connected cells**
```mermaid
graph TD
    subgraph Grid
        R0["V  1  0"]
        R1["1  0  0"]
        R2["0  0  1"]
    end
    S["Visited (0,0), explore neighbors"]
```

**Frame 3: Mark entire island**
```mermaid
graph TD
    subgraph Grid
        R0["V  V  0"]
        R1["V  0  0"]
        R2["0  0  1"]
    end
    S["Island 1 complete, area=3"]
```

**Frame 4: Find second island**
```mermaid
graph TD
    subgraph Grid
        R0["V  V  0"]
        R1["V  0  0"]
        R2["0  0  V"]
    end
    S["Island 2 at (2,2), area=1. Total=2 islands"]
```
""",

"bfs_matrix": """**Multi-source BFS on Grid:**

**Frame 1: Enqueue all sources**
```mermaid
graph TD
    subgraph Grid
        R0["S  .  ."]
        R1[".  .  ."]
        R2[".  .  S"]
    end
    Q["Queue: [(0,0), (2,2)], dist=0"]
```

**Frame 2: Expand distance 1**
```mermaid
graph TD
    subgraph Grid
        R0["0  1  ."]
        R1["1  .  1"]
        R2[".  1  0"]
    end
    Q["Distance 1 cells processed"]
```

**Frame 3: Expand distance 2**
```mermaid
graph TD
    subgraph Grid
        R0["0  1  2"]
        R1["1  2  1"]
        R2["2  1  0"]
    end
    Q["All cells reached. Max distance = 2"]
```
""",

"dp_1d": """**1D Dynamic Programming Table Build:**

**Frame 1: Initialize base cases**
```mermaid
graph LR
    subgraph DP [DP Table]
        D0["dp[0]=base"]
        D1["dp[1]=?"]
        D2["dp[2]=?"]
        D3["dp[3]=?"]
        D4["dp[4]=?"]
    end
```

**Frame 2: Fill dp[1] from dp[0]**
```mermaid
graph LR
    subgraph DP [DP Table]
        D0["dp[0]=base"]
        D1["dp[1]=f(dp[0])"]
        D2["dp[2]=?"]
        D3["dp[3]=?"]
        D4["dp[4]=?"]
    end
    D0 -.->|"transition"| D1
```

**Frame 3: Fill remaining cells**
```mermaid
graph LR
    subgraph DP [DP Table]
        D0["dp[0]=base"]
        D1["dp[1]=f(dp[0])"]
        D2["dp[2]=f(dp[0],dp[1])"]
        D3["dp[3]=f(dp[1],dp[2])"]
        D4["dp[4]=f(dp[2],dp[3])"]
    end
    A["Answer = dp[4]"]
```
""",

"dp_2d": """**2D DP Table Build:**

**Frame 1: Initialize borders**
```mermaid
graph TD
    subgraph DP [DP Table]
        H["   j=0  j=1  j=2"]
        R0["i=0:  0    0    0"]
        R1["i=1:  0    ?    ?"]
        R2["i=2:  0    ?    ?"]
    end
```

**Frame 2: Fill cell by cell**
```mermaid
graph TD
    subgraph DP [DP Table]
        H["   j=0  j=1  j=2"]
        R0["i=0:  0    0    0"]
        R1["i=1:  0   [X]   ?"]
        R2["i=2:  0    ?    ?"]
    end
    N["dp[1][1] = f(dp[0][1], dp[1][0], dp[0][0])"]
```

**Frame 3: Table complete**
```mermaid
graph TD
    subgraph DP [DP Table]
        H["   j=0  j=1  j=2"]
        R0["i=0:  0    0    0"]
        R1["i=1:  0    X    Y"]
        R2["i=2:  0    Y    Z"]
    end
    A["Answer = dp[2][2] = Z"]
```
""",

"union_find": """**Union-Find Step-by-Step:**

**Frame 1: Initial - each node is own parent**
```mermaid
graph TD
    N1((1)) --- P1["parent=1"]
    N2((2)) --- P2["parent=2"]
    N3((3)) --- P3["parent=3"]
    N4((4)) --- P4["parent=4"]
```

**Frame 2: Union(1,2) - merge components**
```mermaid
graph TD
    N1((1))
    N2((2)) -->|parent| N1
    N3((3))
    N4((4))
    E["find(1)=1, find(2)=2 -> merge"]
```

**Frame 3: Union(3,4) then Union(2,3)**
```mermaid
graph TD
    N1((1))
    N2((2)) -->|parent| N1
    N3((3)) -->|parent| N1
    N4((4)) -->|parent| N3
    E["All nodes in one component"]
```

**Frame 4: Path compression on find(4)**
```mermaid
graph TD
    N1((1))
    N2((2)) -->|parent| N1
    N3((3)) -->|parent| N1
    N4((4)) -->|parent| N1
    E["After find(4): path compressed to root"]
```
""",

"topological_sort": """**Topological Sort (Kahn's Algorithm):**

**Frame 1: Compute in-degrees**
```mermaid
graph LR
    A(("A in=0")) --> B(("B in=1"))
    A --> C(("C in=1"))
    B --> D(("D in=2"))
    C --> D
    Q["Queue: [A] (in-degree 0)"]
```

**Frame 2: Process A, reduce neighbors**
```mermaid
graph LR
    A(("A DONE"))
    B(("B in=0"))
    C(("C in=0"))
    D(("D in=2"))
    Q["Order: [A], Queue: [B, C]"]
```

**Frame 3: Process B and C**
```mermaid
graph LR
    A(("A DONE"))
    B(("B DONE"))
    C(("C DONE"))
    D(("D in=0"))
    Q["Order: [A,B,C], Queue: [D]"]
```

**Frame 4: Complete**
```mermaid
graph LR
    A(("A")) --> B(("B")) --> D(("D"))
    A --> C(("C")) --> D
    R["Topological Order: A, B, C, D"]
```
""",

"monotonic_stack": """**Monotonic Stack (Next Greater Element):**

**Frame 1: Process first elements**
```mermaid
graph LR
    subgraph Array
        A0["4"] --- A1["2"] --- A2["1"] --- A3["3"] --- A4["5"]
    end
    S["Stack: [4]  Result: [-,-,-,-,-]"]
```

**Frame 2: Push smaller elements**
```mermaid
graph LR
    subgraph Array
        A0["4"] --- A1["2"] --- A2["1"] --- A3["3"] --- A4["5"]
    end
    S["Stack: [4,2,1]  Result: [-,-,-,-,-]"]
```

**Frame 3: Element 3 pops 1 and 2**
```mermaid
graph LR
    subgraph Array
        A0["4"] --- A1["2"] --- A2["1"] --- A3["3"] --- A4["5"]
    end
    S["Pop 1->NGE=3, Pop 2->NGE=3"]
    R["Stack: [4,3]  Result: [-,3,3,-,-]"]
```

**Frame 4: Element 5 pops all**
```mermaid
graph LR
    subgraph Array
        A0["4"] --- A1["2"] --- A2["1"] --- A3["3"] --- A4["5"]
    end
    S["Pop 3->NGE=5, Pop 4->NGE=5"]
    R["Stack: [5]  Result: [5,3,3,5,-]"]
```
""",

"backtracking": """**Backtracking Decision Tree:**

**Frame 1: Root - start with empty path**
```mermaid
graph TD
    R["[] choices: 1,2,3"]
    R --- A["[1]"]
    R --- B["[2]"]
    R --- C["[3]"]
```

**Frame 2: Explore branch [1]**
```mermaid
graph TD
    R["[]"]
    R --- A["[1]"]
    A --- A1["[1,2]"]
    A --- A2["[1,3]"]
    A1 --- A1a["[1,2,3] SOLUTION"]
    R --- B["[2] ..."]
    R --- C["[3] ..."]
```

**Frame 3: Backtrack, explore [2]**
```mermaid
graph TD
    R["[]"]
    R --- A["[1] done"]
    R --- B["[2]"]
    B --- B1["[2,1]"]
    B --- B2["[2,3]"]
    B1 --- B1a["[2,1,3] SOLUTION"]
    R --- C["[3] ..."]
```

**Frame 4: All solutions found**
```mermaid
graph TD
    R["Complete: 6 permutations found"]
    R --- S1["[1,2,3]"]
    R --- S2["[1,3,2]"]
    R --- S3["[2,1,3] ..."]
```
""",

"linked_list": """**Linked List Operation (Reverse):**

**Frame 1: Initial list**
```mermaid
graph LR
    A["1"] --> B["2"] --> C["3"] --> D["4"] --> N[null]
    P["prev=null, curr=1"]
```

**Frame 2: Reverse first link**
```mermaid
graph LR
    A["1"] --> N[null]
    B["2"] --> C["3"] --> D["4"]
    P["prev=1, curr=2"]
```

**Frame 3: Reverse second link**
```mermaid
graph LR
    B["2"] --> A["1"] --> N[null]
    C["3"] --> D["4"]
    P["prev=2, curr=3"]
```

**Frame 4: Fully reversed**
```mermaid
graph LR
    D["4"] --> C["3"] --> B["2"] --> A["1"] --> N[null]
    P["New head = 4"]
```
""",

"heap": """**Heap Operations (Min-Heap):**

**Frame 1: Initial heap**
```mermaid
graph TD
    A((3))
    A --- B((5))
    A --- C((7))
    B --- D((8))
    B --- E((10))
    S["Heap: [3, 5, 7, 8, 10]"]
```

**Frame 2: Insert 2 - bubble up**
```mermaid
graph TD
    A((2))
    A --- B((5))
    A --- C((3))
    B --- D((8))
    B --- E((10))
    C --- F((7))
    S["Insert 2: swapped up to root"]
```

**Frame 3: Pop minimum (2) - heapify down**
```mermaid
graph TD
    A((3))
    A --- B((5))
    A --- C((7))
    B --- D((8))
    B --- E((10))
    S["Popped 2. Root=3 after heapify"]
```
""",

"trie": """**Trie Insert and Search:**

**Frame 1: Empty trie**
```mermaid
graph TD
    R((root))
    S["Insert: 'app', 'apple'"]
```

**Frame 2: Insert 'app'**
```mermaid
graph TD
    R((root)) --> A((a))
    A --> P1((p))
    P1 --> P2(("p END"))
    S["'app' inserted, marked as end"]
```

**Frame 3: Insert 'apple'**
```mermaid
graph TD
    R((root)) --> A((a))
    A --> P1((p))
    P1 --> P2(("p END"))
    P2 --> L((l))
    L --> E(("e END"))
    S["'apple' extends existing path"]
```

**Frame 4: Search 'app' = True, 'ap' = False**
```mermaid
graph TD
    R((root)) --> A((a))
    A --> P1((p))
    P1 --> P2(("p END"))
    P2 --> L((l))
    L --> E(("e END"))
    S1["search('app'): follow a->p->p, is_end=True -> FOUND"]
    S2["search('ap'): follow a->p, is_end=False -> NOT FOUND"]
```
""",

"shortest_path": """**Dijkstra's Algorithm Step-by-Step:**

**Frame 1: Initialize distances**
```mermaid
graph LR
    S(("S d=0")) -->|4| A(("A d=INF"))
    S -->|1| B(("B d=INF"))
    A -->|1| C(("C d=INF"))
    B -->|2| A
    B -->|5| C
```

**Frame 2: Process S (d=0)**
```mermaid
graph LR
    S(("S d=0 DONE")) -->|4| A(("A d=4"))
    S -->|1| B(("B d=1"))
    A -->|1| C(("C d=INF"))
    B -->|2| A
    B -->|5| C
    Q["Heap: [(1,B), (4,A)]"]
```

**Frame 3: Process B (d=1), update A**
```mermaid
graph LR
    S(("S DONE")) -->|4| A(("A d=3"))
    S -->|1| B(("B d=1 DONE"))
    A -->|1| C(("C d=INF"))
    B -->|2| A
    B -->|5| C
    Q["A updated: 1+2=3 < 4"]
```

**Frame 4: Process A (d=3), reach C**
```mermaid
graph LR
    S(("S d=0")) -->|4| A(("A d=3 DONE"))
    S -->|1| B(("B d=1 DONE"))
    A -->|1| C(("C d=4 DONE"))
    B -->|2| A
    B -->|5| C
    R["Shortest paths: S=0, B=1, A=3, C=4"]
```
""",

"two_pointer": """**Two Pointer Convergence:**

**Frame 1: Initialize pointers**
```mermaid
graph LR
    L["L=0"] --- A0["1"] --- A1["3"] --- A2["5"] --- A3["7"] --- A4["9"] --- R["R=4"]
    S["Target sum = 10"]
```

**Frame 2: Sum = 1+9 = 10, found!**
```mermaid
graph LR
    L["L=0 -> 1"] --- A1["3"] --- A2["5"] --- A3["7"] --- R["R=4 -> 9"]
    S["1 + 9 = 10 = Target. FOUND!"]
```
""",

}  # end ANIMATION_PATTERNS

# Set of patterns that get animations
ANIMATED_PATTERNS = set(ANIMATION_PATTERNS.keys())


# ═══════════════════════════════════════════════════════════════════
# PUBLIC API FUNCTIONS
# ═══════════════════════════════════════════════════════════════════

def auto_classify(tags):
    """Classify a problem into a pattern name based on its tags.
    Returns the pattern key (e.g., 'sliding_window')."""
    return classify_pattern(tags)


def auto_pattern_name(tags):
    """Get the human-readable pattern name."""
    pattern = classify_pattern(tags)
    return PATTERNS.get(pattern, PATTERNS["general"])["name"]


def auto_generate_mermaid(tags):
    """Generate a mermaid flowchart for the problem based on its tags."""
    pattern = classify_pattern(tags)
    return PATTERNS.get(pattern, PATTERNS["general"])["mermaid"]


def auto_generate_approach(tags, title=""):
    """Generate approach explanation text."""
    pattern = classify_pattern(tags)
    return PATTERNS.get(pattern, PATTERNS["general"])["approach"]


def auto_generate_pseudocode(tags):
    """Generate pseudocode."""
    pattern = classify_pattern(tags)
    return PATTERNS.get(pattern, PATTERNS["general"])["pseudocode"]


def auto_complexity_time(tags):
    """Get time complexity for the pattern."""
    pattern = classify_pattern(tags)
    return PATTERNS.get(pattern, PATTERNS["general"])["time"]


def auto_complexity_space(tags):
    """Get space complexity for the pattern."""
    pattern = classify_pattern(tags)
    return PATTERNS.get(pattern, PATTERNS["general"])["space"]


def auto_generate_animation(tags):
    """Generate multi-frame animation if the pattern supports it."""
    pattern = classify_pattern(tags)
    return ANIMATION_PATTERNS.get(pattern, "")


def auto_generate_all(tags, title=""):
    """Generate all auto-content for a problem at once.
    Returns a dict with all fields."""
    pattern = classify_pattern(tags)
    p = PATTERNS.get(pattern, PATTERNS["general"])
    return {
        "pattern": p["name"],
        "time": p["time"],
        "space": p["space"],
        "approach": p["approach"],
        "pseudocode": p["pseudocode"],
        "mermaid": p["mermaid"],
        "animation_frames": ANIMATION_PATTERNS.get(pattern, ""),
    }
