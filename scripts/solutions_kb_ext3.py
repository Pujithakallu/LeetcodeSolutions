#!/usr/bin/env python3
"""
solutions_kb_ext3.py
====================
Additional hand-crafted solutions for popular LeetCode problems (batch 3).
Focus on problems with visual animations and mermaid diagrams.
"""

SOLUTIONS_KB_EXT3 = {

# ═══════════════════════════════════════════
# Problems with Animation Frames (complex visual problems)
# ═══════════════════════════════════════════

# --- 743: Network Delay Time (Dijkstra animation) ---
# Already in ext2, adding animation
743: {"animation_frames": """**Dijkstra's Algorithm Step-by-Step:**

**Frame 1: Initial State**
```mermaid
graph LR
    1(("1<br/>dist=INF"))
    2(("2 START<br/>dist=0"))
    3(("3<br/>dist=INF"))
    4(("4<br/>dist=INF"))
    2 -->|1| 1
    2 -->|1| 3
    3 -->|1| 4
```

**Frame 2: Process node 2 (dist=0)**
```mermaid
graph LR
    1(("1<br/>dist=1"))
    2(("2 DONE<br/>dist=0"))
    3(("3<br/>dist=1"))
    4(("4<br/>dist=INF"))
    2 -.->|1| 1
    2 -.->|1| 3
    3 -->|1| 4
```

**Frame 3: Process node 1 and 3 (dist=1)**
```mermaid
graph LR
    1(("1 DONE<br/>dist=1"))
    2(("2 DONE<br/>dist=0"))
    3(("3 DONE<br/>dist=1"))
    4(("4<br/>dist=2"))
    2 -.->|1| 1
    2 -.->|1| 3
    3 -.->|1| 4
```

**Frame 4: All processed - Answer = max(0,1,1,2) = 2**
```mermaid
graph LR
    1(("1 DONE<br/>dist=1"))
    2(("2 DONE<br/>dist=0"))
    3(("3 DONE<br/>dist=1"))
    4(("4 DONE<br/>dist=2"))
```
"""},

# --- 994: Rotting Oranges (BFS animation) ---
994: {"animation_frames": """**Multi-source BFS Step-by-Step:**

**Frame 1: Initial Grid (2=rotten, 1=fresh, 0=empty)**
```mermaid
graph TD
    subgraph Grid
        R1["[2] [1] [1]"]
        R2["[1] [1] [0]"]
        R3["[0] [1] [1]"]
    end
    Q["Queue: (0,0)"]
```

**Frame 2: Minute 1 - Spread from (0,0)**
```mermaid
graph TD
    subgraph Grid
        R1["[2] [2] [1]"]
        R2["[2] [1] [0]"]
        R3["[0] [1] [1]"]
    end
    Q["Queue: (0,1),(1,0) | fresh=4"]
```

**Frame 3: Minute 2 - Spread from (0,1) and (1,0)**
```mermaid
graph TD
    subgraph Grid
        R1["[2] [2] [2]"]
        R2["[2] [2] [0]"]
        R3["[0] [1] [1]"]
    end
    Q["Queue: (0,2),(1,1) | fresh=2"]
```

**Frame 4: Minute 3 - All reachable oranges rotten**
```mermaid
graph TD
    subgraph Grid
        R1["[2] [2] [2]"]
        R2["[2] [2] [0]"]
        R3["[0] [2] [2]"]
    end
    Q["Queue: empty | fresh=0 | Answer: 4"]
```
"""},

# --- 1143: LCS DP Table Animation ---
1143: {"animation_frames": """**LCS DP Table Build:**

**Input:** text1 = "abcde", text2 = "ace"

**Frame 1: Initialize DP table**
```mermaid
graph TD
    subgraph "DP Table"
        H["  | '' | a | c | e"]
        R0["''|  0 | 0 | 0 | 0"]
        R1["a |  0 | ? | ? | ?"]
        R2["b |  0 | ? | ? | ?"]
    end
```

**Frame 2: Fill row 'a' - match at (a,a)**
```mermaid
graph TD
    subgraph "DP Table"
        H["  | '' | a | c | e"]
        R0["''|  0 | 0 | 0 | 0"]
        R1["a |  0 | 1 | 1 | 1"]
        R2["b |  0 | 1 | 1 | 1"]
    end
```

**Frame 3: Fill rows c, d, e**
```mermaid
graph TD
    subgraph "DP Table"
        H["  | '' | a | c | e"]
        R0["''|  0 | 0 | 0 | 0"]
        R1["a |  0 | 1 | 1 | 1"]
        R2["b |  0 | 1 | 1 | 1"]
        R3["c |  0 | 1 | 2 | 2"]
        R4["d |  0 | 1 | 2 | 2"]
        R5["e |  0 | 1 | 2 | 3"]
    end
    A["Answer: dp[5][3] = 3, LCS = ace"]
```
"""},

# --- 560: Subarray Sum Equals K (Prefix Sum animation) ---
560: {"animation_frames": """**Prefix Sum + Hash Map Step-by-Step:**

**Input:** nums = [1, 1, 1], k = 2

**Frame 1: Initialize**
```mermaid
graph LR
    subgraph State
        PS["prefix_sum = 0"]
        M["map = {0: 1}"]
        C["count = 0"]
    end
```

**Frame 2: Process nums[0]=1**
```mermaid
graph LR
    subgraph State
        PS["prefix_sum = 1"]
        M["map = {0:1, 1:1}"]
        C["count += map[1-2] = map[-1] = 0"]
    end
```

**Frame 3: Process nums[1]=1**
```mermaid
graph LR
    subgraph State
        PS["prefix_sum = 2"]
        M["map = {0:1, 1:1, 2:1}"]
        C["count += map[2-2] = map[0] = 1 -> count=1"]
    end
```

**Frame 4: Process nums[2]=1**
```mermaid
graph LR
    subgraph State
        PS["prefix_sum = 3"]
        M["map = {0:1, 1:1, 2:1, 3:1}"]
        C["count += map[3-2] = map[1] = 1 -> count=2"]
    end
    A["Answer: 2 subarrays sum to k=2"]
```
"""},

# --- 739: Daily Temperatures (Monotonic Stack animation) ---
739: {"animation_frames": """**Monotonic Stack Step-by-Step:**

**Input:** temps = [73, 74, 75, 71, 69, 72, 76, 73]

**Frame 1: Process 73 (i=0)**
```mermaid
graph LR
    S["Stack: [0]"] --> R["Result: [0,0,0,0,0,0,0,0]"]
```

**Frame 2: Process 74 (i=1) - 74 > 73, pop 0**
```mermaid
graph LR
    S["Stack: [1]"] --> R["Result: [1,0,0,0,0,0,0,0]"]
    N["74>73: result[0]=1-0=1"]
```

**Frame 3: Process 75 (i=2) - 75 > 74, pop 1**
```mermaid
graph LR
    S["Stack: [2]"] --> R["Result: [1,1,0,0,0,0,0,0]"]
```

**Frame 4: Process 71,69 (i=3,4) - push both**
```mermaid
graph LR
    S["Stack: [2,3,4]"] --> R["Result: [1,1,0,0,0,0,0,0]"]
```

**Frame 5: Process 72 (i=5) - pop 69,71**
```mermaid
graph LR
    S["Stack: [2,5]"] --> R["Result: [1,1,0,2,1,0,0,0]"]
```

**Frame 6: Process 76 (i=6) - pop all**
```mermaid
graph LR
    S["Stack: [6]"] --> R["Result: [1,1,4,2,1,1,0,0]"]
    A["Answer: [1,1,4,2,1,1,0,0]"]
```
"""},

# --- 684: Union-Find animation ---
684: {"animation_frames": """**Union-Find Step-by-Step:**

**Edges:** [[1,2], [1,3], [2,3]]

**Frame 1: Initial - each node is own parent**
```mermaid
graph TD
    1((1)) --> 1p["parent=1"]
    2((2)) --> 2p["parent=2"]
    3((3)) --> 3p["parent=3"]
```

**Frame 2: Process edge [1,2] - union(1,2)**
```mermaid
graph TD
    1((1))
    2((2)) -->|parent| 1
    3((3))
    E["find(1)=1, find(2)=2 -> different, union OK"]
```

**Frame 3: Process edge [1,3] - union(1,3)**
```mermaid
graph TD
    1((1))
    2((2)) -->|parent| 1
    3((3)) -->|parent| 1
    E["find(1)=1, find(3)=3 -> different, union OK"]
```

**Frame 4: Process edge [2,3] - CYCLE DETECTED!**
```mermaid
graph TD
    1((1))
    2((2)) -->|parent| 1
    3((3)) -->|parent| 1
    E["find(2)=1, find(3)=1 -> SAME! Return [2,3]"]
    style E fill:#ff6666
```
"""},

# --- 875: Koko Eating Bananas (Binary Search on Answer) ---
875: {"animation_frames": """**Binary Search on Answer:**

**Input:** piles = [3, 6, 7, 11], h = 8

**Frame 1: Initial search space**
```mermaid
graph LR
    L["lo=1"] --- M["mid=6"] --- H["hi=11"]
    C["At speed 6: hours = 1+1+2+2 = 6 <= 8 -> go left"]
```

**Frame 2: Narrow to [1, 6]**
```mermaid
graph LR
    L["lo=1"] --- M["mid=3"] --- H["hi=6"]
    C["At speed 3: hours = 1+2+3+4 = 10 > 8 -> go right"]
```

**Frame 3: Narrow to [4, 6]**
```mermaid
graph LR
    L["lo=4"] --- M["mid=5"] --- H["hi=6"]
    C["At speed 5: hours = 1+2+2+3 = 8 <= 8 -> go left"]
```

**Frame 4: Narrow to [4, 5]**
```mermaid
graph LR
    L["lo=4"] --- M["mid=4"] --- H["hi=5"]
    C["At speed 4: hours = 1+2+2+3 = 8 <= 8 -> go left"]
```

**Frame 5: lo=4, hi=4 -> Answer = 4**
```mermaid
graph LR
    A["Minimum eating speed k = 4"]
    V["Verify: ceil(3/4)+ceil(6/4)+ceil(7/4)+ceil(11/4) = 1+2+2+3 = 8 <= 8"]
```
"""},

# --- 1235: Job Scheduling DP ---
1235: {"animation_frames": """**Job Scheduling DP:**

**Jobs sorted by end time:**

| Job | Start | End | Profit |
|-----|-------|-----|--------|
| A   | 1     | 2   | 50     |
| B   | 3     | 5   | 40     |
| C   | 1     | 5   | 60     |
| D   | 6     | 8   | 70     |

**Frame 1: dp[0] = 0 (no jobs)**
```mermaid
graph LR
    D["dp = [0, ?, ?, ?, ?]"]
```

**Frame 2: Job A (1-2, profit 50)**
```mermaid
graph LR
    D["dp = [0, 50, ?, ?, ?]"]
    C["dp[1] = max(dp[0]=0, dp[0]+50=50) = 50"]
```

**Frame 3: Job B (3-5, profit 40)**
```mermaid
graph LR
    D["dp = [0, 50, 90, ?, ?]"]
    C["Binary search: latest non-overlapping = job A"]
    C2["dp[2] = max(dp[1]=50, dp[1]+40=90) = 90"]
```

**Frame 4: Job C (1-5, profit 60) and Job D (6-8, profit 70)**
```mermaid
graph LR
    D["dp = [0, 50, 90, 90, 160]"]
    C["Job C: max(dp[2]=90, dp[0]+60=60) = 90"]
    C2["Job D: max(dp[3]=90, dp[2]+70=160) = 160"]
    A["Answer: 160 (take jobs A, B, D)"]
```
"""},

# ═══════════════════════════════════════════
# More Essential Problems (no animation, just solutions)
# ═══════════════════════════════════════════

503: {"code": """class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [-1] * n
        stack = []
        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                result[stack.pop()] = nums[i % n]
            if i < n:
                stack.append(i)
        return result""", "pattern": "Monotonic Stack (Circular)", "time": "O(n)", "space": "O(n)", "approach": "Iterate twice through array (circular). Monotonic stack to find next greater element."},

513: {"code": """from collections import deque

class Solution:
    def findBottomLeftValue(self, root) -> int:
        queue = deque([root])
        result = root.val
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if i == 0:
                    result = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result""", "pattern": "BFS / Tree", "time": "O(n)", "space": "O(n)", "approach": "Level-order traversal. Track first node of each level. Last level's first node is answer."},

530: {"code": """class Solution:
    def getMinimumDifference(self, root) -> int:
        self.prev = None
        self.min_diff = float('inf')
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)
        inorder(root)
        return self.min_diff""", "pattern": "BST / Inorder Traversal", "time": "O(n)", "space": "O(h)", "approach": "Inorder traversal gives sorted order. Min difference is between adjacent values."},

538: {"code": """class Solution:
    def convertBST(self, root):
        self.total = 0
        def traverse(node):
            if not node:
                return
            traverse(node.right)
            self.total += node.val
            node.val = self.total
            traverse(node.left)
        traverse(root)
        return root""", "pattern": "BST / Reverse Inorder", "time": "O(n)", "space": "O(h)", "approach": "Reverse inorder (right-root-left) accumulates running sum."},

605: {"code": """class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left = (i == 0) or (flowerbed[i-1] == 0)
                right = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
                if left and right:
                    flowerbed[i] = 1
                    count += 1
        return count >= n""", "pattern": "Greedy", "time": "O(n)", "space": "O(1)", "approach": "Greedily plant flower if both neighbors are empty."},

643: {"code": """class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        return max_sum / k""", "pattern": "Sliding Window (Fixed)", "time": "O(n)", "space": "O(1)", "approach": "Fixed-size sliding window of size k. Track maximum window sum."},

724: {"code": """class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == total - left_sum - num:
                return i
            left_sum += num
        return -1""", "pattern": "Prefix Sum", "time": "O(n)", "space": "O(1)", "approach": "Pivot index where left_sum == total - left_sum - nums[i]."},

841: {"code": """class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set([0])
        stack = [0]
        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)
        return len(visited) == len(rooms)""", "pattern": "DFS / Graph", "time": "O(V + E)", "space": "O(V)", "approach": "DFS/BFS from room 0. Check if all rooms visited."},

933: {"code": """from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)""", "pattern": "Queue / Design", "time": "O(1) amortized", "space": "O(n)", "approach": "Queue of timestamps. Pop timestamps older than t-3000. Return queue size."},

1004: {"code": """class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zeros = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len""", "pattern": "Sliding Window", "time": "O(n)", "space": "O(1)", "approach": "Sliding window: track zeros count. Shrink window when zeros > k."},

1456: {"code": """class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        count = sum(1 for c in s[:k] if c in vowels)
        max_count = count
        for i in range(k, len(s)):
            count += (s[i] in vowels) - (s[i-k] in vowels)
            max_count = max(max_count, count)
        return max_count""", "pattern": "Sliding Window (Fixed)", "time": "O(n)", "space": "O(1)", "approach": "Fixed sliding window of size k. Track vowel count."},

1493: {"code": """class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        zeros = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left)
        return max_len""", "pattern": "Sliding Window", "time": "O(n)", "space": "O(1)", "approach": "Sliding window with at most 1 zero. Return max window size - 1 (must delete one)."},

1657: {"code": """class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter
        if len(word1) != len(word2):
            return False
        c1, c2 = Counter(word1), Counter(word2)
        return set(c1.keys()) == set(c2.keys()) and sorted(c1.values()) == sorted(c2.values())""", "pattern": "Hash Map / String", "time": "O(n)", "space": "O(1)", "approach": "Two strings are close if they have same character sets and same sorted frequency lists."},

1679: {"code": """class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        from collections import Counter
        count = Counter(nums)
        result = 0
        for num in list(count.keys()):
            comp = k - num
            if comp == num:
                result += count[num] // 2
            elif comp in count:
                pairs = min(count[num], count[comp])
                result += pairs
                count[num] -= pairs
                count[comp] -= pairs
        return result""", "pattern": "Hash Map / Two Sum Variant", "time": "O(n)", "space": "O(n)", "approach": "Count frequencies. For each number, find complement k-num. Count pairs."},

2352: {"code": """class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        from collections import Counter
        rows = Counter(tuple(row) for row in grid)
        count = 0
        n = len(grid)
        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))
            count += rows[col]
        return count""", "pattern": "Hash Map / Matrix", "time": "O(n^2)", "space": "O(n^2)", "approach": "Hash all rows. For each column, check if it matches any row."},

}

# Set defaults
_DEFAULT_KEYS = {"code": "", "pattern": "", "time": "", "space": "", "approach": "", "pseudocode": "", "mermaid": "", "walkthrough": "", "animation_frames": ""}
for pid in list(SOLUTIONS_KB_EXT3.keys()):
    if not isinstance(pid, int):
        del SOLUTIONS_KB_EXT3[pid]
        continue
    for key, default in _DEFAULT_KEYS.items():
        SOLUTIONS_KB_EXT3[pid].setdefault(key, default)
