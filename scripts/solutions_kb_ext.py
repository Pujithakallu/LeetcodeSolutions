#!/usr/bin/env python3
"""
solutions_kb_ext.py
===================
Extended knowledge base for LeetCode problems 501-2500.
Contains hand-crafted optimal solutions for key/popular problems.
"""

SOLUTIONS_KB_EXT = {

# ═══════════════════════════════════════════
# 501-600: Core Problems
# ═══════════════════════════════════════════

509: {"code": """class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b""", "pattern": "Dynamic Programming (Fibonacci)", "time": "O(n)", "space": "O(1)", "approach": "Iterative Fibonacci with two variables.", "mermaid": ""},

518: {"code": """class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]""", "pattern": "Dynamic Programming (Unbounded Knapsack)", "time": "O(n * amount)", "space": "O(amount)", "approach": "**Unbounded Knapsack:** dp[x] = number of ways to make amount x. Process coins in outer loop to avoid counting permutations.", "mermaid": """```mermaid
flowchart TD
    A["dp[0]=1, rest=0"] --> B[For each coin]
    B --> C[For x from coin to amount]
    C --> D["dp[x] += dp[x-coin]"]
    D --> C
    C --> B
```"""},

543: {"code": """class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.diameter = 0
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        depth(root)
        return self.diameter""", "pattern": "Tree / DFS", "time": "O(n)", "space": "O(h)", "approach": "At each node, diameter through it = left_depth + right_depth. Track global max.", "mermaid": """```mermaid
flowchart TD
    A["depth(node)"] --> B{null?}
    B -- Yes --> C[Return 0]
    B -- No --> D[left = depth left child]
    D --> E[right = depth right child]
    E --> F[Update diameter = max diameter, left+right]
    F --> G[Return 1 + max left,right]
```"""},

560: {"code": """from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        for num in nums:
            prefix_sum += num
            count += prefix_counts[prefix_sum - k]
            prefix_counts[prefix_sum] += 1
        return count""", "pattern": "Prefix Sum + Hash Map", "time": "O(n)", "space": "O(n)", "approach": "**Key Insight:** If prefix[j] - prefix[i] = k, subarray (i,j] sums to k. Count how many times prefix_sum - k has appeared.", "mermaid": """```mermaid
flowchart TD
    A[prefix_sum=0, map={0:1}] --> B[For each num]
    B --> C[prefix_sum += num]
    C --> D[count += map prefix_sum - k]
    D --> E[map prefix_sum += 1]
    E --> B
```"""},

567: {"code": """from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = Counter(s1)
        window = Counter(s2[:len(s1)])
        if window == s1_count:
            return True
        for i in range(len(s1), len(s2)):
            window[s2[i]] += 1
            left = s2[i - len(s1)]
            window[left] -= 1
            if window[left] == 0:
                del window[left]
            if window == s1_count:
                return True
        return False""", "pattern": "Sliding Window", "time": "O(n)", "space": "O(1)", "approach": "Fixed-size sliding window with character frequency comparison.", "mermaid": ""},

572: {"code": """class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        if not root:
            return False
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSame(p.left, q.left) and self.isSame(p.right, q.right)""", "pattern": "Tree / DFS", "time": "O(m*n)", "space": "O(h)", "approach": "Check each node in root tree as potential match for subRoot.", "mermaid": ""},

# ═══════════════════════════════════════════
# 601-700: Key Problems
# ═══════════════════════════════════════════

617: {"code": """class Solution:
    def mergeTrees(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1""", "pattern": "Tree / DFS", "time": "O(n)", "space": "O(h)", "approach": "Recursively merge: add values, recurse on left/right children.", "mermaid": ""},

621: {"code": """from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = Counter(tasks)
        max_count = max(counts.values())
        num_max = sum(1 for v in counts.values() if v == max_count)
        result = (max_count - 1) * (n + 1) + num_max
        return max(result, len(tasks))""", "pattern": "Greedy / Math", "time": "O(n)", "space": "O(1)", "approach": "**Key Insight:** Most frequent task defines the frame. Result = (max_count-1)*(n+1) + num_tasks_with_max_count.", "mermaid": """```mermaid
flowchart TD
    A[Count task frequencies] --> B[Find max frequency]
    B --> C[Count tasks with max freq]
    C --> D["result = (max-1)*(n+1) + num_max"]
    D --> E["Return max(result, total_tasks)"]
```"""},

647: {"code": """class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            for l, r in [(i, i), (i, i + 1)]:
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
        return count""", "pattern": "Expand Around Center", "time": "O(n^2)", "space": "O(1)", "approach": "Expand around each center (odd and even). Count each palindrome found.", "mermaid": ""},

# ═══════════════════════════════════════════
# 701-800
# ═══════════════════════════════════════════

703: {"code": """import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]""", "pattern": "Heap / Design", "time": "O(log k) per add", "space": "O(k)", "approach": "Maintain a min-heap of size k. The top is always the kth largest.", "mermaid": ""},

704: {"code": """class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1""", "pattern": "Binary Search", "time": "O(log n)", "space": "O(1)", "approach": "Classic binary search.", "mermaid": """```mermaid
flowchart TD
    A[lo=0, hi=n-1] --> B{lo <= hi?}
    B -- Yes --> C[mid = lo+hi / 2]
    C --> D{nums_mid == target?}
    D -- Yes --> E[Return mid]
    D -- No --> F{nums_mid < target?}
    F -- Yes --> G[lo = mid+1]
    F -- No --> H[hi = mid-1]
    G --> B
    H --> B
    B -- No --> I[Return -1]
```"""},

733: {"code": """class Solution:
    def floodFill(self, image, sr, sc, color):
        orig = image[sr][sc]
        if orig == color:
            return image
        m, n = len(image), len(image[0])
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != orig:
                return
            image[r][c] = color
            dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)
        dfs(sr, sc)
        return image""", "pattern": "DFS / Graph", "time": "O(m*n)", "space": "O(m*n)", "approach": "DFS from starting pixel, changing all connected same-color pixels.", "mermaid": ""},

739: {"code": """class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)
        return result""", "pattern": "Monotonic Stack", "time": "O(n)", "space": "O(n)", "approach": "**Monotonic decreasing stack** of indices. When a warmer day appears, pop and record the distance.", "mermaid": """```mermaid
flowchart TD
    A[For each day i] --> B{Stack top cooler than today?}
    B -- Yes --> C[Pop, record distance i - top]
    C --> B
    B -- No --> D[Push i]
    D --> A
```"""},

746: {"code": """class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])""", "pattern": "Dynamic Programming", "time": "O(n)", "space": "O(1)", "approach": "DP: cost[i] += min of previous two steps. Return min of last two.", "mermaid": ""},

763: {"code": """class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {c: i for i, c in enumerate(s)}
        result = []
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                result.append(end - start + 1)
                start = end + 1
        return result""", "pattern": "Greedy / Two Pointers", "time": "O(n)", "space": "O(1)", "approach": "Track last occurrence of each char. Extend partition end to include all occurrences. Cut when i == end.", "mermaid": """```mermaid
flowchart TD
    A[Record last index of each char] --> B[start=0, end=0]
    B --> C[For each i, char]
    C --> D["end = max(end, last[char])"]
    D --> E{i == end?}
    E -- Yes --> F[Record partition, start = end+1]
    E -- No --> C
    F --> C
```"""},

# ═══════════════════════════════════════════
# 801-1000
# ═══════════════════════════════════════════

846: {"code": """from collections import Counter

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        for card in sorted(count):
            if count[card] > 0:
                need = count[card]
                for i in range(groupSize):
                    if count[card + i] < need:
                        return False
                    count[card + i] -= need
        return True""", "pattern": "Greedy / Hash Map", "time": "O(n log n)", "space": "O(n)", "approach": "Greedily form groups starting from smallest available card.", "mermaid": ""},

853: {"code": """class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        fleets = 0
        prev_time = 0
        for pos, spd in pairs:
            time = (target - pos) / spd
            if time > prev_time:
                fleets += 1
                prev_time = time
        return fleets""", "pattern": "Stack / Sorting", "time": "O(n log n)", "space": "O(n)", "approach": "Sort by position descending. If a car takes longer than the one ahead, it forms a new fleet.", "mermaid": """```mermaid
flowchart TD
    A[Sort by position descending] --> B[For each car]
    B --> C[Compute arrival time]
    C --> D{Slower than previous?}
    D -- Yes --> E[New fleet, update prev_time]
    D -- No --> F[Joins previous fleet]
    E --> B
    F --> B
```"""},

875: {"code": """import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            hours = sum(math.ceil(p / mid) for p in piles)
            if hours <= h:
                hi = mid
            else:
                lo = mid + 1
        return lo""", "pattern": "Binary Search on Answer", "time": "O(n log m)", "space": "O(1)", "approach": "Binary search on eating speed k. For each k, compute total hours and compare with h.", "mermaid": """```mermaid
flowchart TD
    A[lo=1, hi=max piles] --> B{lo < hi?}
    B -- Yes --> C[mid = lo+hi / 2]
    C --> D[Compute hours at speed mid]
    D --> E{hours <= h?}
    E -- Yes --> F[hi = mid]
    E -- No --> G[lo = mid + 1]
    F --> B
    G --> B
    B -- No --> H[Return lo]
```"""},

981: {"code": """class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''
        vals = self.store[key]
        lo, hi = 0, len(vals) - 1
        result = ''
        while lo <= hi:
            mid = (lo + hi) // 2
            if vals[mid][0] <= timestamp:
                result = vals[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
        return result""", "pattern": "Binary Search / Design", "time": "O(log n) get, O(1) set", "space": "O(n)", "approach": "Store (timestamp, value) pairs sorted by timestamp. Binary search for largest timestamp <= query.", "mermaid": ""},

994: {"code": """from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        minutes = 0
        while queue:
            minutes += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
        return minutes - 1 if fresh == 0 else -1""", "pattern": "BFS / Graph", "time": "O(m*n)", "space": "O(m*n)", "approach": "Multi-source BFS from all rotten oranges simultaneously. Track minutes as levels.", "mermaid": """```mermaid
flowchart TD
    A[Queue all rotten oranges] --> B{Queue not empty AND fresh > 0?}
    B -- Yes --> C[Process one level BFS]
    C --> D[Rot adjacent fresh oranges]
    D --> E[minutes++]
    E --> B
    B -- No --> F{All fresh rotted?}
    F -- Yes --> G[Return minutes]
    F -- No --> H[Return -1]
```"""},

# ═══════════════════════════════════════════
# 1001-1500: Popular Problems
# ═══════════════════════════════════════════

1046: {"code": """import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a = -heapq.heappop(stones)
            b = -heapq.heappop(stones)
            if a != b:
                heapq.heappush(stones, -(a - b))
        return -stones[0] if stones else 0""", "pattern": "Heap", "time": "O(n log n)", "space": "O(n)", "approach": "Max-heap (via negation). Smash two heaviest, push difference back.", "mermaid": ""},

1143: {"code": """class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)
        for i in range(1, m + 1):
            prev = 0
            for j in range(1, n + 1):
                temp = dp[j]
                if text1[i-1] == text2[j-1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j-1])
                prev = temp
        return dp[n]""", "pattern": "Dynamic Programming", "time": "O(m*n)", "space": "O(n)", "approach": "Classic LCS DP. dp[i][j] = LCS of text1[:i] and text2[:j]. Optimized to 1D.", "mermaid": """```mermaid
flowchart TD
    A[Init dp row of zeros] --> B[For each char in text1]
    B --> C[For each char in text2]
    C --> D{Chars match?}
    D -- Yes --> E[dp = diagonal + 1]
    D -- No --> F["dp = max(above, left)"]
    E --> C
    F --> C
```"""},

1235: {"code": """import bisect

class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)
        dp = [0] * (n + 1)
        ends = [j[1] for j in jobs]
        for i in range(1, n + 1):
            s, e, p = jobs[i-1]
            j = bisect.bisect_right(ends, s, 0, i-1)
            dp[i] = max(dp[i-1], dp[j] + p)
        return dp[n]""", "pattern": "Dynamic Programming + Binary Search", "time": "O(n log n)", "space": "O(n)", "approach": "Sort by end time. For each job, binary search for the latest non-overlapping job. dp[i] = max(skip, take).", "mermaid": ""},

1448: {"code": """class Solution:
    def goodNodes(self, root) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0
            good = 1 if node.val >= max_so_far else 0
            new_max = max(max_so_far, node.val)
            return good + dfs(node.left, new_max) + dfs(node.right, new_max)
        return dfs(root, root.val)""", "pattern": "Tree / DFS", "time": "O(n)", "space": "O(h)", "approach": "DFS tracking max value from root to current node. A node is 'good' if its value >= max_so_far.", "mermaid": ""},

# ═══════════════════════════════════════════
# 1501-2000
# ═══════════════════════════════════════════

1584: {"code": """class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        import heapq
        n = len(points)
        visited = set()
        heap = [(0, 0)]
        cost = 0
        while len(visited) < n:
            d, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            cost += d
            for v in range(n):
                if v not in visited:
                    dist = abs(points[u][0]-points[v][0]) + abs(points[u][1]-points[v][1])
                    heapq.heappush(heap, (dist, v))
        return cost""", "pattern": "Prim's MST / Graph", "time": "O(n^2 log n)", "space": "O(n^2)", "approach": "Prim's algorithm: greedily add cheapest edge to MST. Use min-heap.", "mermaid": ""},

1851: {"code": """import heapq

class Solution:
    def minInterval(self, intervals, queries):
        intervals.sort()
        sorted_q = sorted(enumerate(queries), key=lambda x: x[1])
        result = [-1] * len(queries)
        heap = []
        i = 0
        for qi, q in sorted_q:
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, (r - l + 1, r))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                result[qi] = heap[0][0]
        return result""", "pattern": "Heap + Sorting", "time": "O((n+q) log n)", "space": "O(n+q)", "approach": "Sort intervals and queries. For each query, add qualifying intervals to heap, remove expired. Min-heap by size.", "mermaid": ""},

# ═══════════════════════════════════════════
# 2001-2500
# ═══════════════════════════════════════════

2013: {"code": """class DetectSquares:
    def __init__(self):
        from collections import defaultdict
        self.points = defaultdict(int)

    def add(self, point):
        self.points[tuple(point)] += 1

    def count(self, point):
        px, py = point
        result = 0
        for (x, y), cnt in self.points.items():
            if x != px and abs(x - px) == abs(y - py):
                result += cnt * self.points.get((px, y), 0) * self.points.get((x, py), 0)
        return result""", "pattern": "Hash Map / Design", "time": "O(n) count", "space": "O(n)", "approach": "For each diagonal point, check if the other two corners exist. Multiply counts for combinations.", "mermaid": ""},

2300: {"code": """class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        n = len(potions)
        result = []
        for spell in spells:
            needed = (success + spell - 1) // spell
            from bisect import bisect_left
            idx = bisect_left(potions, needed)
            result.append(n - idx)
        return result""", "pattern": "Binary Search + Sorting", "time": "O((m+n) log n)", "space": "O(1) extra", "approach": "Sort potions. For each spell, binary search for minimum potion needed.", "mermaid": ""},

}

# Set defaults
_DEFAULT_KEYS = {"code": "", "pattern": "", "time": "", "space": "", "approach": "", "pseudocode": "", "mermaid": "", "walkthrough": "", "animation_frames": ""}
for pid in SOLUTIONS_KB_EXT:
    for key, default in _DEFAULT_KEYS.items():
        SOLUTIONS_KB_EXT[pid].setdefault(key, default)
