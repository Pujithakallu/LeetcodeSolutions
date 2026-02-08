#!/usr/bin/env python3
"""
solutions_kb_ext2.py
====================
Additional hand-crafted solutions for key LeetCode problems (batch 2).
Covers popular/essential problems from ID range 500-2500.
"""

SOLUTIONS_KB_EXT2 = {

# ═══════════════════════════════════════════
# Binary Search & Two Pointers (500-600)
# ═══════════════════════════════════════════

516: {"code": """class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            new_dp = [0] * n
            new_dp[i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    new_dp[j] = dp[j-1] + 2
                else:
                    new_dp[j] = max(dp[j], new_dp[j-1])
            dp = new_dp
        return dp[n-1]""", "pattern": "Dynamic Programming", "time": "O(n^2)", "space": "O(n)", "approach": "LPS is LCS of s and reverse(s). DP with space optimization."},

525: {"code": """class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        count = 0
        max_len = 0
        map = {0: -1}
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in map:
                max_len = max(max_len, i - map[count])
            else:
                map[count] = i
        return max_len""", "pattern": "Prefix Sum + Hash Map", "time": "O(n)", "space": "O(n)", "approach": "Convert 0->-1, track running sum. Equal 0s and 1s means sum returns to same value."},

532: {"code": """class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        from collections import Counter
        counter = Counter(nums)
        result = 0
        for num in counter:
            if k == 0 and counter[num] > 1:
                result += 1
            elif k > 0 and num + k in counter:
                result += 1
        return result""", "pattern": "Hash Map", "time": "O(n)", "space": "O(n)", "approach": "Count occurrences. For k=0 check duplicates, else check if num+k exists."},

540: {"code": """class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                lo = mid + 2
            else:
                hi = mid
        return nums[lo]""", "pattern": "Binary Search", "time": "O(log n)", "space": "O(1)", "approach": "Binary search: ensure mid is even. If pair matches, single element is on right."},

556: {"code": """class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits) - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        if i < 0:
            return -1
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1
        digits[i], digits[j] = digits[j], digits[i]
        digits[i + 1:] = reversed(digits[i + 1:])
        result = int(''.join(digits))
        return result if result <= 2**31 - 1 else -1""", "pattern": "Math / Next Permutation", "time": "O(n)", "space": "O(n)", "approach": "Same as next permutation: find rightmost ascending pair, swap, reverse suffix."},

# ═══════════════════════════════════════════
# Trees, Graphs, BFS/DFS (600-800)
# ═══════════════════════════════════════════

684: {"code": """class Solution:
    def findRedundantConnection(self, edges):
        parent = list(range(len(edges) + 1))
        rank = [0] * (len(edges) + 1)
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True
        for u, v in edges:
            if not union(u, v):
                return [u, v]""", "pattern": "Union-Find", "time": "O(n * alpha(n))", "space": "O(n)", "approach": "Union-Find with path compression and rank. The edge that creates a cycle is redundant.",
    "mermaid": """```mermaid
flowchart TD
    A[Init: each node is its own parent] --> B[For each edge u,v]
    B --> C{find u == find v?}
    C -- Yes --> D[Return this edge - redundant]
    C -- No --> E[Union u and v]
    E --> B
```"""},

695: {"code": """class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        return max((dfs(r, c) for r in range(m) for c in range(n)), default=0)""", "pattern": "DFS / Graph", "time": "O(m*n)", "space": "O(m*n)", "approach": "DFS from each land cell, counting area. Mark visited by setting to 0."},

743: {"code": """import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        dist = {}
        heap = [(0, k)]
        while heap:
            d, u = heapq.heappop(heap)
            if u in dist:
                continue
            dist[u] = d
            for v, w in graph[u]:
                if v not in dist:
                    heapq.heappush(heap, (d + w, v))
        return max(dist.values()) if len(dist) == n else -1""", "pattern": "Dijkstra / Shortest Path", "time": "O(E log V)", "space": "O(V + E)", "approach": "Dijkstra's algorithm from source k. Answer is max of all shortest distances.",
    "mermaid": """```mermaid
flowchart TD
    A["heap = [(0, k)]"] --> B{Heap not empty?}
    B -- Yes --> C[Pop minimum distance node]
    C --> D{Already visited?}
    D -- Yes --> B
    D -- No --> E[Record distance]
    E --> F[Push all neighbors]
    F --> B
    B -- No --> G{All nodes reached?}
    G -- Yes --> H[Return max distance]
    G -- No --> I[Return -1]
```"""},

785: {"code": """from collections import deque

class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        for start in range(n):
            if color[start] != -1:
                continue
            queue = deque([start])
            color[start] = 0
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
        return True""", "pattern": "BFS / Graph Coloring", "time": "O(V + E)", "space": "O(V)", "approach": "BFS coloring: try to 2-color the graph. If adjacent nodes have same color, not bipartite."},

787: {"code": """class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float('inf')] * n
        prices[src] = 0
        for _ in range(k + 1):
            temp = prices[:]
            for u, v, w in flights:
                if prices[u] != float('inf'):
                    temp[v] = min(temp[v], prices[u] + w)
            prices = temp
        return prices[dst] if prices[dst] != float('inf') else -1""", "pattern": "Bellman-Ford (k stops)", "time": "O(k * E)", "space": "O(V)", "approach": "Modified Bellman-Ford: relax edges k+1 times. Use temp array to avoid using edges from current round."},

# ═══════════════════════════════════════════
# DP, Backtracking, Advanced (800-1000)
# ═══════════════════════════════════════════

838: {"code": """class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        d = list(dominoes)
        n = len(d)
        forces = [0] * n
        f = 0
        for i in range(n):
            if d[i] == 'R':
                f = n
            elif d[i] == 'L':
                f = 0
            else:
                f = max(f - 1, 0)
            forces[i] += f
        f = 0
        for i in range(n - 1, -1, -1):
            if d[i] == 'L':
                f = n
            elif d[i] == 'R':
                f = 0
            else:
                f = max(f - 1, 0)
            forces[i] -= f
        return ''.join('R' if f > 0 else 'L' if f < 0 else '.' for f in forces)""", "pattern": "Two Pass Simulation", "time": "O(n)", "space": "O(n)", "approach": "Two passes: left-to-right for R forces, right-to-left for L forces. Net force determines direction."},

895: {"code": """from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.maxfreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        f = self.freq[val]
        self.maxfreq = max(self.maxfreq, f)
        self.group[f].append(val)

    def pop(self) -> int:
        val = self.group[self.maxfreq].pop()
        self.freq[val] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        return val""", "pattern": "Stack + Hash Map / Design", "time": "O(1) per operation", "space": "O(n)", "approach": "Group elements by frequency in stacks. Pop from the highest frequency group."},

907: {"code": """class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        left = [0] * n
        right = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i
            stack.append(i)
        return sum(arr[i] * left[i] * right[i] for i in range(n)) % MOD""", "pattern": "Monotonic Stack", "time": "O(n)", "space": "O(n)", "approach": "For each element, find how many subarrays have it as minimum using left/right boundaries from monotonic stack."},

973: {"code": """import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for x, y in points:
            dist = -(x*x + y*y)
            if len(heap) < k:
                heapq.heappush(heap, (dist, x, y))
            elif dist > heap[0][0]:
                heapq.heapreplace(heap, (dist, x, y))
        return [[x, y] for _, x, y in heap]""", "pattern": "Heap / Quickselect", "time": "O(n log k)", "space": "O(k)", "approach": "Max-heap of size k (negated distances). Keep k closest points."},

# ═══════════════════════════════════════════
# 1000-1200
# ═══════════════════════════════════════════

1011: {"code": """class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            d, curr = 1, 0
            for w in weights:
                if curr + w > mid:
                    d += 1
                    curr = 0
                curr += w
            if d <= days:
                hi = mid
            else:
                lo = mid + 1
        return lo""", "pattern": "Binary Search on Answer", "time": "O(n log S)", "space": "O(1)", "approach": "Binary search on ship capacity. For each capacity, check if packages fit in 'days' days."},

1020: {"code": """class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return
            grid[r][c] = 0
            dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)
        for r in range(m):
            for c in range(n):
                if (r == 0 or r == m-1 or c == 0 or c == n-1) and grid[r][c] == 1:
                    dfs(r, c)
        return sum(sum(row) for row in grid)""", "pattern": "DFS / Graph", "time": "O(m*n)", "space": "O(m*n)", "approach": "DFS from border land cells to mark reachable. Count remaining land cells."},

1071: {"code": """from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        return str1[:gcd(len(str1), len(str2))]""", "pattern": "Math / String", "time": "O(n+m)", "space": "O(n+m)", "approach": "If str1+str2 != str2+str1, no common divisor. Otherwise, answer length = gcd of lengths."},

1091: {"code": """from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1
        while queue:
            r, c, d = queue.popleft()
            if r == n-1 and c == n-1:
                return d
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc, d+1))
        return -1""", "pattern": "BFS / Shortest Path", "time": "O(n^2)", "space": "O(n^2)", "approach": "BFS from (0,0) to (n-1,n-1) allowing 8-directional movement."},

1137: {"code": """class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n <= 2: return 1
        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c""", "pattern": "Dynamic Programming", "time": "O(n)", "space": "O(1)", "approach": "Iterative tribonacci with three variables."},

1162: {"code": """from collections import deque

class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        n = len(grid)
        queue = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))
        if len(queue) == 0 or len(queue) == n * n:
            return -1
        dist = -1
        while queue:
            dist += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc))
        return dist""", "pattern": "Multi-source BFS", "time": "O(n^2)", "space": "O(n^2)", "approach": "Multi-source BFS from all land cells. Last water cell reached gives max distance."},

# ═══════════════════════════════════════════
# 1200-1500
# ═══════════════════════════════════════════

1254: {"code": """class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            if grid[r][c] == 1:
                return True
            grid[r][c] = 1
            a = dfs(r+1,c)
            b = dfs(r-1,c)
            c1 = dfs(r,c+1)
            d = dfs(r,c-1)
            return a and b and c1 and d
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0 and dfs(r, c):
                    count += 1
        return count""", "pattern": "DFS / Graph", "time": "O(m*n)", "space": "O(m*n)", "approach": "DFS each land island. If DFS never goes out of bounds, it is closed."},

1268: {"code": """class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        result = []
        prefix = ''
        start = 0
        for c in searchWord:
            prefix += c
            import bisect
            start = bisect.bisect_left(products, prefix, start)
            end = bisect.bisect_left(products, prefix[:-1] + chr(ord(prefix[-1]) + 1), start)
            result.append(products[start:min(start + 3, end)])
        return result""", "pattern": "Binary Search / Trie", "time": "O(n log n + m*log n)", "space": "O(1) extra", "approach": "Sort products. For each prefix, binary search for matching range, return first 3."},

1319: {"code": """class Solution:
    def makeConnected(self, n: int, connections) -> int:
        if len(connections) < n - 1:
            return -1
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        components = n
        for a, b in connections:
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pa] = pb
                components -= 1
        return components - 1""", "pattern": "Union-Find", "time": "O(n + E * alpha(n))", "space": "O(n)", "approach": "Need n-1 cables minimum. Count connected components with Union-Find. Answer = components - 1."},

1337: {"code": """import heapq

class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        strengths = [(sum(row), i) for i, row in enumerate(mat)]
        heapq.heapify(strengths)
        return [heapq.heappop(strengths)[1] for _ in range(k)]""", "pattern": "Heap / Sorting", "time": "O(m*n + k*log m)", "space": "O(m)", "approach": "Calculate strength per row, use min-heap to get k weakest."},

1396: {"code": """from collections import defaultdict

class UndergroundSystem:
    def __init__(self):
        self.checkins = {}
        self.totals = defaultdict(lambda: [0, 0])

    def checkIn(self, id, stationName, t):
        self.checkins[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        start, t0 = self.checkins.pop(id)
        key = (start, stationName)
        self.totals[key][0] += t - t0
        self.totals[key][1] += 1

    def getAverageTime(self, startStation, endStation):
        total, count = self.totals[(startStation, endStation)]
        return total / count""", "pattern": "Design / Hash Map", "time": "O(1) per operation", "space": "O(n)", "approach": "Track checkins by id, accumulate (total_time, count) per route pair."},

# ═══════════════════════════════════════════
# 1500-2000
# ═══════════════════════════════════════════

1514: {"code": """import heapq
from collections import defaultdict

class Solution:
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))
        dist = [0.0] * n
        dist[start_node] = 1.0
        heap = [(-1.0, start_node)]
        while heap:
            neg_prob, u = heapq.heappop(heap)
            prob = -neg_prob
            if u == end_node:
                return prob
            if prob < dist[u]:
                continue
            for v, p in graph[u]:
                new_prob = prob * p
                if new_prob > dist[v]:
                    dist[v] = new_prob
                    heapq.heappush(heap, (-new_prob, v))
        return 0.0""", "pattern": "Dijkstra (Max Probability)", "time": "O(E log V)", "space": "O(V + E)", "approach": "Modified Dijkstra: maximize probability instead of minimizing distance."},

1557: {"code": """class Solution:
    def findSmallestSetOfVertices(self, n: int, edges) -> list[int]:
        has_incoming = set()
        for _, v in edges:
            has_incoming.add(v)
        return [i for i in range(n) if i not in has_incoming]""", "pattern": "Graph / Indegree", "time": "O(V + E)", "space": "O(V)", "approach": "Nodes with 0 in-degree must be starting points. All other nodes are reachable from these."},

1631: {"code": """import heapq

class Solution:
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            effort, r, c = heapq.heappop(heap)
            if r == m-1 and c == n-1:
                return effort
            if effort > dist[r][c]:
                continue
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))
        return 0""", "pattern": "Dijkstra / Graph", "time": "O(mn log(mn))", "space": "O(mn)", "approach": "Modified Dijkstra: minimize maximum absolute difference along path."},

1642: {"code": """import heapq

class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
            heapq.heappush(heap, diff)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        return len(heights) - 1""", "pattern": "Heap / Greedy", "time": "O(n log L)", "space": "O(L)", "approach": "Use ladders for largest climbs (heap). Use bricks for the rest. Min-heap of size ladders."},

1706: {"code": """class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        result = []
        for col in range(n):
            c = col
            for r in range(m):
                d = grid[r][c]
                nc = c + d
                if nc < 0 or nc >= n or grid[r][nc] != d:
                    c = -1
                    break
                c = nc
            result.append(c)
        return result""", "pattern": "Simulation", "time": "O(m*n)", "space": "O(1) extra", "approach": "Simulate each ball falling. Check for V-shaped traps at each row."},

1768: {"code": """class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return ''.join(result)""", "pattern": "Two Pointers / String", "time": "O(n+m)", "space": "O(n+m)", "approach": "Alternate characters from both strings using a single index."},

1899: {"code": """class Solution:
    def mergeTriplets(self, triplets, target):
        good = set()
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                for i in range(3):
                    if t[i] == target[i]:
                        good.add(i)
        return len(good) == 3""", "pattern": "Greedy", "time": "O(n)", "space": "O(1)", "approach": "A triplet is usable if no value exceeds target. Check if all target values are achievable."},

# ═══════════════════════════════════════════
# 2000-2500
# ═══════════════════════════════════════════

2095: {"code": """class Solution:
    def deleteMiddle(self, head):
        if not head.next:
            return None
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head""", "pattern": "Linked List / Fast-Slow Pointers", "time": "O(n)", "space": "O(1)", "approach": "Fast pointer starts 2 ahead. When fast reaches end, slow is before middle. Delete slow.next."},

2130: {"code": """class Solution:
    def pairSum(self, head) -> int:
        # Find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Reverse second half
        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        # Find max twin sum
        max_sum = 0
        while prev:
            max_sum = max(max_sum, head.val + prev.val)
            head = head.next
            prev = prev.next
        return max_sum""", "pattern": "Linked List / Two Pointers", "time": "O(n)", "space": "O(1)", "approach": "Find middle, reverse second half, compute pairwise sums."},

2215: {"code": """class Solution:
    def findDifference(self, nums1, nums2):
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]""", "pattern": "Hash Set", "time": "O(n+m)", "space": "O(n+m)", "approach": "Set difference: elements in one set but not the other."},

2336: {"code": """import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.current = 1
        self.added_back = []
        self.added_set = set()

    def popSmallest(self) -> int:
        if self.added_back:
            val = heapq.heappop(self.added_back)
            self.added_set.remove(val)
            return val
        val = self.current
        self.current += 1
        return val

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.added_set:
            heapq.heappush(self.added_back, num)
            self.added_set.add(num)""", "pattern": "Heap / Design", "time": "O(log n) per op", "space": "O(n)", "approach": "Track current smallest + min-heap for added-back numbers below current."},

2390: {"code": """class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)""", "pattern": "Stack", "time": "O(n)", "space": "O(n)", "approach": "Stack: push non-star chars, pop on star."},

2462: {"code": """import heapq

class Solution:
    def totalCost(self, costs, k, candidates):
        n = len(costs)
        left_heap = []
        right_heap = []
        l, r = 0, n - 1
        for i in range(candidates):
            if l <= r:
                heapq.heappush(left_heap, (costs[l], l))
                l += 1
        for i in range(candidates):
            if l <= r:
                heapq.heappush(right_heap, (costs[r], r))
                r -= 1
        total = 0
        for _ in range(k):
            left_val = left_heap[0] if left_heap else (float('inf'), -1)
            right_val = right_heap[0] if right_heap else (float('inf'), -1)
            if left_val <= right_val:
                cost, idx = heapq.heappop(left_heap)
                total += cost
                if l <= r:
                    heapq.heappush(left_heap, (costs[l], l))
                    l += 1
            else:
                cost, idx = heapq.heappop(right_heap)
                total += cost
                if l <= r:
                    heapq.heappush(right_heap, (costs[r], r))
                    r -= 1
        return total""", "pattern": "Two Heaps / Greedy", "time": "O((k+c) log c)", "space": "O(c)", "approach": "Two min-heaps for left and right candidates. Pick cheaper worker each round."},

}

# Set defaults
_DEFAULT_KEYS = {"code": "", "pattern": "", "time": "", "space": "", "approach": "", "pseudocode": "", "mermaid": "", "walkthrough": "", "animation_frames": ""}
for pid in SOLUTIONS_KB_EXT2:
    for key, default in _DEFAULT_KEYS.items():
        SOLUTIONS_KB_EXT2[pid].setdefault(key, default)
