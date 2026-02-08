#!/usr/bin/env python3
"""
solution_templates.py
=====================
Pattern-based Python3 and C++ solution template engine.
~50 pattern families, each with parameterized skeletons.

Each template has:
  - py_body:  Python solution body (indented 8 spaces, inside def)
  - cpp_body: C++ solution body (indented 8 spaces, inside method)
  - py_imports: extra Python imports needed (if any)
  - cpp_includes: extra C++ headers needed (if any)

Templates use these placeholders (filled by generate_solver.py):
  {method_name}, {params}, {return_type}, {ret_default}
  {param0}, {param1}, {param2} -- first/second/third param name
  {ptype0}, {ptype1} -- first/second param C++ type
"""

# ═══════════════════════════════════════════════════════════════════
# TEMPLATE REGISTRY
# ═══════════════════════════════════════════════════════════════════

TEMPLATES = {}


def _t(pattern, *, py, cpp, py_imports="", cpp_includes=""):
    """Register a template for a pattern."""
    TEMPLATES[pattern] = {
        "py_body": py,
        "cpp_body": cpp,
        "py_imports": py_imports,
        "cpp_includes": cpp_includes,
    }


# ─────────────────────────────────────────
# HASH MAP
# ─────────────────────────────────────────
_t("hash_map",
   py="""\
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate({param0}):
            complement = {param1} - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return {ret_default}""",
   cpp="""\
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < {param0}.size(); i++) {{
            int complement = {param1} - {param0}[i];
            if (seen.count(complement)) {{
                return {{seen[complement], i}};
            }}
            seen[{param0}[i]] = i;
        }}
        return {ret_default};""",
   cpp_includes="#include <unordered_map>")

# ─────────────────────────────────────────
# HASH MAP STRING
# ─────────────────────────────────────────
_t("hash_map_string",
   py="""\
        # Hash map for string/character frequency - O(n) time
        freq = {{}}
        for ch in {param0}:
            freq[ch] = freq.get(ch, 0) + 1
        # Process frequency map
        for ch, cnt in freq.items():
            if cnt == 1:
                return {param0}.index(ch)
        return {ret_default}""",
   cpp="""\
        // Hash map for string/character frequency - O(n) time
        unordered_map<char, int> freq;
        for (char ch : {param0}) {{
            freq[ch]++;
        }}
        // Process frequency map
        for (int i = 0; i < {param0}.size(); i++) {{
            if (freq[{param0}[i]] == 1) return i;
        }}
        return {ret_default};""",
   cpp_includes="#include <unordered_map>")

# ─────────────────────────────────────────
# TWO POINTER
# ─────────────────────────────────────────
_t("two_pointer",
   py="""\
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len({param0}) - 1
        while left < right:
            curr = {param0}[left] + {param0}[right]
            if curr == {param1}:
                return [left, right]
            elif curr < {param1}:
                left += 1
            else:
                right -= 1
        return {ret_default}""",
   cpp="""\
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = {param0}.size() - 1;
        while (left < right) {{
            int curr = {param0}[left] + {param0}[right];
            if (curr == {param1}) {{
                return {{left, right}};
            }} else if (curr < {param1}) {{
                left++;
            }} else {{
                right--;
            }}
        }}
        return {ret_default};""")

# ─────────────────────────────────────────
# TWO POINTER SORTED
# ─────────────────────────────────────────
_t("two_pointer_sorted",
   py="""\
        # Sort + two pointers - O(n log n) time
        {param0}.sort()
        left, right = 0, len({param0}) - 1
        result = {ret_default}
        while left < right:
            curr_sum = {param0}[left] + {param0}[right]
            if curr_sum < {param1} if isinstance({param1}, int) else 0:
                left += 1
            else:
                right -= 1
        return result""",
   cpp="""\
        // Sort + two pointers - O(n log n) time
        sort({param0}.begin(), {param0}.end());
        int left = 0, right = {param0}.size() - 1;
        while (left < right) {{
            int curr = {param0}[left] + {param0}[right];
            if (curr < {param1}) {{
                left++;
            }} else {{
                right--;
            }}
        }}
        return {ret_default};""",
   cpp_includes="#include <algorithm>")

# ─────────────────────────────────────────
# SLIDING WINDOW
# ─────────────────────────────────────────
_t("sliding_window",
   py="""\
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len({param0})):
            window[{param0}[right]] += 1
            while len(window) > ({param1} if isinstance({param1}, int) else len({param0})):
                window[{param0}[left]] -= 1
                if window[{param0}[left]] == 0:
                    del window[{param0}[left]]
                left += 1
            result = max(result, right - left + 1)
        return result""",
   cpp="""\
        // Sliding window approach - O(n) time, O(k) space
        unordered_map<char, int> window;
        int left = 0, result = 0;
        for (int right = 0; right < {param0}.size(); right++) {{
            window[{param0}[right]]++;
            while ((int)window.size() > {param1}) {{
                window[{param0}[left]]--;
                if (window[{param0}[left]] == 0)
                    window.erase({param0}[left]);
                left++;
            }}
            result = max(result, right - left + 1);
        }}
        return result;""",
   cpp_includes="#include <unordered_map>\n#include <algorithm>")

# ─────────────────────────────────────────
# BINARY SEARCH
# ─────────────────────────────────────────
_t("binary_search",
   py="""\
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len({param0}) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if {param0}[mid] == {param1}:
                return mid
            elif {param0}[mid] < {param1}:
                lo = mid + 1
            else:
                hi = mid - 1
        return {ret_default}""",
   cpp="""\
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = {param0}.size() - 1;
        while (lo <= hi) {{
            int mid = lo + (hi - lo) / 2;
            if ({param0}[mid] == {param1}) {{
                return mid;
            }} else if ({param0}[mid] < {param1}) {{
                lo = mid + 1;
            }} else {{
                hi = mid - 1;
            }}
        }}
        return {ret_default};""")

# ─────────────────────────────────────────
# LINKED LIST
# ─────────────────────────────────────────
_t("linked_list",
   py="""\
        # Linked list traversal/manipulation
        dummy = ListNode(0)
        dummy.next = {param0}
        prev, curr = dummy, {param0}
        while curr:
            nxt = curr.next
            # Process current node
            prev = curr
            curr = nxt
        return dummy.next""",
   cpp="""\
        // Linked list traversal/manipulation
        ListNode dummy(0);
        dummy.next = {param0};
        ListNode* prev = &dummy;
        ListNode* curr = {param0};
        while (curr) {{
            ListNode* nxt = curr->next;
            // Process current node
            prev = curr;
            curr = nxt;
        }}
        return dummy.next;""")

# ─────────────────────────────────────────
# STACK
# ─────────────────────────────────────────
_t("stack",
   py="""\
        # Stack-based approach - O(n) time
        stack = []
        for ch in {param0}:
            if stack and self._matches(stack[-1], ch):
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0 if isinstance({ret_default}, bool) else stack

    def _matches(self, a, b):
        pairs = {{'(': ')', '[': ']', '{{': '}}'}}
        return pairs.get(a) == b""",
   cpp="""\
        // Stack-based approach - O(n) time
        stack<char> st;
        unordered_map<char, char> pairs = {{{{'(', ')'}}, {{'[', ']'}}, {{'{', '}'}}}};
        for (char ch : {param0}) {{
            if (!st.empty() && pairs.count(st.top()) && pairs[st.top()] == ch) {{
                st.pop();
            }} else {{
                st.push(ch);
            }}
        }}
        return st.empty();""",
   cpp_includes="#include <stack>\n#include <unordered_map>")

# ─────────────────────────────────────────
# MONOTONIC STACK
# ─────────────────────────────────────────
_t("monotonic_stack",
   py="""\
        # Monotonic stack - O(n) time, O(n) space
        n = len({param0})
        result = [0] * n
        stack = []  # indices
        for i in range(n):
            while stack and {param0}[i] > {param0}[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result""",
   cpp="""\
        // Monotonic stack - O(n) time, O(n) space
        int n = {param0}.size();
        vector<int> result(n, 0);
        stack<int> st;
        for (int i = 0; i < n; i++) {{
            while (!st.empty() && {param0}[i] > {param0}[st.top()]) {{
                int idx = st.top(); st.pop();
                result[idx] = i - idx;
            }}
            st.push(i);
        }}
        return result;""",
   cpp_includes="#include <stack>")

# ─────────────────────────────────────────
# MONOTONIC QUEUE
# ─────────────────────────────────────────
_t("monotonic_queue",
   py="""\
        # Monotonic deque - O(n) time
        from collections import deque
        dq = deque()  # store indices
        result = []
        k = {param1} if isinstance({param1}, int) else 1
        for i in range(len({param0})):
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            while dq and {param0}[dq[-1]] < {param0}[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append({param0}[dq[0]])
        return result""",
   cpp="""\
        // Monotonic deque - O(n) time
        deque<int> dq;
        vector<int> result;
        int k = {param1};
        for (int i = 0; i < (int){param0}.size(); i++) {{
            while (!dq.empty() && dq.front() < i - k + 1)
                dq.pop_front();
            while (!dq.empty() && {param0}[dq.back()] < {param0}[i])
                dq.pop_back();
            dq.push_back(i);
            if (i >= k - 1)
                result.push_back({param0}[dq.front()]);
        }}
        return result;""",
   cpp_includes="#include <deque>")

# ─────────────────────────────────────────
# DFS TREE
# ─────────────────────────────────────────
_t("dfs_tree",
   py="""\
        # DFS on binary tree - O(n) time, O(h) space
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left, right)
        
        result = dfs({param0})
        return result""",
   cpp="""\
        // DFS on binary tree - O(n) time, O(h) space
        function<int(TreeNode*)> dfs = [&](TreeNode* node) -> int {{
            if (!node) return 0;
            int left = dfs(node->left);
            int right = dfs(node->right);
            return 1 + max(left, right);
        }};
        return dfs({param0});""",
   cpp_includes="#include <algorithm>\n#include <functional>")

# ─────────────────────────────────────────
# BFS TREE
# ─────────────────────────────────────────
_t("bfs_tree",
   py="""\
        # BFS level-order traversal - O(n) time, O(n) space
        from collections import deque
        if not {param0}:
            return {ret_default}
        result = []
        queue = deque([{param0}])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result""",
   cpp="""\
        // BFS level-order traversal - O(n) time, O(n) space
        vector<vector<int>> result;
        if (!{param0}) return result;
        queue<TreeNode*> q;
        q.push({param0});
        while (!q.empty()) {{
            int sz = q.size();
            vector<int> level;
            for (int i = 0; i < sz; i++) {{
                TreeNode* node = q.front(); q.pop();
                level.push_back(node->val);
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }}
            result.push_back(level);
        }}
        return result;""",
   cpp_includes="#include <queue>")

# ─────────────────────────────────────────
# TREE TRAVERSAL (generic)
# ─────────────────────────────────────────
_t("tree_traversal",
   py="""\
        # Tree traversal - O(n) time, O(h) space
        result = []
        def traverse(node):
            if not node:
                return
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse({param0})
        return result if isinstance({ret_default}, list) else result[0] if result else {ret_default}""",
   cpp="""\
        // Tree traversal - O(n) time, O(h) space
        vector<int> result;
        function<void(TreeNode*)> traverse = [&](TreeNode* node) {{
            if (!node) return;
            result.push_back(node->val);
            traverse(node->left);
            traverse(node->right);
        }};
        traverse({param0});
        return result;""",
   cpp_includes="#include <functional>")

# ─────────────────────────────────────────
# BST (Binary Search Tree)
# ─────────────────────────────────────────
_t("bst",
   py="""\
        # BST search/insert - O(h) time
        def search(node, target):
            if not node:
                return None
            if target == node.val:
                return node
            elif target < node.val:
                return search(node.left, target)
            else:
                return search(node.right, target)
        return search({param0}, {param1} if '{param1}' != '{param0}' else 0)""",
   cpp="""\
        // BST search/insert - O(h) time
        function<TreeNode*(TreeNode*, int)> search = [&](TreeNode* node, int target) -> TreeNode* {{
            if (!node) return nullptr;
            if (target == node->val) return node;
            else if (target < node->val) return search(node->left, target);
            else return search(node->right, target);
        }};
        return search({param0}, {param1});""",
   cpp_includes="#include <functional>")

# ─────────────────────────────────────────
# DFS MATRIX (grid)
# ─────────────────────────────────────────
_t("dfs_matrix",
   py="""\
        # DFS on grid - O(m*n) time
        if not {param0}:
            return 0
        rows, cols = len({param0}), len({param0}[0])
        count = 0
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if {param0}[r][c] == '0' or {param0}[r][c] == 0:
                return
            {param0}[r][c] = '0'
            dfs(r+1, c); dfs(r-1, c)
            dfs(r, c+1); dfs(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if {param0}[r][c] == '1' or {param0}[r][c] == 1:
                    dfs(r, c)
                    count += 1
        return count""",
   cpp="""\
        // DFS on grid - O(m*n) time
        if ({param0}.empty()) return 0;
        int rows = {param0}.size(), cols = {param0}[0].size();
        int count = 0;
        function<void(int, int)> dfs = [&](int r, int c) {{
            if (r < 0 || r >= rows || c < 0 || c >= cols) return;
            if ({param0}[r][c] == '0') return;
            {param0}[r][c] = '0';
            dfs(r+1, c); dfs(r-1, c);
            dfs(r, c+1); dfs(r, c-1);
        }};
        for (int r = 0; r < rows; r++) {{
            for (int c = 0; c < cols; c++) {{
                if ({param0}[r][c] == '1') {{
                    dfs(r, c);
                    count++;
                }}
            }}
        }}
        return count;""",
   cpp_includes="#include <functional>")

# ─────────────────────────────────────────
# BFS MATRIX
# ─────────────────────────────────────────
_t("bfs_matrix",
   py="""\
        # BFS on grid - O(m*n) time
        from collections import deque
        if not {param0}:
            return {ret_default}
        rows, cols = len({param0}), len({param0}[0])
        queue = deque()
        visited = set()
        # Initialize BFS sources
        for r in range(rows):
            for c in range(cols):
                if {param0}[r][c] == 1 or {param0}[r][c] == '1':
                    queue.append((r, c, 0))
                    visited.add((r, c))
        steps = 0
        while queue:
            r, c, d = queue.popleft()
            steps = max(steps, d)
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, d+1))
        return steps""",
   cpp="""\
        // BFS on grid - O(m*n) time
        if ({param0}.empty()) return {ret_default};
        int rows = {param0}.size(), cols = {param0}[0].size();
        queue<tuple<int,int,int>> q;
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));
        int dirs[4][2] = {{{{1,0}},{{-1,0}},{{0,1}},{{0,-1}}}};
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if ({param0}[r][c] == 1) {{
                    q.push({{r, c, 0}});
                    visited[r][c] = true;
                }}
        int steps = 0;
        while (!q.empty()) {{
            auto [r, c, d] = q.front(); q.pop();
            steps = max(steps, d);
            for (auto& dir : dirs) {{
                int nr = r+dir[0], nc = c+dir[1];
                if (nr>=0 && nr<rows && nc>=0 && nc<cols && !visited[nr][nc]) {{
                    visited[nr][nc] = true;
                    q.push({{nr, nc, d+1}});
                }}
            }}
        }}
        return steps;""",
   cpp_includes="#include <queue>\n#include <tuple>\n#include <algorithm>")

# ─────────────────────────────────────────
# DFS GRAPH
# ─────────────────────────────────────────
_t("dfs_graph",
   py="""\
        # DFS on graph - O(V+E) time
        visited = set()
        result = []
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            result.append(node)
            # Traverse neighbors (adjust based on adjacency representation)
        
        dfs(0)
        return result if isinstance({ret_default}, list) else len(result)""",
   cpp="""\
        // DFS on graph - O(V+E) time
        vector<bool> visited({param0}.size(), false);
        vector<int> result;
        function<void(int)> dfs = [&](int node) {{
            if (visited[node]) return;
            visited[node] = true;
            result.push_back(node);
            // Traverse neighbors
        }};
        dfs(0);
        return result;""",
   cpp_includes="#include <functional>")

# ─────────────────────────────────────────
# BFS GRAPH
# ─────────────────────────────────────────
_t("bfs_graph",
   py="""\
        # BFS on graph - O(V+E) time
        from collections import deque
        if not {param0}:
            return {ret_default}
        visited = set()
        queue = deque([0])
        visited.add(0)
        dist = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                # Process node
            dist += 1
        return dist""",
   cpp="""\
        // BFS on graph - O(V+E) time
        if ({param0}.empty()) return {ret_default};
        queue<int> q;
        unordered_set<int> visited;
        q.push(0);
        visited.insert(0);
        int dist = 0;
        while (!q.empty()) {{
            int sz = q.size();
            for (int i = 0; i < sz; i++) {{
                int node = q.front(); q.pop();
                // Process node
            }}
            dist++;
        }}
        return dist;""",
   cpp_includes="#include <queue>\n#include <unordered_set>")

# ─────────────────────────────────────────
# GRAPH GENERAL
# ─────────────────────────────────────────
_t("graph_general",
   py="""\
        # Graph traversal - O(V+E) time
        from collections import defaultdict
        graph = defaultdict(list)
        # Build adjacency list from input
        n = len({param0}) if isinstance({param0}, list) else {param0}
        visited = [False] * n
        result = 0
        
        def dfs(node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                result += 1
        return result""",
   cpp="""\
        // Graph traversal - O(V+E) time
        int n = {param0}.size();
        vector<vector<int>> graph(n);
        vector<bool> visited(n, false);
        int result = 0;
        function<void(int)> dfs = [&](int node) {{
            visited[node] = true;
            for (int neighbor : graph[node]) {{
                if (!visited[neighbor]) dfs(neighbor);
            }}
        }};
        for (int i = 0; i < n; i++) {{
            if (!visited[i]) {{
                dfs(i);
                result++;
            }}
        }}
        return result;""",
   cpp_includes="#include <functional>")

# ─────────────────────────────────────────
# DP 1D
# ─────────────────────────────────────────
_t("dp_1d",
   py="""\
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not {param0}:
            return 0
        n = len({param0}) if isinstance({param0}, list) else {param0}
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]""",
   cpp="""\
        // Dynamic programming (1D) - O(n) time, O(n) space
        int n = {param0};
        if (n <= 0) return 0;
        vector<int> dp(n + 1, 0);
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {{
            dp[i] = dp[i-1];
            if (i >= 2) dp[i] += dp[i-2];
        }}
        return dp[n];""")

# ─────────────────────────────────────────
# DP 2D
# ─────────────────────────────────────────
_t("dp_2d",
   py="""\
        # Dynamic programming (2D) - O(m*n) time and space
        if not {param0}:
            return 0
        m, n = len({param0}), len({param0}[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                # Add problem-specific transition
        return dp[m][n]""",
   cpp="""\
        // Dynamic programming (2D) - O(m*n) time and space
        if ({param0}.empty()) return 0;
        int m = {param0}.size(), n = {param0}[0].size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; i++) {{
            for (int j = 1; j <= n; j++) {{
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }}
        }}
        return dp[m][n];""",
   cpp_includes="#include <algorithm>")

# ─────────────────────────────────────────
# DP STRING
# ─────────────────────────────────────────
_t("dp_string",
   py="""\
        # String DP - O(m*n) time and space
        m, n = len({param0}), len({param1})
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if {param0}[i-1] == {param1}[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]""",
   cpp="""\
        // String DP - O(m*n) time and space
        int m = {param0}.size(), n = {param1}.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; i++) {{
            for (int j = 1; j <= n; j++) {{
                if ({param0}[i-1] == {param1}[j-1])
                    dp[i][j] = dp[i-1][j-1] + 1;
                else
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }}
        }}
        return dp[m][n];""",
   cpp_includes="#include <algorithm>")

# ─────────────────────────────────────────
# DP BITMASK
# ─────────────────────────────────────────
_t("dp_bitmask",
   py="""\
        # Bitmask DP - O(2^n * n) time
        n = len({param0})
        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            bits = bin(mask).count('1')
            for i in range(n):
                if mask & (1 << i):
                    continue
                new_mask = mask | (1 << i)
                dp[new_mask] = min(dp[new_mask], dp[mask] + 1)
        return dp[(1 << n) - 1]""",
   cpp="""\
        // Bitmask DP - O(2^n * n) time
        int n = {param0}.size();
        vector<int> dp(1 << n, INT_MAX);
        dp[0] = 0;
        for (int mask = 0; mask < (1 << n); mask++) {{
            for (int i = 0; i < n; i++) {{
                if (mask & (1 << i)) continue;
                int new_mask = mask | (1 << i);
                dp[new_mask] = min(dp[new_mask], dp[mask] + 1);
            }}
        }}
        return dp[(1 << n) - 1];""",
   cpp_includes="#include <climits>\n#include <algorithm>")

# ─────────────────────────────────────────
# BACKTRACKING
# ─────────────────────────────────────────
_t("backtracking",
   py="""\
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len({param0})):
                path.append({param0}[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result""",
   cpp="""\
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {{
            result.push_back(path);
            for (int i = start; i < (int){param0}.size(); i++) {{
                path.push_back({param0}[i]);
                backtrack(i + 1);
                path.pop_back();
            }}
        }};
        backtrack(0);
        return result;""",
   cpp_includes="#include <functional>")

# ─────────────────────────────────────────
# GREEDY
# ─────────────────────────────────────────
_t("greedy",
   py="""\
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len({param0})):
            if isinstance({param0}[i], int):
                curr_max = max(curr_max, {param0}[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result""",
   cpp="""\
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int){param0}.size(); i++) {{
            curr_max = max(curr_max, {param0}[i]);
            result = max(result, curr_max);
        }}
        return result;""",
   cpp_includes="#include <algorithm>")

# ─────────────────────────────────────────
# GREEDY SORT
# ─────────────────────────────────────────
_t("greedy_sort",
   py="""\
        # Sort + greedy - O(n log n) time
        {param0}.sort()
        result = 0
        curr_end = 0
        for item in {param0}:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result""",
   cpp="""\
        // Sort + greedy - O(n log n) time
        sort({param0}.begin(), {param0}.end());
        int result = 0, curr_end = 0;
        for (auto& item : {param0}) {{
            result++;
        }}
        return result;""",
   cpp_includes="#include <algorithm>")

# ─────────────────────────────────────────
# UNION FIND
# ─────────────────────────────────────────
_t("union_find",
   py="""\
        # Union Find (Disjoint Set Union) - O(n * alpha(n))
        parent = list(range(len({param0}) + 1 if isinstance({param0}, list) else {param0} + 1))
        rank = [0] * len(parent)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
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
        
        components = len(parent)
        # Process edges/connections
        return components""",
   cpp="""\
        // Union Find (DSU) - O(n * alpha(n))
        int n = {param0}.size();
        vector<int> parent(n + 1), rnk(n + 1, 0);
        iota(parent.begin(), parent.end(), 0);
        function<int(int)> find = [&](int x) -> int {{
            return parent[x] == x ? x : parent[x] = find(parent[x]);
        }};
        auto unite = [&](int x, int y) -> bool {{
            int px = find(x), py = find(y);
            if (px == py) return false;
            if (rnk[px] < rnk[py]) swap(px, py);
            parent[py] = px;
            if (rnk[px] == rnk[py]) rnk[px]++;
            return true;
        }};
        int components = n;
        return components;""",
   cpp_includes="#include <numeric>\n#include <functional>")

# ─────────────────────────────────────────
# TOPOLOGICAL SORT
# ─────────────────────────────────────────
_t("topological_sort",
   py="""\
        # Topological sort (Kahn's algorithm) - O(V+E)
        from collections import deque, defaultdict
        graph = defaultdict(list)
        n = {param0} if isinstance({param0}, int) else len({param0})
        indegree = [0] * n
        # Build graph from prerequisites
        prereqs = {param1} if isinstance({param1}, list) else {param0}
        for edge in prereqs:
            if isinstance(edge, (list, tuple)) and len(edge) >= 2:
                graph[edge[1]].append(edge[0])
                indegree[edge[0]] += 1
        queue = deque([i for i in range(n) if indegree[i] == 0])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return len(order) == n if isinstance({ret_default}, bool) else order""",
   cpp="""\
        // Topological sort (Kahn's) - O(V+E)
        int n = {param0};
        vector<vector<int>> graph(n);
        vector<int> indegree(n, 0);
        for (auto& edge : {param1}) {{
            graph[edge[1]].push_back(edge[0]);
            indegree[edge[0]]++;
        }}
        queue<int> q;
        for (int i = 0; i < n; i++)
            if (indegree[i] == 0) q.push(i);
        vector<int> order;
        while (!q.empty()) {{
            int node = q.front(); q.pop();
            order.push_back(node);
            for (int neighbor : graph[node]) {{
                if (--indegree[neighbor] == 0) q.push(neighbor);
            }}
        }}
        return order.size() == n;""",
   cpp_includes="#include <queue>")

# ─────────────────────────────────────────
# TRIE
# ─────────────────────────────────────────
_t("trie",
   py="""\
        # Trie-based approach
        trie = {{}}
        # Build trie from word list
        words = {param0} if isinstance({param0}, list) else [{param0}]
        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {{}}
                node = node[ch]
            node['#'] = True
        
        # Search in trie
        def search(word):
            node = trie
            for ch in word:
                if ch not in node:
                    return False
                node = node[ch]
            return '#' in node
        
        return {ret_default}""",
   cpp="""\
        // Trie-based approach
        struct TrieNode {{
            TrieNode* children[26] = {{}};
            bool isEnd = false;
        }};
        TrieNode* root = new TrieNode();
        // Build trie
        for (auto& word : {param0}) {{
            TrieNode* node = root;
            for (char ch : word) {{
                int idx = ch - 'a';
                if (!node->children[idx])
                    node->children[idx] = new TrieNode();
                node = node->children[idx];
            }}
            node->isEnd = true;
        }}
        return {ret_default};""")

# ─────────────────────────────────────────
# HEAP (Priority Queue)
# ─────────────────────────────────────────
_t("heap",
   py="""\
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not {param0}:
            return {ret_default}
        # Min heap (negate for max heap)
        heap = []
        for val in {param0}:
            heapq.heappush(heap, val)
            if len(heap) > ({param1} if isinstance({param1}, int) else len({param0})):
                heapq.heappop(heap)
        return heap[0] if heap else {ret_default}""",
   cpp="""\
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : {param0}) {{
            pq.push(val);
            if ((int)pq.size() > {param1})
                pq.pop();
        }}
        return pq.empty() ? {ret_default} : pq.top();""",
   cpp_includes="#include <queue>")

# ─────────────────────────────────────────
# BIT MANIPULATION
# ─────────────────────────────────────────
_t("bit_manipulation",
   py="""\
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in {param0}:
            result ^= val
        return result""",
   cpp="""\
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : {param0}) {{
            result ^= val;
        }}
        return result;""")

# ─────────────────────────────────────────
# MATH
# ─────────────────────────────────────────
_t("math",
   py="""\
        # Mathematical approach
        result = 0
        x = {param0}
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result""",
   cpp="""\
        // Mathematical approach
        long long result = 0;
        int x = {param0};
        while (x != 0) {{
            result = result * 10 + x % 10;
            x /= 10;
        }}
        return (int)result;""")

# ─────────────────────────────────────────
# NUMBER THEORY
# ─────────────────────────────────────────
_t("number_theory",
   py="""\
        # Number theory approach
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        result = {param0}[0] if isinstance({param0}, list) else {param0}
        if isinstance({param0}, list):
            for val in {param0}[1:]:
                result = gcd(result, val)
        return result""",
   cpp="""\
        // Number theory approach
        auto gcd_func = [](int a, int b) -> int {{
            while (b) {{ int t = b; b = a % b; a = t; }}
            return a;
        }};
        int result = {param0}[0];
        for (int i = 1; i < (int){param0}.size(); i++) {{
            result = gcd_func(result, {param0}[i]);
        }}
        return result;""")

# ─────────────────────────────────────────
# COMBINATORICS
# ─────────────────────────────────────────
_t("combinatorics",
   py="""\
        # Combinatorics approach
        MOD = 10**9 + 7
        # Compute using factorials or DP
        n = {param0} if isinstance({param0}, int) else len({param0})
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = dp[i-1] * i % MOD
        return dp[n] % MOD""",
   cpp="""\
        // Combinatorics approach
        const int MOD = 1e9 + 7;
        int n = {param0};
        vector<long long> dp(n + 1, 1);
        for (int i = 2; i <= n; i++) {{
            dp[i] = dp[i-1] * i % MOD;
        }}
        return dp[n] % MOD;""")

# ─────────────────────────────────────────
# SORTING
# ─────────────────────────────────────────
_t("sorting",
   py="""\
        # Sort-based approach - O(n log n) time
        {param0}.sort(key=lambda x: x[0] if isinstance(x, (list, tuple)) else x)
        result = [{param0}[0]]
        for i in range(1, len({param0})):
            curr = {param0}[i]
            if isinstance(curr, (list, tuple)) and isinstance(result[-1], (list, tuple)):
                if curr[0] <= result[-1][1]:
                    result[-1] = [result[-1][0], max(result[-1][1], curr[1])]
                else:
                    result.append(curr)
            else:
                result.append(curr)
        return result""",
   cpp="""\
        // Sort-based approach - O(n log n) time
        sort({param0}.begin(), {param0}.end());
        vector<vector<int>> result;
        result.push_back({param0}[0]);
        for (int i = 1; i < (int){param0}.size(); i++) {{
            if ({param0}[i][0] <= result.back()[1]) {{
                result.back()[1] = max(result.back()[1], {param0}[i][1]);
            }} else {{
                result.push_back({param0}[i]);
            }}
        }}
        return result;""",
   cpp_includes="#include <algorithm>")

# ─────────────────────────────────────────
# PREFIX SUM
# ─────────────────────────────────────────
_t("prefix_sum",
   py="""\
        # Prefix sum approach - O(n) time, O(n) space
        prefix = {{0: -1}}
        curr_sum = 0
        result = 0
        target = {param1} if isinstance({param1}, int) else 0
        for i, val in enumerate({param0}):
            curr_sum += val
            if curr_sum - target in prefix:
                result = max(result, i - prefix[curr_sum - target])
            if curr_sum not in prefix:
                prefix[curr_sum] = i
        return result""",
   cpp="""\
        // Prefix sum approach - O(n) time, O(n) space
        unordered_map<int, int> prefix;
        prefix[0] = -1;
        int curr_sum = 0, result = 0;
        int target = {param1};
        for (int i = 0; i < (int){param0}.size(); i++) {{
            curr_sum += {param0}[i];
            if (prefix.count(curr_sum - target)) {{
                result = max(result, i - prefix[curr_sum - target]);
            }}
            if (!prefix.count(curr_sum)) {{
                prefix[curr_sum] = i;
            }}
        }}
        return result;""",
   cpp_includes="#include <unordered_map>\n#include <algorithm>")

# ─────────────────────────────────────────
# DIVIDE AND CONQUER
# ─────────────────────────────────────────
_t("divide_conquer",
   py="""\
        # Divide and conquer approach - O(n log n) time
        def solve(left, right):
            if left >= right:
                return {param0}[left] if left < len({param0}) else 0
            mid = (left + right) // 2
            left_result = solve(left, mid)
            right_result = solve(mid + 1, right)
            return max(left_result, right_result)  # merge step
        
        return solve(0, len({param0}) - 1) if {param0} else {ret_default}""",
   cpp="""\
        // Divide and conquer - O(n log n) time
        function<int(int, int)> solve = [&](int left, int right) -> int {{
            if (left >= right) return left < (int){param0}.size() ? {param0}[left] : 0;
            int mid = (left + right) / 2;
            int leftRes = solve(left, mid);
            int rightRes = solve(mid + 1, right);
            return max(leftRes, rightRes);
        }};
        return {param0}.empty() ? {ret_default} : solve(0, {param0}.size() - 1);""",
   cpp_includes="#include <functional>\n#include <algorithm>")

# ─────────────────────────────────────────
# SIMULATION
# ─────────────────────────────────────────
_t("simulation",
   py="""\
        # Simulation approach - follow the rules step by step
        result = {ret_default}
        for i in range(len({param0}) if isinstance({param0}, list) else {param0}):
            # Simulate each step
            pass
        return result""",
   cpp="""\
        // Simulation approach
        int n = {param0}.size();
        for (int i = 0; i < n; i++) {{
            // Simulate each step
        }}
        return {ret_default};""")

# ─────────────────────────────────────────
# STRING
# ─────────────────────────────────────────
_t("string",
   py="""\
        # String processing approach - O(n) time
        result = []
        for ch in {param0}:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance({ret_default}, bool) else processed""",
   cpp="""\
        // String processing approach - O(n) time
        string processed;
        for (char ch : {param0}) {{
            if (isalnum(ch)) {{
                processed += tolower(ch);
            }}
        }}
        string rev = processed;
        reverse(rev.begin(), rev.end());
        return processed == rev;""",
   cpp_includes="#include <algorithm>\n#include <cctype>")

# ─────────────────────────────────────────
# STRING MATCHING
# ─────────────────────────────────────────
_t("string_matching",
   py="""\
        # String matching (KMP/Rolling Hash) - O(n+m) time
        if not {param1} or not {param0}:
            return {ret_default}
        n, m = len({param0}), len({param1})
        # Build failure function for KMP
        fail = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and {param1}[i] != {param1}[j]:
                j = fail[j-1]
            if {param1}[i] == {param1}[j]:
                j += 1
            fail[i] = j
        # Search
        j = 0
        for i in range(n):
            while j > 0 and {param0}[i] != {param1}[j]:
                j = fail[j-1]
            if {param0}[i] == {param1}[j]:
                j += 1
            if j == m:
                return i - m + 1
        return -1""",
   cpp="""\
        // String matching (KMP) - O(n+m) time
        int n = {param0}.size(), m = {param1}.size();
        if (m == 0) return 0;
        vector<int> fail(m, 0);
        for (int i = 1, j = 0; i < m; i++) {{
            while (j > 0 && {param1}[i] != {param1}[j]) j = fail[j-1];
            if ({param1}[i] == {param1}[j]) j++;
            fail[i] = j;
        }}
        for (int i = 0, j = 0; i < n; i++) {{
            while (j > 0 && {param0}[i] != {param1}[j]) j = fail[j-1];
            if ({param0}[i] == {param1}[j]) j++;
            if (j == m) return i - m + 1;
        }}
        return -1;""")

# ─────────────────────────────────────────
# MATRIX
# ─────────────────────────────────────────
_t("matrix",
   py="""\
        # Matrix manipulation - O(m*n) time
        if not {param0}:
            return {ret_default}
        m, n = len({param0}), len({param0}[0])
        # Process matrix in-place or build result
        for i in range(m):
            for j in range(n):
                pass  # Process {param0}[i][j]
        return {ret_default}""",
   cpp="""\
        // Matrix manipulation - O(m*n) time
        if ({param0}.empty()) return {ret_default};
        int m = {param0}.size(), n = {param0}[0].size();
        for (int i = 0; i < m; i++) {{
            for (int j = 0; j < n; j++) {{
                // Process matrix[i][j]
            }}
        }}
        return {ret_default};""")

# ─────────────────────────────────────────
# GEOMETRY
# ─────────────────────────────────────────
_t("geometry",
   py="""\
        # Geometry approach
        import math
        result = 0
        for i in range(len({param0})):
            for j in range(i + 1, len({param0})):
                dx = {param0}[i][0] - {param0}[j][0]
                dy = {param0}[i][1] - {param0}[j][1]
                dist = math.sqrt(dx*dx + dy*dy)
                result = max(result, dist)
        return result""",
   cpp="""\
        // Geometry approach
        double result = 0;
        for (int i = 0; i < (int){param0}.size(); i++) {{
            for (int j = i + 1; j < (int){param0}.size(); j++) {{
                double dx = {param0}[i][0] - {param0}[j][0];
                double dy = {param0}[i][1] - {param0}[j][1];
                result = max(result, sqrt(dx*dx + dy*dy));
            }}
        }}
        return result;""",
   cpp_includes="#include <cmath>\n#include <algorithm>")

# ─────────────────────────────────────────
# DESIGN (general)
# ─────────────────────────────────────────
_t("design",
   py="""\
        # Design data structure
        # Initialize in __init__, implement operations
        pass""",
   cpp="""\
        // Design data structure
        // Implement operations""")

# ─────────────────────────────────────────
# DESIGN STREAM
# ─────────────────────────────────────────
_t("design_stream",
   py="""\
        # Data stream design
        # Maintain running state for streaming operations
        pass""",
   cpp="""\
        // Data stream design
        // Maintain running state""")

# ─────────────────────────────────────────
# SHORTEST PATH
# ─────────────────────────────────────────
_t("shortest_path",
   py="""\
        # Dijkstra's shortest path - O(E log V)
        import heapq
        from collections import defaultdict
        graph = defaultdict(list)
        edges = {param0} if isinstance({param0}, list) else []
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        n = {param1} if isinstance({param1}, int) else len(graph)
        dist = [float('inf')] * n
        dist[0] = 0
        heap = [(0, 0)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))
        return max(dist) if max(dist) != float('inf') else -1""",
   cpp="""\
        // Dijkstra's shortest path - O(E log V)
        int n = {param1};
        vector<vector<pair<int,int>>> graph(n);
        for (auto& e : {param0}) {{
            graph[e[0]].push_back({{e[1], e[2]}});
            graph[e[1]].push_back({{e[0], e[2]}});
        }}
        vector<int> dist(n, INT_MAX);
        dist[0] = 0;
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
        pq.push({{0, 0}});
        while (!pq.empty()) {{
            auto [d, u] = pq.top(); pq.pop();
            if (d > dist[u]) continue;
            for (auto [v, w] : graph[u]) {{
                if (dist[u] + w < dist[v]) {{
                    dist[v] = dist[u] + w;
                    pq.push({{dist[v], v}});
                }}
            }}
        }}
        return *max_element(dist.begin(), dist.end());""",
   cpp_includes="#include <queue>\n#include <climits>\n#include <algorithm>")

# ─────────────────────────────────────────
# SEGMENT TREE
# ─────────────────────────────────────────
_t("segment_tree",
   py="""\
        # Segment tree for range queries - O(n log n) build, O(log n) query
        n = len({param0})
        tree = [0] * (4 * n)
        
        def build(node, start, end):
            if start == end:
                tree[node] = {param0}[start]
                return
            mid = (start + end) // 2
            build(2*node, start, mid)
            build(2*node+1, mid+1, end)
            tree[node] = tree[2*node] + tree[2*node+1]
        
        def query(node, start, end, l, r):
            if r < start or end < l:
                return 0
            if l <= start and end <= r:
                return tree[node]
            mid = (start + end) // 2
            return query(2*node, start, mid, l, r) + query(2*node+1, mid+1, end, l, r)
        
        build(1, 0, n-1)
        return {ret_default}""",
   cpp="""\
        // Segment tree for range queries
        int n = {param0}.size();
        vector<int> tree(4 * n, 0);
        function<void(int, int, int)> build = [&](int node, int s, int e) {{
            if (s == e) {{ tree[node] = {param0}[s]; return; }}
            int mid = (s + e) / 2;
            build(2*node, s, mid);
            build(2*node+1, mid+1, e);
            tree[node] = tree[2*node] + tree[2*node+1];
        }};
        function<int(int, int, int, int, int)> query = [&](int node, int s, int e, int l, int r) -> int {{
            if (r < s || e < l) return 0;
            if (l <= s && e <= r) return tree[node];
            int mid = (s + e) / 2;
            return query(2*node, s, mid, l, r) + query(2*node+1, mid+1, e, l, r);
        }};
        build(1, 0, n-1);
        return {ret_default};""",
   cpp_includes="#include <functional>")

# ─────────────────────────────────────────
# BINARY INDEXED TREE (Fenwick)
# ─────────────────────────────────────────
_t("binary_indexed_tree",
   py="""\
        # Binary Indexed Tree (Fenwick) - O(log n) update/query
        n = len({param0})
        bit = [0] * (n + 1)
        
        def update(i, delta):
            i += 1
            while i <= n:
                bit[i] += delta
                i += i & (-i)
        
        def query(i):
            i += 1
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s
        
        for i, val in enumerate({param0}):
            update(i, val)
        return {ret_default}""",
   cpp="""\
        // Binary Indexed Tree (Fenwick) - O(log n) update/query
        int n = {param0}.size();
        vector<int> bit(n + 1, 0);
        auto update = [&](int i, int delta) {{
            for (i++; i <= n; i += i & (-i))
                bit[i] += delta;
        }};
        auto query = [&](int i) -> int {{
            int s = 0;
            for (i++; i > 0; i -= i & (-i))
                s += bit[i];
            return s;
        }};
        for (int i = 0; i < n; i++) update(i, {param0}[i]);
        return {ret_default};""")

# ─────────────────────────────────────────
# QUICKSELECT
# ─────────────────────────────────────────
_t("quickselect",
   py="""\
        # Quickselect - O(n) average time
        import random
        def quickselect(arr, k):
            if len(arr) == 1:
                return arr[0]
            pivot = random.choice(arr)
            lows = [x for x in arr if x < pivot]
            highs = [x for x in arr if x > pivot]
            pivots = [x for x in arr if x == pivot]
            if k < len(lows):
                return quickselect(lows, k)
            elif k < len(lows) + len(pivots):
                return pivot
            else:
                return quickselect(highs, k - len(lows) - len(pivots))
        
        k = {param1} if isinstance({param1}, int) else 1
        return quickselect({param0}, len({param0}) - k)""",
   cpp="""\
        // Quickselect - O(n) average time
        int k = {param1};
        nth_element({param0}.begin(), {param0}.begin() + {param0}.size() - k, {param0}.end());
        return {param0}[{param0}.size() - k];""",
   cpp_includes="#include <algorithm>")

# ─────────────────────────────────────────
# MERGE SORT
# ─────────────────────────────────────────
_t("merge_sort",
   py="""\
        # Merge sort approach - O(n log n)
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)
        
        def merge(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i]); i += 1
                else:
                    result.append(right[j]); j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        
        return merge_sort({param0})""",
   cpp="""\
        // Merge sort - O(n log n)
        function<void(int, int)> mergeSort = [&](int l, int r) {{
            if (l >= r) return;
            int mid = (l + r) / 2;
            mergeSort(l, mid);
            mergeSort(mid + 1, r);
            vector<int> temp;
            int i = l, j = mid + 1;
            while (i <= mid && j <= r) {{
                if ({param0}[i] <= {param0}[j]) temp.push_back({param0}[i++]);
                else temp.push_back({param0}[j++]);
            }}
            while (i <= mid) temp.push_back({param0}[i++]);
            while (j <= r) temp.push_back({param0}[j++]);
            for (int k = l; k <= r; k++) {param0}[k] = temp[k - l];
        }};
        mergeSort(0, {param0}.size() - 1);
        return {param0};""",
   cpp_includes="#include <functional>")

# ─────────────────────────────────────────
# RESERVOIR SAMPLING
# ─────────────────────────────────────────
_t("reservoir_sampling",
   py="""\
        # Reservoir sampling - O(n) time, O(1) space
        import random
        result = {param0}
        count = 0
        curr = {param0} if not isinstance({param0}, list) else None
        while curr:
            count += 1
            if random.randint(1, count) == 1:
                result = curr
            curr = getattr(curr, 'next', None)
        return result""",
   cpp="""\
        // Reservoir sampling - O(n) time, O(1) space
        int result = 0, count = 0;
        srand(time(0));
        // Iterate through stream/list
        for (int i = 0; i < (int){param0}.size(); i++) {{
            count++;
            if (rand() % count == 0) result = {param0}[i];
        }}
        return result;""",
   cpp_includes="#include <cstdlib>\n#include <ctime>")

# ─────────────────────────────────────────
# ORDERED SET
# ─────────────────────────────────────────
_t("ordered_set",
   py="""\
        # Ordered set / SortedList - O(n log n) time
        from sortedcontainers import SortedList
        sl = SortedList()
        result = 0
        for val in {param0}:
            pos = sl.bisect_left(val)
            if pos < len(sl):
                result = max(result, sl[pos] - val)
            sl.add(val)
        return result""",
   cpp="""\
        // Ordered set - O(n log n) time
        set<int> ordered;
        int result = 0;
        for (int val : {param0}) {{
            auto it = ordered.lower_bound(val);
            if (it != ordered.end()) {{
                result = max(result, *it - val);
            }}
            ordered.insert(val);
        }}
        return result;""",
   cpp_includes="#include <set>\n#include <algorithm>")

# ─────────────────────────────────────────
# LINE SWEEP
# ─────────────────────────────────────────
_t("line_sweep",
   py="""\
        # Line sweep algorithm - O(n log n) time
        events = []
        for interval in {param0}:
            events.append((interval[0], 1))   # start
            events.append((interval[1], -1))  # end
        events.sort()
        active = 0
        result = 0
        for _, delta in events:
            active += delta
            result = max(result, active)
        return result""",
   cpp="""\
        // Line sweep algorithm - O(n log n) time
        vector<pair<int,int>> events;
        for (auto& interval : {param0}) {{
            events.push_back({{interval[0], 1}});
            events.push_back({{interval[1], -1}});
        }}
        sort(events.begin(), events.end());
        int active = 0, result = 0;
        for (auto& [pos, delta] : events) {{
            active += delta;
            result = max(result, active);
        }}
        return result;""",
   cpp_includes="#include <algorithm>")

# ─────────────────────────────────────────
# QUEUE
# ─────────────────────────────────────────
_t("queue",
   py="""\
        # Queue-based approach - O(n) time
        from collections import deque
        queue = deque()
        for val in {param0}:
            queue.append(val)
        result = []
        while queue:
            result.append(queue.popleft())
        return result""",
   cpp="""\
        // Queue-based approach - O(n) time
        queue<int> q;
        for (int val : {param0}) {{
            q.push(val);
        }}
        vector<int> result;
        while (!q.empty()) {{
            result.push_back(q.front());
            q.pop();
        }}
        return result;""",
   cpp_includes="#include <queue>")

# ─────────────────────────────────────────
# RANDOMIZED
# ─────────────────────────────────────────
_t("randomized",
   py="""\
        # Randomized approach
        import random
        # Fisher-Yates shuffle or random sampling
        arr = list({param0})
        for i in range(len(arr) - 1, 0, -1):
            j = random.randint(0, i)
            arr[i], arr[j] = arr[j], arr[i]
        return arr""",
   cpp="""\
        // Randomized approach (Fisher-Yates shuffle)
        vector<int> arr = {param0};
        srand(time(0));
        for (int i = arr.size() - 1; i > 0; i--) {{
            int j = rand() % (i + 1);
            swap(arr[i], arr[j]);
        }}
        return arr;""",
   cpp_includes="#include <cstdlib>\n#include <ctime>")

# ─────────────────────────────────────────
# ENUMERATION
# ─────────────────────────────────────────
_t("enumeration",
   py="""\
        # Enumeration approach - try all valid candidates
        result = {ret_default}
        for i in range(len({param0}) if isinstance({param0}, list) else {param0}):
            # Check if candidate i is valid
            valid = True
            if valid:
                result = i
                break
        return result""",
   cpp="""\
        // Enumeration approach
        int n = {param0}.size();
        for (int i = 0; i < n; i++) {{
            // Check if candidate is valid
            bool valid = true;
            if (valid) return i;
        }}
        return {ret_default};""")

# ─────────────────────────────────────────
# COUNTING
# ─────────────────────────────────────────
_t("counting",
   py="""\
        # Counting approach - O(n) time
        from collections import Counter
        counts = Counter({param0})
        result = 0
        for val, cnt in counts.items():
            result = max(result, cnt)
        return result""",
   cpp="""\
        // Counting approach - O(n) time
        unordered_map<int, int> counts;
        for (auto& val : {param0}) counts[val]++;
        int result = 0;
        for (auto& [val, cnt] : counts) {{
            result = max(result, cnt);
        }}
        return result;""",
   cpp_includes="#include <unordered_map>\n#include <algorithm>")

# ─────────────────────────────────────────
# RECURSION
# ─────────────────────────────────────────
_t("recursion",
   py="""\
        # Recursive approach
        def solve(n):
            if n <= 1:
                return n
            return solve(n - 1) + solve(n - 2)
        
        return solve({param0} if isinstance({param0}, int) else len({param0}))""",
   cpp="""\
        // Recursive approach with memoization
        unordered_map<int, int> memo;
        function<int(int)> solve = [&](int n) -> int {{
            if (n <= 1) return n;
            if (memo.count(n)) return memo[n];
            return memo[n] = solve(n-1) + solve(n-2);
        }};
        return solve({param0});""",
   cpp_includes="#include <unordered_map>\n#include <functional>")

# ─────────────────────────────────────────
# ARRAY (generic fallback)
# ─────────────────────────────────────────
_t("array",
   py="""\
        # Array processing - O(n) time
        result = {ret_default}
        for i in range(len({param0})):
            # Process element
            pass
        return result""",
   cpp="""\
        // Array processing - O(n) time
        for (int i = 0; i < (int){param0}.size(); i++) {{
            // Process element
        }}
        return {ret_default};""")


# ═══════════════════════════════════════════════════════════════════
# DESIGN PROBLEM TEMPLATES
# ═══════════════════════════════════════════════════════════════════

DESIGN_TEMPLATES = {
    "LRUCache": {
        "py": '''\
class LRUCache:
    def __init__(self, capacity: int):
        from collections import OrderedDict
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)''',
        "cpp": '''\
class LRUCache {
    int cap;
    list<pair<int,int>> lst;
    unordered_map<int, list<pair<int,int>>::iterator> mp;
public:
    LRUCache(int capacity) : cap(capacity) {}
    
    int get(int key) {
        if (!mp.count(key)) return -1;
        lst.splice(lst.end(), lst, mp[key]);
        return mp[key]->second;
    }
    
    void put(int key, int value) {
        if (mp.count(key)) {
            mp[key]->second = value;
            lst.splice(lst.end(), lst, mp[key]);
            return;
        }
        if ((int)lst.size() == cap) {
            mp.erase(lst.front().first);
            lst.pop_front();
        }
        lst.push_back({key, value});
        mp[key] = prev(lst.end());
    }
};''',
    },
    "MinStack": {
        "py": '''\
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1] if self.min_stack else val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]''',
        "cpp": '''\
class MinStack {
    stack<int> st, minSt;
public:
    MinStack() {}
    void push(int val) {
        st.push(val);
        minSt.push(minSt.empty() ? val : min(val, minSt.top()));
    }
    void pop() { st.pop(); minSt.pop(); }
    int top() { return st.top(); }
    int getMin() { return minSt.top(); }
};''',
    },
}


# ═══════════════════════════════════════════════════════════════════
# PUBLIC API
# ═══════════════════════════════════════════════════════════════════

def get_template(pattern):
    """Get the template dict for a pattern, or fallback."""
    return TEMPLATES.get(pattern, TEMPLATES.get("array"))


def get_design_template(class_name):
    """Get a design problem template by class name, or None."""
    return DESIGN_TEMPLATES.get(class_name)


def fill_template(template_body, **kwargs):
    """Fill placeholders in a template body.
    
    Available placeholders: {method_name}, {params}, {return_type},
    {ret_default}, {param0}, {param1}, {param2}, {ptype0}, {ptype1}
    
    Template strings use {{ and }} for literal braces (C++ code).
    After placeholder substitution, these are unescaped to { and }.
    """
    result = template_body
    for key, val in kwargs.items():
        placeholder = "{" + key + "}"
        result = result.replace(placeholder, str(val))
    # Unescape doubled braces to literal braces (for C++ code)
    result = result.replace("{{", "{").replace("}}", "}")
    return result


def generate_solution_py(pattern, methods, class_name, is_design, kb_solution=None):
    """Generate a complete Python solution file.
    
    Args:
        pattern: classified pattern name
        methods: list of method dicts from sig_parser
        class_name: e.g. "Solution" or "LRUCache"
        is_design: True for multi-method design problems
        kb_solution: existing KB solution code (takes priority)
    
    Returns:
        Complete Python solution as string
    """
    if kb_solution:
        return kb_solution
    
    # Design problem with known template
    if is_design:
        design_tmpl = get_design_template(class_name)
        if design_tmpl:
            return design_tmpl["py"]
    
    # Build from template
    template = get_template(pattern)
    if not template:
        template = TEMPLATES["array"]
    
    non_init = [m for m in methods if not m.get("is_init")]
    if not non_init:
        # Fallback: generate stub
        return f"class {class_name}:\n    pass"
    
    lines = [f"class {class_name}:"]
    
    # For design problems, generate __init__ and all methods
    if is_design:
        init_methods = [m for m in methods if m.get("is_init")]
        if init_methods:
            init_m = init_methods[0]
            params_str = ", ".join(f"{n}: {t}" for n, t in init_m["params"])
            if params_str:
                params_str = ", " + params_str
            lines.append(f"    def __init__(self{params_str}):")
            lines.append("        # Initialize data structure")
            for n, t in init_m["params"]:
                lines.append(f"        self.{n} = {n}")
            if not init_m["params"]:
                lines.append("        pass")
            lines.append("")
        
        for m in non_init:
            params_str = ", ".join(f"{n}: {t}" for n, t in m["params"])
            if params_str:
                params_str = ", " + params_str
            ret_str = f" -> {m['return_type']}" if m["return_type"] != "None" else " -> None"
            lines.append(f"    def {m['name']}(self{params_str}){ret_str}:")
            from sig_parser import py_default
            lines.append(f"        return {py_default(m['return_type'])}")
            lines.append("")
    else:
        m = non_init[0]
        params_str = ", ".join(f"{n}: {t}" for n, t in m["params"])
        if params_str:
            params_str = ", " + params_str
        ret_str = f" -> {m['return_type']}" if m["return_type"] else ""
        lines.append(f"    def {m['name']}(self{params_str}){ret_str}:")
        
        # Fill template
        from sig_parser import py_default
        kwargs = {
            "method_name": m["name"],
            "return_type": m["return_type"] or "None",
            "ret_default": py_default(m["return_type"]),
        }
        for i, (pn, pt) in enumerate(m["params"]):
            kwargs[f"param{i}"] = pn
            kwargs[f"ptype{i}"] = pt
        # Ensure param0/param1 exist even if no params
        for i in range(3):
            if f"param{i}" not in kwargs:
                kwargs[f"param{i}"] = kwargs.get("param0", "nums")
        
        body = fill_template(template["py_body"], **kwargs)
        lines.append(body)
    
    return "\n".join(lines)


def generate_solution_cpp(pattern, methods, class_name, is_design, kb_solution=None):
    """Generate a complete C++ solution file.
    
    Returns:
        Complete C++ solution as string
    """
    if kb_solution:
        return kb_solution
    
    # Design problem with known template
    if is_design:
        design_tmpl = get_design_template(class_name)
        if design_tmpl:
            return design_tmpl["cpp"]
    
    template = get_template(pattern)
    if not template:
        template = TEMPLATES["array"]
    
    from sig_parser import py_type_to_cpp, cpp_default, cpp_param_decl
    
    non_init = [m for m in methods if not m.get("is_init")]
    if not non_init:
        return f"class {class_name} {{\npublic:\n    // Design problem stub\n}};"
    
    # Collect includes
    includes = set()
    includes.add("#include <vector>")
    includes.add("#include <string>")
    if template.get("cpp_includes"):
        for inc in template["cpp_includes"].split("\n"):
            includes.add(inc.strip())
    
    lines = list(sorted(includes))
    lines.append("using namespace std;")
    lines.append("")
    
    if is_design:
        lines.append(f"class {class_name} {{")
        lines.append("public:")
        
        init_methods = [m for m in methods if m.get("is_init")]
        if init_methods:
            init_m = init_methods[0]
            params = ", ".join(cpp_param_decl(n, t) for n, t in init_m["params"])
            lines.append(f"    {class_name}({params}) {{")
            lines.append("        // Initialize")
            lines.append("    }")
            lines.append("")
        
        for m in non_init:
            cpp_ret = py_type_to_cpp(m["return_type"])
            params = ", ".join(cpp_param_decl(n, t) for n, t in m["params"])
            lines.append(f"    {cpp_ret} {m['name']}({params}) {{")
            lines.append(f"        return {cpp_default(cpp_ret)};")
            lines.append("    }")
            lines.append("")
        
        lines.append("};")
    else:
        m = non_init[0]
        cpp_ret = py_type_to_cpp(m["return_type"])
        params = ", ".join(cpp_param_decl(n, t) for n, t in m["params"])
        
        lines.append(f"class {class_name} {{")
        lines.append("public:")
        lines.append(f"    {cpp_ret} {m['name']}({params}) {{")
        
        kwargs = {
            "method_name": m["name"],
            "return_type": cpp_ret,
            "ret_default": cpp_default(cpp_ret),
        }
        for i, (pn, pt) in enumerate(m["params"]):
            kwargs[f"param{i}"] = pn
            kwargs[f"ptype{i}"] = py_type_to_cpp(pt)
        for i in range(3):
            if f"param{i}" not in kwargs:
                kwargs[f"param{i}"] = kwargs.get("param0", "nums")
        
        body = fill_template(template["cpp_body"], **kwargs)
        lines.append(body)
        lines.append("    }")
        lines.append("};")
    
    return "\n".join(lines)
