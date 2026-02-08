#!/usr/bin/env python3
"""
solutions_kb.py
===============
Knowledge base of optimal solutions for LeetCode problems 1-500.
Maps problem ID -> solution data dict with keys:
  - code: Python solution code
  - pattern: Algorithm pattern name
  - time: Time complexity
  - space: Space complexity
  - approach: Explanation of approach
  - pseudocode: Step-by-step pseudocode
  - mermaid: Mermaid flowchart (optional)
  - walkthrough: Dry-run table (optional)
  - animation_frames: Multi-frame mermaid for complex problems (optional)
"""

SOLUTIONS_KB = {

# ──────────────────────────────────────────
# Problem 1: Two Sum
# ──────────────────────────────────────────
1: {
    "code": """class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []""",
    "pattern": "Hash Map Lookup",
    "time": "O(n)",
    "space": "O(n)",
    "approach": "**Key Insight:** For each element, check if `target - num` exists in a hash map. One-pass solution.\n\nStore each number's index as we iterate. For every element, compute its complement and check the map.",
    "pseudocode": "1. Create empty hash map seen = {}\n2. For each (i, num) in nums:\n   a. complement = target - num\n   b. If complement in seen: return [seen[complement], i]\n   c. seen[num] = i",
    "mermaid": """```mermaid
flowchart TD
    A[Start: seen = empty map] --> B[For each i, num in nums]
    B --> C[complement = target - num]
    C --> D{complement in seen?}
    D -- Yes --> E[Return seen_complement, i]
    D -- No --> F[seen_num = i]
    F --> B
    E --> G[Done]
```""",
    "walkthrough": """**Input:** `nums = [2, 7, 11, 15]`, `target = 9`

| Step | i | num | complement | seen | Action |
|------|---|-----|-----------|------|--------|
| 1 | 0 | 2 | 7 | {} | Store {2:0} |
| 2 | 1 | 7 | 2 | {2:0} | Found! Return [0,1] |""",
},

# ──────────────────────────────────────────
# Problem 2: Add Two Numbers
# ──────────────────────────────────────────
2: {
    "code": """class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next""",
    "pattern": "Linked List Math",
    "time": "O(max(m,n))",
    "space": "O(max(m,n))",
    "approach": "**Key Insight:** Digits are in reverse order, so add digit-by-digit from head with a carry variable.\n\nUse a dummy head node. Iterate both lists simultaneously, computing sum + carry at each position.",
    "pseudocode": "1. dummy = ListNode(0), curr = dummy, carry = 0\n2. While l1 or l2 or carry:\n   a. v1 = l1.val or 0, v2 = l2.val or 0\n   b. total = v1 + v2 + carry\n   c. carry = total // 10\n   d. curr.next = ListNode(total % 10)\n   e. Advance pointers\n3. Return dummy.next",
    "mermaid": """```mermaid
flowchart TD
    A[Start: dummy head, carry=0] --> B{l1 or l2 or carry?}
    B -- Yes --> C[Sum digits + carry]
    C --> D[carry = sum/10, digit = sum%10]
    D --> E[Append new node]
    E --> F[Advance pointers]
    F --> B
    B -- No --> G[Return dummy.next]
```""",
    "walkthrough": """**Input:** `l1 = [2,4,3]`, `l2 = [5,6,4]`

| Step | v1 | v2 | carry_in | total | digit | carry_out | Result |
|------|----|----|----------|-------|-------|-----------|--------|
| 1 | 2 | 5 | 0 | 7 | 7 | 0 | [7] |
| 2 | 4 | 6 | 0 | 10 | 0 | 1 | [7,0] |
| 3 | 3 | 4 | 1 | 8 | 8 | 0 | [7,0,8] |""",
    "animation_frames": """**Linked List Addition Step-by-Step:**

**Step 1:** Process first digits (carry=0)

```mermaid
flowchart LR
    subgraph L1[List 1]
        A1["2 *"] --> A2[4] --> A3[3]
    end
    subgraph L2[List 2]
        B1["5 *"] --> B2[6] --> B3[4]
    end
    subgraph Result
        R1["7"]
    end
```

**Step 2:** Process second digits (carry=0)

```mermaid
flowchart LR
    subgraph L1[List 1]
        A1[2] --> A2["4 *"] --> A3[3]
    end
    subgraph L2[List 2]
        B1[5] --> B2["6 *"] --> B3[4]
    end
    subgraph Result
        R1[7] --> R2["0 carry=1"]
    end
```

**Step 3:** Process third digits (carry=1)

```mermaid
flowchart LR
    subgraph L1[List 1]
        A1[2] --> A2[4] --> A3["3 *"]
    end
    subgraph L2[List 2]
        B1[5] --> B2[6] --> B3["4 *"]
    end
    subgraph Result
        R1[7] --> R2[0] --> R3[8]
    end
```""",
},

# ──────────────────────────────────────────
# Problem 3: Longest Substring Without Repeating Characters
# ──────────────────────────────────────────
3: {
    "code": """class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_len = 0
        for right, ch in enumerate(s):
            if ch in char_index and char_index[ch] >= left:
                left = char_index[ch] + 1
            char_index[ch] = right
            max_len = max(max_len, right - left + 1)
        return max_len""",
    "pattern": "Sliding Window",
    "time": "O(n)",
    "space": "O(min(n,m))",
    "approach": "**Key Insight:** Maintain a window [left, right] with unique characters. When a duplicate is found, jump left past the previous occurrence.\n\nUse a hash map to track last-seen index of each character.",
    "pseudocode": "1. char_index = {}, left = 0, max_len = 0\n2. For right, ch in enumerate(s):\n   a. If ch in map and map[ch] >= left: left = map[ch] + 1\n   b. map[ch] = right\n   c. max_len = max(max_len, right - left + 1)\n3. Return max_len",
    "mermaid": """```mermaid
flowchart TD
    A[Start: left=0, max_len=0] --> B[Move right through string]
    B --> C{Duplicate in window?}
    C -- Yes --> D[Jump left past duplicate]
    C -- No --> E[Keep left]
    D --> F[Update char map and max_len]
    E --> F
    F --> G{More chars?}
    G -- Yes --> B
    G -- No --> H[Return max_len]
```""",
    "walkthrough": """**Input:** `s = "abcabcbb"`

| Step | right | char | left | Window | max_len |
|------|-------|------|------|--------|---------|
| 1 | 0 | a | 0 | "a" | 1 |
| 2 | 1 | b | 0 | "ab" | 2 |
| 3 | 2 | c | 0 | "abc" | 3 |
| 4 | 3 | a | 1 | "bca" | 3 |
| 5 | 4 | b | 2 | "cab" | 3 |""",
},

# ──────────────────────────────────────────
# Problem 4: Median of Two Sorted Arrays
# ──────────────────────────────────────────
4: {
    "code": """class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2
            j = (m + n + 1) // 2 - i
            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')
            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                return max(left1, left2)
            elif left1 > right2:
                hi = i - 1
            else:
                lo = i + 1
        return 0.0""",
    "pattern": "Binary Search",
    "time": "O(log(min(m,n)))",
    "space": "O(1)",
    "approach": "**Key Insight:** Binary search on the shorter array to find the correct partition. At the correct partition, all left elements <= all right elements.\n\nBinary search the partition index `i` in the shorter array. Compute `j` for the other array such that left half has `(m+n+1)//2` elements total.",
    "pseudocode": "1. Ensure nums1 is shorter\n2. Binary search i in [0, m]\n3. j = (m+n+1)//2 - i\n4. Check left1<=right2 and left2<=right1\n5. If valid: compute median from boundary elements\n6. Else adjust lo/hi",
    "mermaid": """```mermaid
flowchart TD
    A[Ensure nums1 is shorter] --> B[Binary search: lo=0, hi=m]
    B --> C[i = mid of lo,hi]
    C --> D[j = half - i]
    D --> E{left1 <= right2 AND left2 <= right1?}
    E -- Yes --> F[Compute median from boundaries]
    E -- No left1 too big --> G[hi = i - 1]
    E -- No left2 too big --> H[lo = i + 1]
    G --> B
    H --> B
    F --> I[Return median]
```""",
    "animation_frames": """**Binary Search Partition Animation:**

**Step 1:** Initial state - search full range of shorter array

```mermaid
flowchart LR
    subgraph nums1["nums1: [1, 3]"]
        direction LR
        N1A[1] --> N1B[3]
    end
    subgraph nums2["nums2: [2]"]
        N2A[2]
    end
    Note["lo=0 hi=2 i=1 j=1"]
```

**Step 2:** Check partition i=1, j=1: left=[1,2] right=[3] -- Valid!

```mermaid
flowchart LR
    subgraph LeftHalf[Left Half]
        L1[1] --> L2[2]
    end
    subgraph RightHalf[Right Half]
        R1[3]
    end
    LeftHalf -->|"max=2"| M["Median = 2"]
    RightHalf -->|"min=3"| M
```""",
},

# ──────────────────────────────────────────
# Problem 5: Longest Palindromic Substring
# ──────────────────────────────────────────
5: {
    "code": """class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        result = ""
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)
            result = max(result, odd, even, key=len)
        return result""",
    "pattern": "Expand Around Center",
    "time": "O(n^2)",
    "space": "O(1)",
    "approach": "**Key Insight:** A palindrome expands symmetrically from its center. Try each index (and each pair) as a center and expand outward.\n\nFor each position, expand for both odd-length and even-length palindromes. Track the longest found.",
    "pseudocode": "1. For each index i in s:\n   a. Expand around (i, i) for odd palindromes\n   b. Expand around (i, i+1) for even palindromes\n   c. Update result if longer found\n2. Return longest palindrome",
    "mermaid": """```mermaid
flowchart TD
    A[For each center i] --> B[Expand odd: l=i, r=i]
    A --> C[Expand even: l=i, r=i+1]
    B --> D[While s_l == s_r: expand]
    C --> D
    D --> E[Track longest palindrome]
    E --> F{More centers?}
    F -- Yes --> A
    F -- No --> G[Return result]
```""",
    "animation_frames": """**Expand Around Center Animation for s = "babad":**

**Step 1:** Center at index 0 ("b")

```mermaid
flowchart LR
    B0["[b]"] --> A1[a] --> B2[b] --> A3[a] --> D4[d]
```

Result so far: "b" (length 1)

**Step 2:** Center at index 1 ("a"), expand to check s[0]==s[2]?  b==b? Yes!

```mermaid
flowchart LR
    B0["b"] --> A1["[a]"] --> B2["b"]
    A3[a] --> D4[d]
```

Palindrome found: "bab" (length 3)

**Step 3:** Center at index 2 ("b"), expand to check s[1]==s[3]? a==a? Yes!

```mermaid
flowchart LR
    B0[b] --> A1["a"] --> B2["[b]"] --> A3["a"]
    D4[d]
```

Palindrome found: "aba" (length 3, same as "bab")""",
},

# ──────────────────────────────────────────
# Problem 6: Zigzag Conversion
# ──────────────────────────────────────────
6: {
    "code": """class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [''] * numRows
        idx, step = 0, 1
        for ch in s:
            rows[idx] += ch
            if idx == 0:
                step = 1
            elif idx == numRows - 1:
                step = -1
            idx += step
        return ''.join(rows)""",
    "pattern": "String Simulation",
    "time": "O(n)",
    "space": "O(n)",
    "approach": "**Key Insight:** Simulate the zigzag pattern by maintaining row buckets and bouncing the row index up and down.\n\nCreate `numRows` string builders. Iterate through characters, appending to the current row and reversing direction at boundaries.",
    "pseudocode": "1. rows = [''] * numRows, idx=0, step=1\n2. For each char in s:\n   a. rows[idx] += char\n   b. If idx==0: step=1; if idx==numRows-1: step=-1\n   c. idx += step\n3. Return ''.join(rows)",
    "mermaid": """```mermaid
flowchart TD
    A[Create numRows empty strings] --> B[idx=0, step=1]
    B --> C[For each char in s]
    C --> D[Append char to rows_idx]
    D --> E{At boundary?}
    E -- Top --> F[step = 1]
    E -- Bottom --> G[step = -1]
    E -- No --> H[Keep step]
    F --> I[idx += step]
    G --> I
    H --> I
    I --> C
```""",
},

# ──────────────────────────────────────────
# Problem 7: Reverse Integer
# ──────────────────────────────────────────
7: {
    "code": """class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        result = 0
        while x:
            result = result * 10 + x % 10
            x //= 10
        result *= sign
        return result if -2**31 <= result <= 2**31 - 1 else 0""",
    "pattern": "Math",
    "time": "O(log x)",
    "space": "O(1)",
    "approach": "Extract digits from the end using modulo, build the reversed number. Check 32-bit overflow before returning.",
    "pseudocode": "1. Handle sign, work with abs(x)\n2. While x > 0: result = result*10 + x%10, x //= 10\n3. Restore sign, check [-2^31, 2^31-1]",
    "mermaid": """```mermaid
flowchart TD
    A[Save sign, x = abs x] --> B{x > 0?}
    B -- Yes --> C[result = result*10 + x%10]
    C --> D[x = x // 10]
    D --> B
    B -- No --> E[Restore sign]
    E --> F{In 32-bit range?}
    F -- Yes --> G[Return result]
    F -- No --> H[Return 0]
```""",
},

# ──────────────────────────────────────────
# Problem 8: String to Integer (atoi)
# ──────────────────────────────────────────
8: {
    "code": """class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        i = 0
        if s[0] in '+-':
            sign = -1 if s[0] == '-' else 1
            i = 1
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        result *= sign
        return max(-2**31, min(result, 2**31 - 1))""",
    "pattern": "String Parsing",
    "time": "O(n)",
    "space": "O(1)",
    "approach": "Strip whitespace, handle optional sign, parse digits one by one, clamp to 32-bit integer range.",
    "pseudocode": "1. Strip leading whitespace\n2. Check for +/- sign\n3. Parse consecutive digits\n4. Clamp to [-2^31, 2^31-1]",
    "mermaid": """```mermaid
flowchart TD
    A[Strip whitespace] --> B{Sign char?}
    B -- Yes --> C[Record sign, advance]
    B -- No --> D[sign = 1]
    C --> E[Parse digits]
    D --> E
    E --> F[Clamp to 32-bit range]
    F --> G[Return result]
```""",
},

# ──────────────────────────────────────────
# Problem 9: Palindrome Number
# ──────────────────────────────────────────
9: {
    "code": """class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        return x == reversed_half or x == reversed_half // 10""",
    "pattern": "Math",
    "time": "O(log n)",
    "space": "O(1)",
    "approach": "**Key Insight:** Reverse only the second half of the number and compare with the first half. No string conversion needed.\n\nNegatives and multiples of 10 (except 0) are not palindromes.",
    "pseudocode": "1. If x < 0 or (x%10==0 and x!=0): return False\n2. Reverse second half until reversed >= x\n3. Return x == reversed or x == reversed//10",
    "mermaid": """```mermaid
flowchart TD
    A[x negative or ends in 0?] --> |Yes| B[Return False]
    A --> |No| C[Reverse second half]
    C --> D{x > reversed?}
    D -- Yes --> E[reversed = reversed*10 + x%10, x//=10]
    E --> D
    D -- No --> F{x == reversed OR x == reversed//10?}
    F -- Yes --> G[Return True]
    F -- No --> H[Return False]
```""",
},

# ──────────────────────────────────────────
# Problem 10: Regular Expression Matching
# ──────────────────────────────────────────
10: {
    "code": """class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]  # zero occurrences
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]""",
    "pattern": "Dynamic Programming",
    "time": "O(m*n)",
    "space": "O(m*n)",
    "approach": "**Key Insight:** Use 2D DP where `dp[i][j]` = whether `s[0..i-1]` matches `p[0..j-1]`.\n\nHandle three cases: (1) exact char match or '.', (2) '*' with zero occurrences, (3) '*' with one+ occurrences.",
    "pseudocode": "1. dp[0][0] = True\n2. Fill first row: p[j-1]=='*' means dp[0][j] = dp[0][j-2]\n3. For each (i,j):\n   - If p[j-1]=='*': zero match or extend\n   - If p[j-1]=='.' or match: dp[i-1][j-1]\n4. Return dp[m][n]",
    "mermaid": """```mermaid
flowchart TD
    A[Init dp table m+1 x n+1] --> B[dp_0_0 = True]
    B --> C[Fill first row for star patterns]
    C --> D[For each i,j]
    D --> E{p_j is star?}
    E -- Yes --> F[Zero match: dp_i_j-2]
    E -- Yes --> G[Extend: dp_i-1_j if char matches]
    E -- No --> H{Char match or dot?}
    H -- Yes --> I[dp_i-1_j-1]
    H -- No --> J[dp_i_j = False]
    F --> D
    G --> D
    I --> D
    J --> D
```""",
    "animation_frames": """**DP Table Fill for s="aa", p="a*":**

**Step 1:** Initialize dp table

```mermaid
flowchart TD
    subgraph DPTable["DP Table"]
        R0["dp[0]: T F T"]
        R1["dp[1]: F ? ?"]
        R2["dp[2]: F ? ?"]
    end
```

**Step 2:** Fill dp[1][1]: p[0]='a' matches s[0]='a', dp[0][0]=T

```mermaid
flowchart TD
    subgraph DPTable["DP Table"]
        R0["dp[0]: T F T"]
        R1["dp[1]: F T ?"]
        R2["dp[2]: F ? ?"]
    end
```

**Step 3:** Fill dp[1][2]: p[1]='*', zero match dp[1][0]=F, extend dp[0][2]=T

```mermaid
flowchart TD
    subgraph DPTable["DP Table"]
        R0["dp[0]: T F T"]
        R1["dp[1]: F T T"]
        R2["dp[2]: F ? ?"]
    end
```

**Step 4:** Fill dp[2][2]: p[1]='*', extend dp[1][2]=T. Result: True

```mermaid
flowchart TD
    subgraph DPTable["DP Table Complete"]
        R0["dp[0]: T F T"]
        R1["dp[1]: F T T"]
        R2["dp[2]: F F T"]
    end
```""",
},

# ──────────────────────────────────────────
# Problem 11: Container With Most Water
# ──────────────────────────────────────────
11: {
    "code": """class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area""",
    "pattern": "Two Pointers",
    "time": "O(n)",
    "space": "O(1)",
    "approach": "**Key Insight:** Start with widest container (left=0, right=end). Move the shorter pointer inward since moving the taller one can only decrease area.",
    "pseudocode": "1. left=0, right=n-1, max_area=0\n2. While left < right:\n   a. area = min(h[left], h[right]) * (right-left)\n   b. Update max_area\n   c. Move shorter pointer inward\n3. Return max_area",
    "mermaid": """```mermaid
flowchart TD
    A[left=0, right=n-1] --> B{left < right?}
    B -- Yes --> C[Compute area]
    C --> D[Update max_area]
    D --> E{height_left < height_right?}
    E -- Yes --> F[left++]
    E -- No --> G[right--]
    F --> B
    G --> B
    B -- No --> H[Return max_area]
```""",
},

# ──────────────────────────────────────────
# Problem 12: Integer to Roman
# ──────────────────────────────────────────
12: {
    "code": """class Solution:
    def intToRoman(self, num: int) -> str:
        vals = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),
                (100,'C'),(90,'XC'),(50,'L'),(40,'XL'),
                (10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
        result = []
        for val, sym in vals:
            while num >= val:
                result.append(sym)
                num -= val
        return ''.join(result)""",
    "pattern": "Greedy",
    "time": "O(1)",
    "space": "O(1)",
    "approach": "Greedy: subtract the largest possible Roman numeral value at each step. Use a table of value-symbol pairs including subtractive forms.",
    "pseudocode": "1. Define value-symbol pairs in descending order\n2. For each pair: while num >= val: append symbol, subtract val\n3. Return joined result",
    "mermaid": """```mermaid
flowchart TD
    A[Start with num] --> B[For each val,sym pair]
    B --> C{num >= val?}
    C -- Yes --> D[Append sym, num -= val]
    D --> C
    C -- No --> E[Next pair]
    E --> B
```""",
},

# ──────────────────────────────────────────
# Problem 13: Roman to Integer
# ──────────────────────────────────────────
13: {
    "code": """class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]
        return result""",
    "pattern": "String Parsing",
    "time": "O(n)",
    "space": "O(1)",
    "approach": "If a smaller value appears before a larger one, subtract it; otherwise add it.",
    "pseudocode": "1. Map each Roman char to value\n2. For each char: if next char is larger, subtract; else add\n3. Return total",
    "mermaid": """```mermaid
flowchart TD
    A[result = 0] --> B[For each char i in s]
    B --> C{current < next?}
    C -- Yes --> D[result -= current]
    C -- No --> E[result += current]
    D --> B
    E --> B
```""",
},

# ──────────────────────────────────────────
# Problem 14: Longest Common Prefix
# ──────────────────────────────────────────
14: {
    "code": """class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix""",
    "pattern": "String",
    "time": "O(S) where S = sum of all chars",
    "space": "O(1)",
    "approach": "Start with first string as prefix. Shrink it until every other string starts with it.",
    "pseudocode": "1. prefix = strs[0]\n2. For each other string s:\n   While s doesn't start with prefix: remove last char\n3. Return prefix",
    "mermaid": """```mermaid
flowchart TD
    A[prefix = strs_0] --> B[For each string s]
    B --> C{s starts with prefix?}
    C -- Yes --> D[Next string]
    C -- No --> E[Shorten prefix by 1]
    E --> C
    D --> B
```""",
},

# ──────────────────────────────────────────
# Problem 15: 3Sum
# ──────────────────────────────────────────
15: {
    "code": """class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result""",
    "pattern": "Two Pointers",
    "time": "O(n^2)",
    "space": "O(1) extra",
    "approach": "**Key Insight:** Sort the array. Fix one element, then use two pointers on the remainder to find pairs summing to its negative.\n\nSkip duplicates at all levels to avoid duplicate triplets.",
    "pseudocode": "1. Sort nums\n2. For each i (skip duplicates):\n   left = i+1, right = n-1\n   While left < right:\n     If sum < 0: left++\n     If sum > 0: right--\n     If sum == 0: record, skip duplicates",
    "mermaid": """```mermaid
flowchart TD
    A[Sort array] --> B[Fix element at i]
    B --> C[left = i+1, right = n-1]
    C --> D{left < right?}
    D -- Yes --> E[sum = nums_i + nums_left + nums_right]
    E --> F{sum == 0?}
    F -- Yes --> G[Record triplet, skip dupes]
    F -- sum < 0 --> H[left++]
    F -- sum > 0 --> I[right--]
    G --> D
    H --> D
    I --> D
    D -- No --> J[Next i]
    J --> B
```""",
},

# ──────────────────────────────────────────
# Problem 16: 3Sum Closest
# ──────────────────────────────────────────
16: {
    "code": """class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(closest - target):
                    closest = total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total
        return closest""",
    "pattern": "Two Pointers",
    "time": "O(n^2)",
    "space": "O(1)",
    "approach": "Sort + two pointers. Track the closest sum seen so far. Adjust pointers based on comparison with target.",
    "pseudocode": "1. Sort nums, closest = inf\n2. Fix i, two pointers left/right\n3. Track closest sum, adjust pointers\n4. Return closest",
    "mermaid": """```mermaid
flowchart TD
    A[Sort array] --> B[For each i]
    B --> C[Two pointers left, right]
    C --> D[Compute sum]
    D --> E[Update closest if better]
    E --> F{sum vs target}
    F -- Less --> G[left++]
    F -- Greater --> H[right--]
    F -- Equal --> I[Return target]
```""",
},

# ──────────────────────────────────────────
# Problem 17: Letter Combinations of a Phone Number
# ──────────────────────────────────────────
17: {
    "code": """class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        phone = {'2':'abc','3':'def','4':'ghi','5':'jkl',
                 '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        result = []
        def backtrack(idx, path):
            if idx == len(digits):
                result.append(''.join(path))
                return
            for ch in phone[digits[idx]]:
                path.append(ch)
                backtrack(idx + 1, path)
                path.pop()
        backtrack(0, [])
        return result""",
    "pattern": "Backtracking",
    "time": "O(4^n) where n = len(digits)",
    "space": "O(n)",
    "approach": "Classic backtracking: for each digit, try all mapped letters and recurse to the next digit.",
    "pseudocode": "1. Map digits to letters\n2. Backtrack(idx, path):\n   If idx == len(digits): record path\n   For each letter of digits[idx]: append, recurse, pop",
    "mermaid": """```mermaid
flowchart TD
    A[Start with digits] --> B[backtrack idx=0, path=empty]
    B --> C{idx == len digits?}
    C -- Yes --> D[Add path to result]
    C -- No --> E[For each letter of digit]
    E --> F[Append letter to path]
    F --> G[Recurse idx+1]
    G --> H[Pop letter from path]
    H --> E
```""",
},

# ──────────────────────────────────────────
# Problem 18: 4Sum
# ──────────────────────────────────────────
18: {
    "code": """class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return result""",
    "pattern": "Two Pointers",
    "time": "O(n^3)",
    "space": "O(1) extra",
    "approach": "Extension of 3Sum: fix two elements, use two pointers for the remaining two. Skip duplicates at all levels.",
    "pseudocode": "1. Sort nums\n2. Fix i, fix j > i\n3. Two pointers left=j+1, right=n-1\n4. Find quads summing to target, skip dupes",
    "mermaid": """```mermaid
flowchart TD
    A[Sort array] --> B[Fix i and j]
    B --> C[Two pointers left, right]
    C --> D{sum == target?}
    D -- Yes --> E[Record quad, skip dupes]
    D -- Less --> F[left++]
    D -- Greater --> G[right--]
```""",
},

# ──────────────────────────────────────────
# Problem 19: Remove Nth Node From End of List
# ──────────────────────────────────────────
19: {
    "code": """class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next""",
    "pattern": "Fast and Slow Pointers",
    "time": "O(L) where L = list length",
    "space": "O(1)",
    "approach": "**Key Insight:** Use two pointers with a gap of n+1. When fast reaches end, slow is just before the node to remove.\n\nDummy head handles edge case of removing the first node.",
    "pseudocode": "1. dummy -> head, fast = slow = dummy\n2. Advance fast by n+1 steps\n3. Move both until fast is null\n4. slow.next = slow.next.next\n5. Return dummy.next",
    "mermaid": """```mermaid
flowchart TD
    A[dummy -> head] --> B[Advance fast n+1 steps]
    B --> C{fast is null?}
    C -- No --> D[Move fast and slow together]
    D --> C
    C -- Yes --> E[slow.next = slow.next.next]
    E --> F[Return dummy.next]
```""",
    "animation_frames": """**Two-Pointer Gap Animation for n=2, list=[1,2,3,4,5]:**

**Step 1:** Advance fast 3 steps ahead of slow

```mermaid
flowchart LR
    D["dummy(S)"] --> N1[1] --> N2[2] --> N3["3(F)"] --> N4[4] --> N5[5]
```

**Step 2:** Move both until fast reaches end

```mermaid
flowchart LR
    D[dummy] --> N1[1] --> N2[2] --> N3["3(S)"] --> N4[4] --> N5["5(F)"]
```

**Step 3:** Remove slow.next (node 4)

```mermaid
flowchart LR
    D[dummy] --> N1[1] --> N2[2] --> N3["3(S)"] --> N5[5]
```""",
},

# ──────────────────────────────────────────
# Problem 20: Valid Parentheses
# ──────────────────────────────────────────
20: {
    "code": """class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack""",
    "pattern": "Stack",
    "time": "O(n)",
    "space": "O(n)",
    "approach": "Use a stack. Push opening brackets, pop on matching closing brackets. Invalid if mismatch or stack not empty at end.",
    "pseudocode": "1. For each char:\n   If closing: check stack top matches, pop\n   If opening: push\n2. Return stack is empty",
    "mermaid": """```mermaid
flowchart TD
    A[Initialize empty stack] --> B[For each char]
    B --> C{Opening bracket?}
    C -- Yes --> D[Push to stack]
    C -- No --> E{Stack top matches?}
    E -- Yes --> F[Pop stack]
    E -- No --> G[Return False]
    D --> B
    F --> B
```""",
},

# ──────────────────────────────────────────
# Problem 21: Merge Two Sorted Lists
# ──────────────────────────────────────────
21: {
    "code": """class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2
        return dummy.next""",
    "pattern": "Two Pointers / Merge",
    "time": "O(m+n)",
    "space": "O(1)",
    "approach": "Compare heads of both lists, attach the smaller one. When one list is exhausted, attach the remainder.",
    "pseudocode": "1. dummy node, curr pointer\n2. While both lists: attach smaller, advance\n3. Attach remaining list\n4. Return dummy.next",
    "mermaid": """```mermaid
flowchart TD
    A[dummy node, curr] --> B{Both lists non-empty?}
    B -- Yes --> C{list1.val <= list2.val?}
    C -- Yes --> D[Attach list1 node]
    C -- No --> E[Attach list2 node]
    D --> B
    E --> B
    B -- No --> F[Attach remaining]
    F --> G[Return dummy.next]
```""",
},

# ──────────────────────────────────────────
# Problem 22: Generate Parentheses
# ──────────────────────────────────────────
22: {
    "code": """class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def backtrack(path, open_count, close_count):
            if len(path) == 2 * n:
                result.append(''.join(path))
                return
            if open_count < n:
                path.append('(')
                backtrack(path, open_count + 1, close_count)
                path.pop()
            if close_count < open_count:
                path.append(')')
                backtrack(path, open_count, close_count + 1)
                path.pop()
        backtrack([], 0, 0)
        return result""",
    "pattern": "Backtracking",
    "time": "O(4^n / sqrt(n))",
    "space": "O(n)",
    "approach": "Backtrack with two counters: open and close. Add '(' if open < n. Add ')' if close < open.",
    "pseudocode": "1. backtrack(path, open, close):\n   If len==2n: add to result\n   If open < n: try '('\n   If close < open: try ')'",
    "mermaid": """```mermaid
flowchart TD
    A[Start: open=0, close=0] --> B{Length == 2n?}
    B -- Yes --> C[Add to result]
    B -- No --> D{open < n?}
    D -- Yes --> E["Add '(' recurse"]
    D --> F{close < open?}
    F -- Yes --> G["Add ')' recurse"]
```""",
},

# ──────────────────────────────────────────
# Problem 23: Merge k Sorted Lists
# ──────────────────────────────────────────
23: {
    "code": """import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        dummy = ListNode(0)
        curr = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next""",
    "pattern": "Heap / Priority Queue",
    "time": "O(N log k)",
    "space": "O(k)",
    "approach": "**Key Insight:** Use a min-heap of size k. Always extract the smallest head, advance that list, and push the next node.\n\nN = total number of nodes across all lists.",
    "pseudocode": "1. Push head of each list into min-heap\n2. While heap not empty:\n   Pop smallest, attach to result\n   If popped node has next, push it\n3. Return dummy.next",
    "mermaid": """```mermaid
flowchart TD
    A[Push all list heads into min-heap] --> B{Heap empty?}
    B -- No --> C[Pop min node]
    C --> D[Attach to result]
    D --> E{Node has next?}
    E -- Yes --> F[Push next into heap]
    E -- No --> B
    F --> B
    B -- Yes --> G[Return result]
```""",
},

# ──────────────────────────────────────────
# Problem 24: Swap Nodes in Pairs
# ──────────────────────────────────────────
24: {
    "code": """class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        prev = dummy
        while prev.next and prev.next.next:
            a, b = prev.next, prev.next.next
            prev.next, a.next, b.next = b, b.next, a
            prev = a
        return dummy.next""",
    "pattern": "Linked List",
    "time": "O(n)",
    "space": "O(1)",
    "approach": "Iteratively swap adjacent pairs using pointer manipulation. Use a dummy node to handle the head swap.",
    "pseudocode": "1. dummy -> head, prev = dummy\n2. While two nodes ahead exist:\n   a, b = prev.next, prev.next.next\n   Rewire: prev->b->a->b.next\n   prev = a\n3. Return dummy.next",
    "mermaid": """```mermaid
flowchart TD
    A[dummy -> head, prev=dummy] --> B{Two nodes ahead?}
    B -- Yes --> C[a=prev.next, b=a.next]
    C --> D[Swap: prev->b->a->rest]
    D --> E[prev = a]
    E --> B
    B -- No --> F[Return dummy.next]
```""",
},

# ──────────────────────────────────────────
# Problem 25: Reverse Nodes in k-Group
# ──────────────────────────────────────────
25: {
    "code": """class Solution:
    def reverseKGroup(self, head, k):
        def reverse(head, k):
            prev, curr = None, head
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        dummy = ListNode(0, head)
        prev_group = dummy
        while True:
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            next_group = kth.next
            new_head = reverse(prev_group.next, k)
            tail = prev_group.next
            tail.next = next_group
            prev_group.next = new_head
            prev_group = tail
        return dummy.next""",
    "pattern": "Linked List",
    "time": "O(n)",
    "space": "O(1)",
    "approach": "Find the kth node, reverse that segment, reconnect. Repeat until fewer than k nodes remain.",
    "pseudocode": "1. For each group of k nodes:\n   Find kth node (if < k remain, stop)\n   Reverse k nodes\n   Reconnect with previous group\n   Move to next group",
    "mermaid": """```mermaid
flowchart TD
    A[Find kth node] --> B{k nodes exist?}
    B -- Yes --> C[Reverse k nodes]
    C --> D[Reconnect group]
    D --> E[Move to next group]
    E --> A
    B -- No --> F[Return result]
```""",
},

# ──────────────────────────────────────────
# Problem 26: Remove Duplicates from Sorted Array
# ──────────────────────────────────────────
26: {
    "code": """class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1
        return write""",
    "pattern": "Two Pointers",
    "time": "O(n)",
    "space": "O(1)",
    "approach": "Use a write pointer. Only advance it when encountering a new unique value.",
    "pseudocode": "1. write = 1\n2. For read from 1 to n-1:\n   If nums[read] != nums[read-1]: nums[write] = nums[read], write++\n3. Return write",
    "mermaid": """```mermaid
flowchart TD
    A[write=1] --> B[For each read from 1]
    B --> C{nums_read != nums_read-1?}
    C -- Yes --> D[Copy to write position, write++]
    C -- No --> E[Skip]
    D --> B
    E --> B
```""",
},

# ──────────────────────────────────────────
# Problem 27: Remove Element
# ──────────────────────────────────────────
27: {
    "code": """class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        write = 0
        for num in nums:
            if num != val:
                nums[write] = num
                write += 1
        return write""",
    "pattern": "Two Pointers",
    "time": "O(n)",
    "space": "O(1)",
    "approach": "Write pointer overwrites values != val in place.",
    "pseudocode": "1. write = 0\n2. For each num: if num != val: nums[write] = num, write++\n3. Return write",
    "mermaid": """```mermaid
flowchart TD
    A[write=0] --> B[For each num]
    B --> C{num != val?}
    C -- Yes --> D[Write and advance]
    C -- No --> E[Skip]
    D --> B
    E --> B
```""",
},

# ──────────────────────────────────────────
# Problem 28: Find the Index of the First Occurrence
# ──────────────────────────────────────────
28: {
    "code": """class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)""",
    "pattern": "String Matching",
    "time": "O(m*n)",
    "space": "O(1)",
    "approach": "Use built-in string find or implement KMP. The simplest approach uses the built-in method.",
    "pseudocode": "1. Return haystack.find(needle)",
    "mermaid": """```mermaid
flowchart TD
    A[Search for needle in haystack] --> B{Found?}
    B -- Yes --> C[Return index]
    B -- No --> D[Return -1]
```""",
},

# Problems 29-500 follow. Let me continue with key problems...

# ──────────────────────────────────────────
# Problem 29: Divide Two Integers
# ──────────────────────────────────────────
29: {
    "code": """class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        a, b = abs(dividend), abs(divisor)
        result = 0
        while a >= b:
            temp, multiple = b, 1
            while a >= temp << 1:
                temp <<= 1
                multiple <<= 1
            a -= temp
            result += multiple
        return sign * result""",
    "pattern": "Bit Manipulation / Math",
    "time": "O(log^2 n)",
    "space": "O(1)",
    "approach": "Use bit shifting to double the divisor until it exceeds the dividend. Subtract and accumulate the quotient.",
    "pseudocode": "1. Handle overflow edge case\n2. Work with absolute values\n3. Repeatedly double divisor, subtract, accumulate\n4. Restore sign",
    "mermaid": """```mermaid
flowchart TD
    A[Handle sign and overflow] --> B{dividend >= divisor?}
    B -- Yes --> C[Double divisor with bit shift]
    C --> D[Subtract and accumulate quotient]
    D --> B
    B -- No --> E[Return signed result]
```""",
},

# ──────────────────────────────────────────
# Problem 30: Substring with Concatenation of All Words
# ──────────────────────────────────────────
30: {
    "code": """from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = Counter(words)
        result = []
        for i in range(len(s) - total_len + 1):
            seen = Counter()
            j = 0
            while j < len(words):
                word = s[i + j * word_len: i + (j + 1) * word_len]
                if word in word_count:
                    seen[word] += 1
                    if seen[word] > word_count[word]:
                        break
                else:
                    break
                j += 1
            if j == len(words):
                result.append(i)
        return result""",
    "pattern": "Sliding Window / Hash Map",
    "time": "O(n * m * w) where n=len(s), m=num words, w=word len",
    "space": "O(m)",
    "approach": "Check every starting position. For each, try to match all words using a counter map.",
    "pseudocode": "1. For each start position i:\n   Count words in window\n   Compare with target word counts\n   If all match: add i to result",
    "mermaid": """```mermaid
flowchart TD
    A[For each start position i] --> B[Extract words from window]
    B --> C{All words matched?}
    C -- Yes --> D[Add i to result]
    C -- No --> E[Next position]
```""",
},

# ──────────────────────────────────────────
# Problem 31: Next Permutation
# ──────────────────────────────────────────
31: {
    "code": """class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = reversed(nums[i + 1:])""",
    "pattern": "Array Manipulation",
    "time": "O(n)",
    "space": "O(1)",
    "approach": "1. Find rightmost element smaller than its successor (i). 2. Find rightmost element larger than nums[i] (j). 3. Swap i,j. 4. Reverse suffix after i.",
    "pseudocode": "1. Find i where nums[i] < nums[i+1] from right\n2. Find j > i where nums[j] > nums[i] from right\n3. Swap nums[i], nums[j]\n4. Reverse nums[i+1:]",
    "mermaid": """```mermaid
flowchart TD
    A[Find i: rightmost ascent] --> B{i found?}
    B -- Yes --> C[Find j: rightmost larger than nums_i]
    C --> D[Swap nums_i and nums_j]
    D --> E[Reverse suffix after i]
    B -- No --> E[Reverse entire array]
```""",
},

# ──────────────────────────────────────────
# Problem 32: Longest Valid Parentheses
# ──────────────────────────────────────────
32: {
    "code": """class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len""",
    "pattern": "Stack",
    "time": "O(n)",
    "space": "O(n)",
    "approach": "**Key Insight:** Stack stores indices. Push -1 as base. For ')', pop and compute length from new stack top.\n\nIf stack becomes empty after pop, push current index as new base.",
    "pseudocode": "1. stack = [-1]\n2. For each i, ch:\n   '(': push i\n   ')': pop, if empty push i, else update max_len = i - stack[-1]\n3. Return max_len",
    "mermaid": """```mermaid
flowchart TD
    A["stack = [-1]"] --> B[For each index i]
    B --> C{"'(' ?"}
    C -- Yes --> D[Push i]
    C -- No --> E[Pop]
    E --> F{Stack empty?}
    F -- Yes --> G[Push i as new base]
    F -- No --> H[max_len = i - stack top]
    D --> B
    G --> B
    H --> B
```""",
},

# ──────────────────────────────────────────
# Problem 33: Search in Rotated Sorted Array
# ──────────────────────────────────────────
33: {
    "code": """class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1""",
    "pattern": "Binary Search",
    "time": "O(log n)",
    "space": "O(1)",
    "approach": "**Key Insight:** One half is always sorted. Determine which half is sorted, then check if target lies within that half.",
    "pseudocode": "1. lo=0, hi=n-1\n2. mid = (lo+hi)//2\n3. If left half sorted: check if target in left half\n4. Else right half sorted: check if target in right half\n5. Adjust lo/hi accordingly",
    "mermaid": """```mermaid
flowchart TD
    A[lo=0, hi=n-1] --> B[mid = lo+hi / 2]
    B --> C{nums_mid == target?}
    C -- Yes --> D[Return mid]
    C -- No --> E{Left half sorted?}
    E -- Yes --> F{Target in left half?}
    F -- Yes --> G[hi = mid-1]
    F -- No --> H[lo = mid+1]
    E -- No --> I{Target in right half?}
    I -- Yes --> H
    I -- No --> G
```""",
},

# ──────────────────────────────────────────
# Problem 34: Find First and Last Position
# ──────────────────────────────────────────
34: {
    "code": """class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_left():
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return lo

        def find_right():
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return hi

        left, right = find_left(), find_right()
        if left <= right:
            return [left, right]
        return [-1, -1]""",
    "pattern": "Binary Search",
    "time": "O(log n)",
    "space": "O(1)",
    "approach": "Two binary searches: one for the leftmost occurrence, one for the rightmost.",
    "pseudocode": "1. Binary search for leftmost target index\n2. Binary search for rightmost target index\n3. If left <= right: return [left, right]\n4. Else: return [-1, -1]",
    "mermaid": """```mermaid
flowchart TD
    A[Binary search left boundary] --> B[Binary search right boundary]
    B --> C{left <= right?}
    C -- Yes --> D["Return [left, right]"]
    C -- No --> E["Return [-1, -1]"]
```""",
},

# ──────────────────────────────────────────
# Problem 35: Search Insert Position
# ──────────────────────────────────────────
35: {
    "code": """class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo""",
    "pattern": "Binary Search",
    "time": "O(log n)",
    "space": "O(1)",
    "approach": "Standard binary search. Return lo when the loop ends -- it's the insertion point.",
    "pseudocode": "1. lo=0, hi=n\n2. While lo < hi: mid check\n3. Return lo as insertion point",
    "mermaid": """```mermaid
flowchart TD
    A[lo=0, hi=n] --> B{lo < hi?}
    B -- Yes --> C[mid = lo+hi / 2]
    C --> D{nums_mid < target?}
    D -- Yes --> E[lo = mid+1]
    D -- No --> F[hi = mid]
    E --> B
    F --> B
    B -- No --> G[Return lo]
```""",
},

# ──────────────────────────────────────────
# Problem 36: Valid Sudoku
# ──────────────────────────────────────────
36: {
    "code": """class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                box_idx = (i // 3) * 3 + j // 3
                if num in rows[i] or num in cols[j] or num in boxes[box_idx]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_idx].add(num)
        return True""",
    "pattern": "Hash Set",
    "time": "O(1) (fixed 9x9 board)",
    "space": "O(1)",
    "approach": "Track seen numbers in each row, column, and 3x3 box using sets.",
    "pseudocode": "1. Create sets for 9 rows, 9 cols, 9 boxes\n2. For each cell: check row/col/box sets for duplicate\n3. Add to sets if valid",
    "mermaid": """```mermaid
flowchart TD
    A[Init 9 row, col, box sets] --> B[For each cell i,j]
    B --> C{Already in row/col/box?}
    C -- Yes --> D[Return False]
    C -- No --> E[Add to sets]
    E --> B
```""",
},

# ──────────────────────────────────────────
# Problem 37: Sudoku Solver
# ──────────────────────────────────────────
37: {
    "code": """class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def is_valid(row, col, num):
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
                r, c = 3 * (row // 3) + i // 3, 3 * (col // 3) + i % 3
                if board[r][c] == num:
                    return False
            return True

        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in '123456789':
                            if is_valid(i, j, num):
                                board[i][j] = num
                                if solve():
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        solve()""",
    "pattern": "Backtracking",
    "time": "O(9^(empty cells))",
    "space": "O(81)",
    "approach": "Backtracking: try each digit 1-9 for each empty cell, validate, recurse.",
    "pseudocode": "1. Find next empty cell\n2. Try digits 1-9:\n   If valid: place and recurse\n   If recurse fails: undo (backtrack)\n3. If no digits work: return False",
    "mermaid": """```mermaid
flowchart TD
    A[Find next empty cell] --> B{Found?}
    B -- No --> C[Solved - Return True]
    B -- Yes --> D[Try digits 1-9]
    D --> E{Valid placement?}
    E -- Yes --> F[Place digit, recurse]
    F --> G{Recursion solved?}
    G -- Yes --> C
    G -- No --> H[Undo, try next digit]
    E -- No --> H
    H --> D
```""",
},

# ──────────────────────────────────────────
# Problem 38: Count and Say
# ──────────────────────────────────────────
38: {
    "code": """class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            result = []
            i = 0
            while i < len(s):
                count = 1
                while i + count < len(s) and s[i + count] == s[i]:
                    count += 1
                result.append(str(count) + s[i])
                i += count
            s = ''.join(result)
        return s""",
    "pattern": "String Simulation",
    "time": "O(2^n) worst case",
    "space": "O(2^n)",
    "approach": "Iteratively build each sequence by counting consecutive identical digits in the previous one.",
    "pseudocode": "1. Start with '1'\n2. Repeat n-1 times:\n   Count consecutive same digits\n   Build new string: count + digit\n3. Return result",
    "mermaid": """```mermaid
flowchart TD
    A["s = '1'"] --> B[Repeat n-1 times]
    B --> C[Count consecutive runs]
    C --> D[Build: count + digit]
    D --> B
```""",
},

# ──────────────────────────────────────────
# Problem 39: Combination Sum
# ──────────────────────────────────────────
39: {
    "code": """class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    continue
                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])
                path.pop()
        backtrack(0, [], target)
        return result""",
    "pattern": "Backtracking",
    "time": "O(n^(target/min))",
    "space": "O(target/min)",
    "approach": "Backtrack trying each candidate (reusable). Start index prevents duplicates.",
    "pseudocode": "1. backtrack(start, path, remaining):\n   If remaining == 0: record path\n   For i from start: try candidates[i], recurse with same i",
    "mermaid": """```mermaid
flowchart TD
    A[backtrack start, path, remaining] --> B{remaining == 0?}
    B -- Yes --> C[Record path]
    B -- No --> D[For each candidate from start]
    D --> E{candidate <= remaining?}
    E -- Yes --> F[Add to path, recurse]
    E -- No --> G[Skip]
    F --> H[Remove from path]
```""",
},

# ──────────────────────────────────────────
# Problem 40: Combination Sum II
# ──────────────────────────────────────────
40: {
    "code": """class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])
                path.pop()
        backtrack(0, [], target)
        return result""",
    "pattern": "Backtracking",
    "time": "O(2^n)",
    "space": "O(n)",
    "approach": "Sort first. Backtrack with i+1 (no reuse). Skip duplicates at same level.",
    "pseudocode": "1. Sort candidates\n2. backtrack(start, path, remaining):\n   Skip if same as prev at same level\n   Recurse with i+1",
    "mermaid": """```mermaid
flowchart TD
    A[Sort candidates] --> B[backtrack]
    B --> C{remaining == 0?}
    C -- Yes --> D[Record]
    C -- No --> E[For each from start]
    E --> F{Duplicate at same level?}
    F -- Yes --> G[Skip]
    F -- No --> H[Try, recurse with i+1]
```""",
},

# ──────────────────────────────────────────
# Problem 41: First Missing Positive
# ──────────────────────────────────────────
41: {
    "code": """class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1""",
    "pattern": "Cyclic Sort",
    "time": "O(n)",
    "space": "O(1)",
    "approach": "**Key Insight:** Place each number at its correct index (nums[i] should be i+1). Then scan for the first mismatch.",
    "pseudocode": "1. For each i: swap nums[i] to its correct position\n2. Scan for first i where nums[i] != i+1\n3. Return i+1 (or n+1 if all correct)",
    "mermaid": """```mermaid
flowchart TD
    A[For each element] --> B{1 <= nums_i <= n?}
    B -- Yes --> C{Already in place?}
    C -- No --> D[Swap to correct position]
    D --> B
    C -- Yes --> E[Next element]
    B -- No --> E
    E --> F[Scan for first mismatch]
    F --> G[Return missing positive]
```""",
},

# ──────────────────────────────────────────
# Problem 42: Trapping Rain Water
# ──────────────────────────────────────────
42: {
    "code": """class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water""",
    "pattern": "Two Pointers",
    "time": "O(n)",
    "space": "O(1)",
    "approach": "**Key Insight:** Water at each position = min(left_max, right_max) - height. Use two pointers moving inward, tracking max heights from each side.",
    "pseudocode": "1. left=0, right=n-1, left_max=0, right_max=0\n2. While left < right:\n   Process shorter side\n   Update max or add trapped water\n3. Return total water",
    "mermaid": """```mermaid
flowchart TD
    A[left=0, right=n-1] --> B{left < right?}
    B -- Yes --> C{height_left < height_right?}
    C -- Yes --> D[Process left side]
    C -- No --> E[Process right side]
    D --> F[Update left_max or add water]
    E --> G[Update right_max or add water]
    F --> B
    G --> B
    B -- No --> H[Return total water]
```""",
    "animation_frames": """**Two Pointer Water Trapping for height=[0,1,0,2,1,0,1,3,2,1,2,1]:**

**Step 1:** Initialize pointers at edges

```mermaid
flowchart LR
    H0["0(L)"] --> H1[1] --> H2[0] --> H3[2] --> H4[1] --> H5[0] --> H6[1] --> H7[3] --> H8[2] --> H9[1] --> H10[2] --> H11["1(R)"]
```

left_max=0, right_max=0, water=0

**Step 2:** Process left (h=0 < h=1), left_max=0, water stays 0

```mermaid
flowchart LR
    H0[0] --> H1["1(L)"] --> H2[0] --> H3[2] --> H4[1] --> H5[0] --> H6[1] --> H7[3] --> H8[2] --> H9[1] --> H10[2] --> H11["1(R)"]
```

left_max=0, right_max=0, water=0

**Step 3:** Both equal, process right (h=1), right_max=1

```mermaid
flowchart LR
    H0[0] --> H1["1(L)"] --> H2[0] --> H3[2] --> H4[1] --> H5[0] --> H6[1] --> H7[3] --> H8[2] --> H9[1] --> H10["2(R)"] --> H11[1]
```

left_max=1, right_max=1, water=0""",
},

# ──────────────────────────────────────────
# Problem 43-50 (continuing the pattern)
# ──────────────────────────────────────────
43: {
    "code": """class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - 48) * (ord(num2[j]) - 48)
                p1, p2 = i + j, i + j + 1
                total = mul + result[p2]
                result[p2] = total % 10
                result[p1] += total // 10
        result_str = ''.join(map(str, result)).lstrip('0')
        return result_str or '0'""",
    "pattern": "Math / String",
    "time": "O(m*n)",
    "space": "O(m+n)",
    "approach": "Grade-school multiplication: multiply each digit pair, accumulate at correct position in result array.",
    "pseudocode": "1. result = [0] * (m+n)\n2. For each digit pair: multiply, add to position i+j and i+j+1\n3. Convert array to string, strip leading zeros",
    "mermaid": """```mermaid
flowchart TD
    A[Create result array of m+n zeros] --> B[For each i in num1 reversed]
    B --> C[For each j in num2 reversed]
    C --> D[Multiply digits, add to result positions]
    D --> C
    C --> B
    B --> E[Convert to string, strip zeros]
```""",
},

44: {
    "code": """class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]""",
    "pattern": "Dynamic Programming",
    "time": "O(m*n)",
    "space": "O(m*n)",
    "approach": "2D DP: dp[i][j] = s[:i] matches p[:j]. '*' can match empty (dp[i][j-1]) or extend (dp[i-1][j]).",
    "pseudocode": "1. dp[0][0] = True\n2. First row: '*' matches empty\n3. For each (i,j): handle '*', '?', exact match\n4. Return dp[m][n]",
    "mermaid": """```mermaid
flowchart TD
    A[Init dp table] --> B[Fill first row for star]
    B --> C[For each i,j]
    C --> D{p_j == star?}
    D -- Yes --> E["dp[i-1][j] OR dp[i][j-1]"]
    D -- No --> F{Match or '?'}
    F -- Yes --> G["dp[i-1][j-1]"]
    F -- No --> H[False]
```""",
},

45: {
    "code": """class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = current_end = farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps""",
    "pattern": "Greedy",
    "time": "O(n)",
    "space": "O(1)",
    "approach": "**Greedy BFS:** Track the farthest reachable position. When we reach the current jump boundary, take a jump.",
    "pseudocode": "1. jumps=0, current_end=0, farthest=0\n2. For i in [0, n-2]:\n   farthest = max(farthest, i + nums[i])\n   If i == current_end: jumps++, current_end = farthest\n3. Return jumps",
    "mermaid": """```mermaid
flowchart TD
    A[jumps=0, end=0, far=0] --> B[For each i to n-2]
    B --> C[Update farthest]
    C --> D{i == current_end?}
    D -- Yes --> E[jumps++, end = farthest]
    D -- No --> F[Continue]
    E --> B
    F --> B
```""",
},

46: {
    "code": """class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        def backtrack(path, remaining):
            if not remaining:
                result.append(path[:])
                return
            for i in range(len(remaining)):
                path.append(remaining[i])
                backtrack(path, remaining[:i] + remaining[i+1:])
                path.pop()
        backtrack([], nums)
        return result""",
    "pattern": "Backtracking",
    "time": "O(n!)",
    "space": "O(n)",
    "approach": "Classic backtracking: try each remaining element, recurse with it removed.",
    "pseudocode": "1. backtrack(path, remaining):\n   If empty: record path\n   For each in remaining: add, recurse without it, remove",
    "mermaid": """```mermaid
flowchart TD
    A[backtrack path, remaining] --> B{remaining empty?}
    B -- Yes --> C[Record permutation]
    B -- No --> D[For each element]
    D --> E[Add to path, recurse]
    E --> F[Remove from path]
```""",
},

47: {
    "code": """class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        used = [False] * len(nums)
        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False
        backtrack([])
        return result""",
    "pattern": "Backtracking",
    "time": "O(n!)",
    "space": "O(n)",
    "approach": "Sort + backtrack with used array. Skip duplicate elements at the same level.",
    "pseudocode": "1. Sort nums, used = [False]*n\n2. backtrack(path):\n   Skip used or same-level duplicates\n   Mark used, recurse, unmark",
    "mermaid": """```mermaid
flowchart TD
    A[Sort nums] --> B[backtrack with used array]
    B --> C{Duplicate at same level?}
    C -- Yes --> D[Skip]
    C -- No --> E[Use element, recurse]
```""",
},

48: {
    "code": """class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()""",
    "pattern": "Matrix Manipulation",
    "time": "O(n^2)",
    "space": "O(1)",
    "approach": "**Transpose then reverse each row.** This rotates the matrix 90 degrees clockwise in-place.",
    "pseudocode": "1. Transpose: swap matrix[i][j] with matrix[j][i]\n2. Reverse each row",
    "mermaid": """```mermaid
flowchart TD
    A[Transpose matrix] --> B[Reverse each row]
    B --> C[Matrix rotated 90 degrees]
```""",
},

49: {
    "code": """from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)
        return list(groups.values())""",
    "pattern": "Hash Map / Sorting",
    "time": "O(n * k log k)",
    "space": "O(n * k)",
    "approach": "Group strings by their sorted version as key. All anagrams share the same sorted form.",
    "pseudocode": "1. For each string: sort it to get key\n2. Group strings by key in a dict\n3. Return all groups",
    "mermaid": """```mermaid
flowchart TD
    A[For each string] --> B[Sort to get key]
    B --> C[Add to group map]
    C --> A
    A --> D[Return all groups]
```""",
},

50: {
    "code": """class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        result = 1
        while n:
            if n & 1:
                result *= x
            x *= x
            n >>= 1
        return result""",
    "pattern": "Math / Binary Exponentiation",
    "time": "O(log n)",
    "space": "O(1)",
    "approach": "Fast power using binary exponentiation. Square x repeatedly, multiply into result when bit is set.",
    "pseudocode": "1. Handle negative n: x = 1/x\n2. While n > 0:\n   If n is odd: result *= x\n   x *= x, n >>= 1\n3. Return result",
    "mermaid": """```mermaid
flowchart TD
    A[Handle negative exponent] --> B{n > 0?}
    B -- Yes --> C{n is odd?}
    C -- Yes --> D[result *= x]
    C -- No --> E[Skip]
    D --> F[x *= x, n >>= 1]
    E --> F
    F --> B
    B -- No --> G[Return result]
```""",
},

# ──────────────────────────────────────────
# Problems 51-100 (core problems)
# ──────────────────────────────────────────
51: {"code": """class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        cols = set()
        diag1 = set()
        diag2 = set()
        board = [['.' ] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                result.append([''.join(r) for r in board])
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'
                cols.discard(col)
                diag1.discard(row - col)
                diag2.discard(row + col)
        backtrack(0)
        return result""", "pattern": "Backtracking", "time": "O(n!)", "space": "O(n^2)", "approach": "Place queens row by row. Track attacked columns and diagonals with sets.", "pseudocode": "1. For each row: try each column\n2. Skip if column/diagonal attacked\n3. Place queen, recurse to next row\n4. Backtrack if no solution", "mermaid": """```mermaid
flowchart TD
    A[Start row 0] --> B[Try each column]
    B --> C{Column/diagonal free?}
    C -- Yes --> D[Place queen]
    D --> E[Recurse next row]
    C -- No --> F[Next column]
    E --> G{All rows filled?}
    G -- Yes --> H[Record solution]
    G -- No --> I[Backtrack]
```"""},

52: {"code": """class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        cols, d1, d2 = set(), set(), set()
        def solve(row):
            if row == n:
                self.count += 1
                return
            for col in range(n):
                if col in cols or row-col in d1 or row+col in d2:
                    continue
                cols.add(col); d1.add(row-col); d2.add(row+col)
                solve(row+1)
                cols.discard(col); d1.discard(row-col); d2.discard(row+col)
        solve(0)
        return self.count""", "pattern": "Backtracking", "time": "O(n!)", "space": "O(n)", "approach": "Same as N-Queens I but just count solutions instead of storing boards.", "pseudocode": "Same as N-Queens but increment counter instead of recording", "mermaid": ""},

53: {"code": """class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = curr_sum = nums[0]
        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum""", "pattern": "Kadane's Algorithm (DP)", "time": "O(n)", "space": "O(1)", "approach": "**Kadane's Algorithm:** At each position, either extend the current subarray or start fresh. Track the global maximum.", "pseudocode": "1. curr_sum = max_sum = nums[0]\n2. For each num from index 1:\n   curr_sum = max(num, curr_sum + num)\n   max_sum = max(max_sum, curr_sum)\n3. Return max_sum", "mermaid": """```mermaid
flowchart TD
    A[curr = max = nums_0] --> B[For each num]
    B --> C[curr = max of num or curr+num]
    C --> D[Update global max]
    D --> B
```"""},

54: {"code": """class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        while matrix:
            result += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())
            if matrix:
                result += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))
        return result""", "pattern": "Matrix Simulation", "time": "O(m*n)", "space": "O(1) extra", "approach": "Peel layers: top row, right column, bottom row (reversed), left column (reversed). Repeat.", "pseudocode": "1. While matrix not empty:\n   Pop top row\n   Pop right column\n   Pop bottom row reversed\n   Pop left column reversed", "mermaid": ""},

55: {"code": """class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
        return True""", "pattern": "Greedy", "time": "O(n)", "space": "O(1)", "approach": "Track the farthest reachable index. If current index exceeds it, return False.", "pseudocode": "1. farthest = 0\n2. For each i: if i > farthest: False; farthest = max(farthest, i+nums[i])\n3. Return True", "mermaid": """```mermaid
flowchart TD
    A[farthest = 0] --> B[For each index i]
    B --> C{i > farthest?}
    C -- Yes --> D[Return False]
    C -- No --> E[farthest = max farthest, i+nums_i]
    E --> B
```"""},

56: {"code": """class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged""", "pattern": "Intervals / Sort", "time": "O(n log n)", "space": "O(n)", "approach": "Sort by start time. Merge overlapping intervals by extending the end of the last merged interval.", "pseudocode": "1. Sort intervals by start\n2. For each interval:\n   If overlaps with last merged: extend end\n   Else: add new interval", "mermaid": """```mermaid
flowchart TD
    A[Sort by start] --> B[merged = first interval]
    B --> C[For each interval]
    C --> D{Overlaps with last?}
    D -- Yes --> E[Extend end]
    D -- No --> F[Append new]
    E --> C
    F --> C
```"""},

57: {"code": """class Solution:
    def insert(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        while i < n:
            result.append(intervals[i])
            i += 1
        return result""", "pattern": "Intervals", "time": "O(n)", "space": "O(n)", "approach": "Three passes: add all before, merge all overlapping, add all after.", "pseudocode": "1. Add intervals ending before new starts\n2. Merge overlapping intervals\n3. Add remaining intervals", "mermaid": ""},

58: {"code": """class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split()[-1])""", "pattern": "String", "time": "O(n)", "space": "O(n)", "approach": "Strip trailing spaces, split by spaces, return length of last word.", "pseudocode": "1. Strip trailing spaces\n2. Split by spaces\n3. Return length of last element", "mermaid": ""},

59: {"code": """class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0]*n for _ in range(n)]
        top, bottom, left, right = 0, n-1, 0, n-1
        num = 1
        while num <= n*n:
            for j in range(left, right+1):
                matrix[top][j] = num; num += 1
            top += 1
            for i in range(top, bottom+1):
                matrix[i][right] = num; num += 1
            right -= 1
            for j in range(right, left-1, -1):
                matrix[bottom][j] = num; num += 1
            bottom -= 1
            for i in range(bottom, top-1, -1):
                matrix[i][left] = num; num += 1
            left += 1
        return matrix""", "pattern": "Matrix Simulation", "time": "O(n^2)", "space": "O(n^2)", "approach": "Fill matrix in spiral order using boundary pointers (top, bottom, left, right).", "pseudocode": "1. Use four boundaries\n2. Fill top row, right col, bottom row, left col\n3. Shrink boundaries, repeat", "mermaid": ""},

60: {"code": """class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial
        nums = list(range(1, n+1))
        k -= 1
        result = []
        for i in range(n, 0, -1):
            f = factorial(i - 1)
            idx = k // f
            result.append(str(nums[idx]))
            nums.pop(idx)
            k %= f
        return ''.join(result)""", "pattern": "Math", "time": "O(n^2)", "space": "O(n)", "approach": "Use factorial number system to directly compute the kth permutation without generating all permutations.", "pseudocode": "1. k -= 1 (0-indexed)\n2. For each position: idx = k // (n-1)!, pick nums[idx], k %= (n-1)!", "mermaid": ""},

# Problems 61-100 - continuing essential problems
61: {"code": """class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        k %= length
        if k == 0:
            return head
        tail.next = head
        steps = length - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head""", "pattern": "Linked List", "time": "O(n)", "space": "O(1)", "approach": "Make list circular, then break at the right point. k %= length to handle large k.", "pseudocode": "1. Find length, connect tail to head\n2. k %= length\n3. Walk length-k steps from head, break the link", "mermaid": ""},

62: {"code": """class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]""", "pattern": "Dynamic Programming", "time": "O(m*n)", "space": "O(n)", "approach": "DP: paths to (i,j) = paths from above + paths from left. Optimize to 1D array.", "pseudocode": "1. dp = [1]*n (first row all 1s)\n2. For each row: dp[j] += dp[j-1]\n3. Return dp[-1]", "mermaid": """```mermaid
flowchart TD
    A["dp = [1]*n"] --> B[For each row 1 to m-1]
    B --> C[For j=1 to n-1: dp_j += dp_j-1]
    C --> B
    B --> D[Return dp n-1]
```"""},

63: {"code": """class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        dp = [0] * n
        dp[0] = 1
        for row in grid:
            for j in range(n):
                if row[j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1]
        return dp[-1]""", "pattern": "Dynamic Programming", "time": "O(m*n)", "space": "O(n)", "approach": "Same as Unique Paths but set dp[j]=0 for obstacles.", "pseudocode": "1. dp[0] = 1 if no obstacle\n2. For each cell: if obstacle dp=0, else dp[j] += dp[j-1]\n3. Return dp[-1]", "mermaid": ""},

64: {"code": """class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]""", "pattern": "Dynamic Programming", "time": "O(m*n)", "space": "O(1)", "approach": "In-place DP: each cell += min of cell above and cell to the left.", "pseudocode": "1. For each cell (i,j):\n   grid[i][j] += min(above, left)\n2. Return grid[-1][-1]", "mermaid": ""},

65: {"code": """class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except ValueError:
            return False""", "pattern": "String Parsing / State Machine", "time": "O(n)", "space": "O(1)", "approach": "Parse the number string with state machine or use Python float conversion with validation.", "pseudocode": "1. Try float(s)\n2. Return True if valid, False if ValueError", "mermaid": ""},

66: {"code": """class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits""", "pattern": "Math / Array", "time": "O(n)", "space": "O(1)", "approach": "Add 1 from the end. If digit < 9, increment and return. If 9, set to 0 and carry. If all 9s, prepend 1.", "pseudocode": "1. From rightmost digit:\n   If < 9: increment, done\n   If 9: set to 0, continue left\n2. If all carried: prepend 1", "mermaid": ""},

67: {"code": """class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i]); i -= 1
            if j >= 0:
                total += int(b[j]); j -= 1
            result.append(str(total % 2))
            carry = total // 2
        return ''.join(reversed(result))""", "pattern": "Math / String", "time": "O(max(m,n))", "space": "O(max(m,n))", "approach": "Same as Add Two Numbers but for binary strings. Add from right with carry.", "pseudocode": "1. Process from right with carry\n2. total = carry + a[i] + b[j]\n3. Append total%2, carry = total//2\n4. Return reversed result", "mermaid": ""},

68: {"code": """class Solution:
    def fullJustify(self, words, maxWidth):
        result, line, line_len = [], [], 0
        for word in words:
            if line_len + len(word) + len(line) > maxWidth:
                for i in range(maxWidth - line_len):
                    line[i % (len(line)-1 or 1)] += ' '
                result.append(''.join(line))
                line, line_len = [], 0
            line.append(word)
            line_len += len(word)
        result.append(' '.join(line).ljust(maxWidth))
        return result""", "pattern": "String Simulation", "time": "O(n)", "space": "O(n)", "approach": "Greedily pack words into lines. Distribute extra spaces round-robin. Last line is left-justified.", "pseudocode": "1. Pack words into lines greedily\n2. Distribute spaces evenly (round-robin)\n3. Left-justify last line", "mermaid": ""},

69: {"code": """class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo""", "pattern": "Binary Search", "time": "O(log n)", "space": "O(1)", "approach": "Binary search for the integer square root. Find largest mid where mid^2 <= x.", "pseudocode": "1. Binary search [0, x]\n2. If mid^2 <= x < (mid+1)^2: return mid\n3. Adjust lo/hi accordingly", "mermaid": ""},

70: {"code": """class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b""", "pattern": "Dynamic Programming (Fibonacci)", "time": "O(n)", "space": "O(1)", "approach": "**Key Insight:** Same as Fibonacci. Ways to reach step n = ways(n-1) + ways(n-2).", "pseudocode": "1. Base: step 1 = 1 way, step 2 = 2 ways\n2. For 3 to n: ways[i] = ways[i-1] + ways[i-2]\n3. Return ways[n]", "mermaid": """```mermaid
flowchart TD
    A[a=1, b=2] --> B[For i = 3 to n]
    B --> C["a, b = b, a+b"]
    C --> B
    B --> D[Return b]
```""", "animation_frames": """**DP State Transition for n=5:**

**Step 1:** Base cases

```mermaid
flowchart LR
    S1["Step 1: 1 way"] --> S2["Step 2: 2 ways"]
```

**Step 2:** Step 3 = 1 + 2 = 3 ways

```mermaid
flowchart LR
    S1["Step 1: 1"] --> S2["Step 2: 2"] --> S3["Step 3: 3"]
```

**Step 3:** Step 4 = 2 + 3 = 5 ways, Step 5 = 3 + 5 = 8 ways

```mermaid
flowchart LR
    S1["Step 1: 1"] --> S2["Step 2: 2"] --> S3["Step 3: 3"] --> S4["Step 4: 5"] --> S5["Step 5: 8"]
```"""},

71: {"code": """class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split('/'):
            if part == '..':
                if stack:
                    stack.pop()
            elif part and part != '.':
                stack.append(part)
        return '/' + '/'.join(stack)""", "pattern": "Stack", "time": "O(n)", "space": "O(n)", "approach": "Split by '/', use stack: push directories, pop on '..', ignore '.' and empty.", "pseudocode": "1. Split path by '/'\n2. For each part: '..' = pop, '.' = skip, else push\n3. Return '/' + '/'.join(stack)", "mermaid": ""},

72: {"code": """class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = list(range(n + 1))
        for i in range(1, m + 1):
            prev = dp[0]
            dp[0] = i
            for j in range(1, n + 1):
                temp = dp[j]
                if word1[i-1] == word2[j-1]:
                    dp[j] = prev
                else:
                    dp[j] = 1 + min(prev, dp[j], dp[j-1])
                prev = temp
        return dp[n]""", "pattern": "Dynamic Programming", "time": "O(m*n)", "space": "O(n)", "approach": "**Edit Distance DP:** dp[i][j] = min ops to convert word1[:i] to word2[:j]. Insert/delete/replace.", "pseudocode": "1. dp[j] = j for base case\n2. For each i,j:\n   If chars match: dp = diagonal\n   Else: 1 + min(insert, delete, replace)\n3. Return dp[n]", "mermaid": """```mermaid
flowchart TD
    A[Init dp row 0..n] --> B[For each char in word1]
    B --> C[For each char in word2]
    C --> D{Chars match?}
    D -- Yes --> E[dp = prev diagonal]
    D -- No --> F["dp = 1 + min(insert, delete, replace)"]
    E --> C
    F --> C
```"""},

73: {"code": """class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row = any(matrix[0][j] == 0 for j in range(n))
        first_col = any(matrix[i][0] == 0 for i in range(m))
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row:
            for j in range(n):
                matrix[0][j] = 0
        if first_col:
            for i in range(m):
                matrix[i][0] = 0""", "pattern": "Matrix / In-place", "time": "O(m*n)", "space": "O(1)", "approach": "Use first row/col as markers. Track if first row/col themselves need zeroing.", "pseudocode": "1. Mark first row/col flags\n2. Use first row/col to mark zero rows/cols\n3. Zero based on markers\n4. Handle first row/col", "mermaid": ""},

74: {"code": """class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False""", "pattern": "Binary Search", "time": "O(log(m*n))", "space": "O(1)", "approach": "Treat 2D matrix as 1D sorted array. Binary search with index mapping: row=mid//n, col=mid%n.", "pseudocode": "1. Binary search [0, m*n-1]\n2. Map mid to matrix[mid//n][mid%n]\n3. Standard binary search logic", "mermaid": ""},

75: {"code": """class Solution:
    def sortColors(self, nums: list[int]) -> None:
        lo, mid, hi = 0, 0, len(nums) - 1
        while mid <= hi:
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1; mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1""", "pattern": "Dutch National Flag / Three Pointers", "time": "O(n)", "space": "O(1)", "approach": "**Dutch National Flag:** Three pointers (lo, mid, hi). 0s go to front, 2s go to back, 1s stay in middle.", "pseudocode": "1. lo=0, mid=0, hi=n-1\n2. While mid <= hi:\n   0: swap with lo, advance both\n   1: advance mid\n   2: swap with hi, decrement hi", "mermaid": """```mermaid
flowchart TD
    A[lo=0, mid=0, hi=n-1] --> B{mid <= hi?}
    B -- Yes --> C{nums_mid value?}
    C -- 0 --> D[Swap lo,mid. lo++ mid++]
    C -- 1 --> E[mid++]
    C -- 2 --> F[Swap mid,hi. hi--]
    D --> B
    E --> B
    F --> B
    B -- No --> G[Sorted]
```"""},

76: {"code": """from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        left = 0
        start, end = 0, float('inf')
        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            while missing == 0:
                if right - left < end - start:
                    start, end = left, right
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1
        return s[start:end+1] if end != float('inf') else '' """, "pattern": "Sliding Window", "time": "O(m+n)", "space": "O(m+n)", "approach": "**Key Insight:** Expand right to include all needed chars, then shrink left to minimize window. Track missing count.", "pseudocode": "1. Count needed chars\n2. Expand right: decrement need, if was needed decrement missing\n3. While missing==0: try shrink left, update best window\n4. Return minimum window", "mermaid": """```mermaid
flowchart TD
    A[Count needed chars from t] --> B[Expand right pointer]
    B --> C{All chars found?}
    C -- No --> B
    C -- Yes --> D[Shrink left pointer]
    D --> E[Update min window]
    E --> F{Still valid?}
    F -- Yes --> D
    F -- No --> B
```"""},

# Continue with more key problems...
77: {"code": """class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
        backtrack(1, [])
        return result""", "pattern": "Backtracking", "time": "O(C(n,k))", "space": "O(k)", "approach": "Backtrack: pick elements in order to avoid duplicates.", "pseudocode": "1. backtrack(start, path):\n   If len(path)==k: record\n   For i from start to n: try i, recurse with i+1", "mermaid": ""},

78: {"code": """class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        def backtrack(start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return result""", "pattern": "Backtracking", "time": "O(2^n)", "space": "O(n)", "approach": "At each step, include or exclude the current element.", "pseudocode": "1. backtrack(start, path):\n   Record path (every subset valid)\n   For i from start: add nums[i], recurse, remove", "mermaid": ""},

79: {"code": """class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            tmp = board[i][j]
            board[i][j] = '#'
            found = any(dfs(i+di, j+dj, k+1) for di, dj in [(-1,0),(1,0),(0,-1),(0,1)])
            board[i][j] = tmp
            return found
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))""", "pattern": "Backtracking / DFS", "time": "O(m*n*4^L)", "space": "O(L)", "approach": "DFS from each cell, mark visited, backtrack.", "pseudocode": "1. For each cell: start DFS if first char matches\n2. DFS: check bounds, mark visited, try 4 directions\n3. Backtrack: restore cell", "mermaid": ""},

80: {"code": """class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        write = 0
        for num in nums:
            if write < 2 or num != nums[write - 2]:
                nums[write] = num
                write += 1
        return write""", "pattern": "Two Pointers", "time": "O(n)", "space": "O(1)", "approach": "Write pointer allows at most 2 of each value.", "pseudocode": "1. write = 0\n2. For each num: if write<2 or num!=nums[write-2]: write it\n3. Return write", "mermaid": ""},

# Skipping to key milestone problems for brevity, filling all 395 would be enormous
# The generator will use the python3_snippet as fallback for problems without KB entries

81: {"code": """class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True
            if nums[lo] == nums[mid] == nums[hi]:
                lo += 1; hi -= 1
            elif nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False""", "pattern": "Binary Search", "time": "O(n) worst, O(log n) avg", "space": "O(1)", "approach": "Like problem 33 but handle duplicates by shrinking both ends when ambiguous.", "pseudocode": "1. Same as Search in Rotated Sorted Array\n2. When lo==mid==hi: shrink both ends\n3. Otherwise determine sorted half and search", "mermaid": ""},

84: {"code": """class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        heights.pop()
        return max_area""", "pattern": "Monotonic Stack", "time": "O(n)", "space": "O(n)", "approach": "**Key Insight:** Maintain a stack of increasing heights. When a shorter bar appears, pop and compute rectangles.", "pseudocode": "1. Stack of indices (increasing heights)\n2. For each bar: pop taller bars, compute area\n3. Width = i - stack[-1] - 1", "mermaid": """```mermaid
flowchart TD
    A[stack = empty, append 0 sentinel] --> B[For each bar i]
    B --> C{stack top taller than current?}
    C -- Yes --> D[Pop, compute area with popped height]
    D --> C
    C -- No --> E[Push i onto stack]
    E --> B
```"""},

85: {"code": """class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0
        n = len(matrix[0])
        heights = [0] * n
        max_area = 0
        for row in matrix:
            for j in range(n):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            # Largest rectangle in histogram
            stack = []
            h = heights + [0]
            for i in range(len(h)):
                while stack and h[stack[-1]] > h[i]:
                    height = h[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
        return max_area""", "pattern": "Monotonic Stack / DP", "time": "O(m*n)", "space": "O(n)", "approach": "Build histogram for each row, then apply Largest Rectangle in Histogram.", "pseudocode": "1. For each row: update heights (cumulative or reset)\n2. Apply problem 84 to each histogram\n3. Track global max area", "mermaid": ""},

88: {"code": """class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1""", "pattern": "Two Pointers / Merge", "time": "O(m+n)", "space": "O(1)", "approach": "Merge from the end to avoid overwriting. Fill nums1 from position m+n-1 backwards.", "pseudocode": "1. i=m-1, j=n-1, k=m+n-1\n2. While j >= 0: pick larger of nums1[i], nums2[j]\n3. Place at nums1[k], decrement pointers", "mermaid": ""},

90: {"code": """class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        def backtrack(start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return result""", "pattern": "Backtracking", "time": "O(2^n)", "space": "O(n)", "approach": "Sort + backtrack, skip duplicates at same recursion level.", "pseudocode": "1. Sort nums\n2. backtrack: record path, skip same-level dupes\n3. Recurse with i+1", "mermaid": ""},

91: {"code": """class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            two = int(s[i-2:i])
            if 10 <= two <= 26:
                dp[i] += dp[i-2]
        return dp[n]""", "pattern": "Dynamic Programming", "time": "O(n)", "space": "O(n)", "approach": "DP: dp[i] = ways to decode s[:i]. Check single digit and two-digit decodings.", "pseudocode": "1. dp[0]=dp[1]=1\n2. For i>=2: if single digit valid: dp[i]+=dp[i-1]; if two-digit valid: dp[i]+=dp[i-2]\n3. Return dp[n]", "mermaid": ""},

94: {"code": """class Solution:
    def inorderTraversal(self, root) -> list[int]:
        result = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result""", "pattern": "Tree Traversal / Stack", "time": "O(n)", "space": "O(n)", "approach": "Iterative inorder: go left as far as possible, pop and process, then go right.", "pseudocode": "1. Push all left nodes onto stack\n2. Pop, record value\n3. Move to right child, repeat", "mermaid": """```mermaid
flowchart TD
    A[curr = root] --> B{curr or stack?}
    B -- Yes --> C{curr not null?}
    C -- Yes --> D[Push curr, go left]
    D --> C
    C -- No --> E[Pop from stack]
    E --> F[Record value]
    F --> G[curr = right child]
    G --> B
    B -- No --> H[Return result]
```""", "animation_frames": """**Inorder Traversal of tree [1,null,2,3]:**

**Step 1:** Start at root 1, no left child

```mermaid
flowchart TD
    N1["1 *"] --> N2[null]
    N1 --> N3[2]
    N3 --> N4[3]
    N3 --> N5[null]
```

Stack: [1], Visit: 1

**Step 2:** Move to right child 2, go left to 3

```mermaid
flowchart TD
    N1[1] --> N2[null]
    N1 --> N3[2]
    N3 --> N4["3 *"]
    N3 --> N5[null]
```

Stack: [2,3], Visit: 3

**Step 3:** Pop 2, no right child

```mermaid
flowchart TD
    N1[1] --> N2[null]
    N1 --> N3["2 *"]
    N3 --> N4[3]
    N3 --> N5[null]
```

Result: [1, 3, 2]"""},

# Key tree problems
98: {"code": """class Solution:
    def isValidBST(self, root) -> bool:
        def validate(node, lo, hi):
            if not node:
                return True
            if node.val <= lo or node.val >= hi:
                return False
            return validate(node.left, lo, node.val) and validate(node.right, node.val, hi)
        return validate(root, float('-inf'), float('inf'))""", "pattern": "Tree / DFS", "time": "O(n)", "space": "O(h)", "approach": "DFS with bounds: each node must be within (lo, hi). Left subtree narrows hi, right narrows lo.", "pseudocode": "1. validate(node, lo, hi):\n   If null: True\n   If not lo < val < hi: False\n   Recurse left with (lo, val), right with (val, hi)", "mermaid": """```mermaid
flowchart TD
    A["validate(root, -inf, +inf)"] --> B{Node null?}
    B -- Yes --> C[Return True]
    B -- No --> D{lo < val < hi?}
    D -- No --> E[Return False]
    D -- Yes --> F["validate(left, lo, val)"]
    D -- Yes --> G["validate(right, val, hi)"]
```"""},

100: {"code": """class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)""", "pattern": "Tree / DFS", "time": "O(n)", "space": "O(h)", "approach": "Recursive comparison: both null = same, one null = different, else compare values and recurse.", "pseudocode": "1. Both null: True\n2. One null: False\n3. Values equal AND left same AND right same", "mermaid": ""},

101: {"code": """class Solution:
    def isSymmetric(self, root) -> bool:
        def mirror(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            return l.val == r.val and mirror(l.left, r.right) and mirror(l.right, r.left)
        return mirror(root.left, root.right) if root else True""", "pattern": "Tree / DFS", "time": "O(n)", "space": "O(h)", "approach": "Check if left subtree mirrors right subtree: compare l.left with r.right and l.right with r.left.", "pseudocode": "1. mirror(l, r):\n   Both null: True; one null: False\n   l.val == r.val AND mirror(l.left, r.right) AND mirror(l.right, r.left)", "mermaid": ""},

102: {"code": """from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        result = []
        queue = deque([root])
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
        return result""", "pattern": "BFS / Tree", "time": "O(n)", "space": "O(n)", "approach": "BFS with queue. Process one level at a time by tracking queue size.", "pseudocode": "1. Queue = [root]\n2. While queue not empty:\n   Process all nodes at current level\n   Add children to queue\n   Record level values", "mermaid": """```mermaid
flowchart TD
    A[Queue = root] --> B{Queue not empty?}
    B -- Yes --> C[Process current level]
    C --> D[Add children to queue]
    D --> E[Record level values]
    E --> B
    B -- No --> F[Return result]
```""", "animation_frames": """**Level Order BFS on tree [3,9,20,null,null,15,7]:**

**Step 1:** Level 0 - Process root

```mermaid
flowchart TD
    N3["3 *"] --> N9[9]
    N3 --> N20[20]
    N20 --> N15[15]
    N20 --> N7[7]
```

Queue: [3] -> Process -> Result: [[3]]

**Step 2:** Level 1 - Process 9 and 20

```mermaid
flowchart TD
    N3[3] --> N9["9 *"]
    N3 --> N20["20 *"]
    N20 --> N15[15]
    N20 --> N7[7]
```

Queue: [9,20] -> Process -> Result: [[3],[9,20]]

**Step 3:** Level 2 - Process 15 and 7

```mermaid
flowchart TD
    N3[3] --> N9[9]
    N3 --> N20[20]
    N20 --> N15["15 *"]
    N20 --> N7["7 *"]
```

Queue: [15,7] -> Process -> Result: [[3],[9,20],[15,7]]"""},

104: {"code": """class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))""", "pattern": "Tree / DFS", "time": "O(n)", "space": "O(h)", "approach": "Recursive: depth = 1 + max(left depth, right depth).", "pseudocode": "1. If null: return 0\n2. Return 1 + max(depth(left), depth(right))", "mermaid": ""},

121: {"code": """class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit""", "pattern": "Greedy / One Pass", "time": "O(n)", "space": "O(1)", "approach": "Track minimum price seen. At each price, compute potential profit = price - min_price.", "pseudocode": "1. min_price = inf, max_profit = 0\n2. For each price: update min, update max profit\n3. Return max_profit", "mermaid": """```mermaid
flowchart TD
    A[min_price = inf, max_profit = 0] --> B[For each price]
    B --> C[min_price = min of min_price and price]
    C --> D[max_profit = max of max_profit and price - min_price]
    D --> B
```"""},

128: {"code": """class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)
        return longest""", "pattern": "Hash Set", "time": "O(n)", "space": "O(n)", "approach": "**Key Insight:** Only start counting from sequence beginnings (num-1 not in set). Count forward.", "pseudocode": "1. num_set = set(nums)\n2. For each num: if num-1 not in set: count forward\n3. Track longest sequence", "mermaid": """```mermaid
flowchart TD
    A[Build hash set] --> B[For each num]
    B --> C{num-1 in set?}
    C -- Yes --> D[Not a start, skip]
    C -- No --> E[Count consecutive nums forward]
    E --> F[Update longest]
    D --> B
    F --> B
```"""},

136: {"code": """class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result""", "pattern": "Bit Manipulation (XOR)", "time": "O(n)", "space": "O(1)", "approach": "XOR all numbers. Pairs cancel out (a ^ a = 0), leaving the single number.", "pseudocode": "1. result = 0\n2. For each num: result ^= num\n3. Return result", "mermaid": ""},

141: {"code": """class Solution:
    def hasCycle(self, head) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False""", "pattern": "Fast and Slow Pointers", "time": "O(n)", "space": "O(1)", "approach": "**Floyd's Cycle Detection:** Slow moves 1 step, fast moves 2. If they meet, there's a cycle.", "pseudocode": "1. slow = fast = head\n2. While fast and fast.next:\n   slow++, fast+=2\n   If slow == fast: cycle!\n3. Return False", "mermaid": """```mermaid
flowchart TD
    A[slow = fast = head] --> B{fast and fast.next?}
    B -- Yes --> C[slow += 1, fast += 2]
    C --> D{slow == fast?}
    D -- Yes --> E[Return True - cycle]
    D -- No --> B
    B -- No --> F[Return False - no cycle]
```""", "animation_frames": """**Floyd's Cycle Detection on [3,2,0,-4] with cycle at pos 1:**

**Step 1:** Both at start

```mermaid
flowchart LR
    N3["3(S,F)"] --> N2[2] --> N0[0] --> N4[-4]
    N4 --> N2
```

**Step 2:** slow=2, fast=0

```mermaid
flowchart LR
    N3[3] --> N2["2(S)"] --> N0["0(F)"] --> N4[-4]
    N4 --> N2
```

**Step 3:** slow=0, fast=2 -- They meet!

```mermaid
flowchart LR
    N3[3] --> N2["2(F)"] --> N0["0(S)"] --> N4[-4]
    N4 --> N2
```

Cycle detected at step 3!"""},

146: {"code": """from collections import OrderedDict

class Solution:
    pass

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)""", "pattern": "Design / Hash Map + Linked List", "time": "O(1) per operation", "space": "O(capacity)", "approach": "OrderedDict gives O(1) access + ordering. Move to end on access, pop from front when full.", "pseudocode": "1. get: if exists, move to end, return value\n2. put: insert/update, move to end\n3. If over capacity: evict least recently used (front)", "mermaid": """```mermaid
flowchart TD
    A["get(key)"] --> B{key in cache?}
    B -- Yes --> C[Move to end, return value]
    B -- No --> D[Return -1]
    E["put(key, val)"] --> F[Insert/update, move to end]
    F --> G{Over capacity?}
    G -- Yes --> H[Evict LRU from front]
    G -- No --> I[Done]
```"""},

148: {"code": """class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        dummy = ListNode(0)
        curr = dummy
        while left and right:
            if left.val <= right.val:
                curr.next = left; left = left.next
            else:
                curr.next = right; right = right.next
            curr = curr.next
        curr.next = left or right
        return dummy.next""", "pattern": "Merge Sort / Linked List", "time": "O(n log n)", "space": "O(log n)", "approach": "Merge sort on linked list: find middle, split, sort halves, merge.", "pseudocode": "1. Find middle with slow/fast\n2. Split list in two\n3. Recursively sort each half\n4. Merge sorted halves", "mermaid": ""},

152: {"code": """class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_prod = min_prod = result = nums[0]
        for num in nums[1:]:
            if num < 0:
                max_prod, min_prod = min_prod, max_prod
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)
            result = max(result, max_prod)
        return result""", "pattern": "Dynamic Programming", "time": "O(n)", "space": "O(1)", "approach": "Track both max and min products (negatives can flip). Swap on negative numbers.", "pseudocode": "1. max_prod = min_prod = result = nums[0]\n2. For each num: if negative swap max/min\n3. Update max/min products\n4. Track global max", "mermaid": ""},

153: {"code": """class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]""", "pattern": "Binary Search", "time": "O(log n)", "space": "O(1)", "approach": "Binary search: if mid > hi, min is in right half; else in left half (including mid).", "pseudocode": "1. lo=0, hi=n-1\n2. While lo < hi: mid check\n3. If nums[mid] > nums[hi]: lo = mid+1\n4. Else: hi = mid\n5. Return nums[lo]", "mermaid": ""},

155: {"code": """class Solution:
    pass

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
        return self.min_stack[-1]""", "pattern": "Stack / Design", "time": "O(1) per operation", "space": "O(n)", "approach": "Maintain a parallel min stack that tracks the minimum at each level.", "pseudocode": "1. Two stacks: main + min tracker\n2. Push: push val and min(val, current min)\n3. Pop: pop both\n4. getMin: peek min stack", "mermaid": ""},

160: {"code": """class Solution:
    def getIntersectionNode(self, headA, headB):
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a""", "pattern": "Two Pointers", "time": "O(m+n)", "space": "O(1)", "approach": "**Key Insight:** When pointer a reaches end of list A, redirect to head of B (and vice versa). They meet at intersection or both reach null.", "pseudocode": "1. a=headA, b=headB\n2. While a != b:\n   a = a.next or headB\n   b = b.next or headA\n3. Return a (intersection or null)", "mermaid": ""},

169: {"code": """class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate""", "pattern": "Boyer-Moore Voting", "time": "O(n)", "space": "O(1)", "approach": "**Boyer-Moore Voting:** Maintain a candidate and count. The majority element survives all cancellations.", "pseudocode": "1. candidate=0, count=0\n2. For each num:\n   If count==0: candidate = num\n   count += 1 if same else -1\n3. Return candidate", "mermaid": ""},

198: {"code": """class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        prev2, prev1 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            prev2, prev1 = prev1, max(prev1, prev2 + nums[i])
        return prev1""", "pattern": "Dynamic Programming", "time": "O(n)", "space": "O(1)", "approach": "DP: rob[i] = max(rob[i-1], rob[i-2] + nums[i]). Can't rob adjacent houses.", "pseudocode": "1. prev2 = nums[0], prev1 = max(nums[0:2])\n2. For i >= 2: prev = max(skip, rob current + prev2)\n3. Return prev1", "mermaid": ""},

200: {"code": """class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            dfs(i+1, j); dfs(i-1, j); dfs(i, j+1); dfs(i, j-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count""", "pattern": "DFS / Graph", "time": "O(m*n)", "space": "O(m*n)", "approach": "For each unvisited '1', increment count and DFS to mark all connected land as visited.", "pseudocode": "1. For each cell:\n   If '1': count++, DFS to mark connected '1's as '0'\n2. Return count", "mermaid": """```mermaid
flowchart TD
    A[Scan grid] --> B{Cell == 1?}
    B -- Yes --> C[Increment island count]
    C --> D[DFS: mark all connected 1s as 0]
    B -- No --> E[Next cell]
    D --> E
```""", "animation_frames": """**DFS Island Counting on grid:**

**Step 1:** Find first '1' at (0,0), start DFS

```mermaid
flowchart TD
    subgraph Grid["Grid State"]
        R0["1* 1 1 1 0"]
        R1["1  1 0 1 0"]
        R2["1  1 0 0 0"]
        R3["0  0 0 0 0"]
    end
```

Island count: 1, DFS marks all connected 1s

**Step 2:** After DFS from (0,0), find next '1' at (0,3)

```mermaid
flowchart TD
    subgraph Grid["Grid State"]
        R0["0 0 0 1* 0"]
        R1["0 0 0 1  0"]
        R2["0 0 0 0  0"]
        R3["0 0 0 0  0"]
    end
```

Island count: 1 (all first island marked as 0)

**Step 3:** DFS from (0,3), marks connected. No more 1s.

```mermaid
flowchart TD
    subgraph Grid["Grid State"]
        R0["0 0 0 0 0"]
        R1["0 0 0 0 0"]
        R2["0 0 0 0 0"]
        R3["0 0 0 0 0"]
    end
```

Final count: 2 islands"""},

206: {"code": """class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev""", "pattern": "Linked List Reversal", "time": "O(n)", "space": "O(1)", "approach": "Iterative reversal: maintain prev and curr pointers, reverse links one at a time.", "pseudocode": "1. prev=None, curr=head\n2. While curr: save next, reverse link, advance\n3. Return prev", "mermaid": """```mermaid
flowchart TD
    A[prev=None, curr=head] --> B{curr not null?}
    B -- Yes --> C[nxt = curr.next]
    C --> D[curr.next = prev]
    D --> E[prev = curr, curr = nxt]
    E --> B
    B -- No --> F[Return prev]
```"""},

207: {"code": """from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return count == numCourses""", "pattern": "Topological Sort (BFS)", "time": "O(V+E)", "space": "O(V+E)", "approach": "**Kahn's Algorithm:** BFS with in-degree tracking. If all nodes are processed, no cycle exists.", "pseudocode": "1. Build adjacency list and in-degree array\n2. Queue all nodes with in-degree 0\n3. BFS: process node, decrement neighbors' in-degree\n4. If count == numCourses: no cycle", "mermaid": """```mermaid
flowchart TD
    A[Build graph and in-degrees] --> B[Queue nodes with in-degree 0]
    B --> C{Queue not empty?}
    C -- Yes --> D[Process node, count++]
    D --> E[Decrement neighbors in-degree]
    E --> F{In-degree becomes 0?}
    F -- Yes --> G[Add to queue]
    F -- No --> C
    G --> C
    C -- No --> H{count == numCourses?}
    H -- Yes --> I[Return True]
    H -- No --> J[Return False - cycle exists]
```"""},

215: {"code": """import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]""", "pattern": "Heap / Quickselect", "time": "O(n log k)", "space": "O(k)", "approach": "Use a min-heap of size k, or heapq.nlargest for simplicity.", "pseudocode": "1. Return the kth largest using heap\n2. heapq.nlargest(k, nums)[-1]", "mermaid": ""},

226: {"code": """class Solution:
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root""", "pattern": "Tree / DFS", "time": "O(n)", "space": "O(h)", "approach": "Recursively swap left and right children.", "pseudocode": "1. If null: return None\n2. Swap left and right subtrees recursively\n3. Return root", "mermaid": ""},

230: {"code": """class Solution:
    def kthSmallest(self, root, k: int) -> int:
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
        return -1""", "pattern": "Tree / Inorder Traversal", "time": "O(h+k)", "space": "O(h)", "approach": "Inorder traversal gives sorted order. Stop at kth element.", "pseudocode": "1. Inorder traversal with stack\n2. Decrement k on each visit\n3. When k==0: return current value", "mermaid": ""},

236: {"code": """class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right""", "pattern": "Tree / DFS", "time": "O(n)", "space": "O(h)", "approach": "**Key Insight:** If p and q are in different subtrees, current node is LCA. If both in same subtree, recurse.", "pseudocode": "1. If root is null, p, or q: return root\n2. Recurse left and right\n3. If both found: root is LCA\n4. Else return whichever found", "mermaid": """```mermaid
flowchart TD
    A[Check root] --> B{root is null, p, or q?}
    B -- Yes --> C[Return root]
    B -- No --> D[Search left subtree]
    D --> E[Search right subtree]
    E --> F{Both found?}
    F -- Yes --> G[Root is LCA]
    F -- No --> H[Return whichever found]
```"""},

238: {"code": """class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result""", "pattern": "Prefix/Suffix Products", "time": "O(n)", "space": "O(1) extra", "approach": "**Key Insight:** product except self = prefix product * suffix product. Two passes, no division.", "pseudocode": "1. Left pass: result[i] = product of all left elements\n2. Right pass: multiply by product of all right elements", "mermaid": """```mermaid
flowchart TD
    A[Left pass: prefix products] --> B[Right pass: multiply suffix products]
    B --> C[result_i = prefix_i * suffix_i]
```"""},

239: {"code": """from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        result = []
        for i in range(len(nums)):
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result""", "pattern": "Monotonic Deque", "time": "O(n)", "space": "O(k)", "approach": "**Monotonic decreasing deque:** Front is always the window max. Remove expired and smaller elements.", "pseudocode": "1. Deque stores indices in decreasing order of values\n2. Remove expired (outside window)\n3. Remove smaller than current from back\n4. Front = window max", "mermaid": """```mermaid
flowchart TD
    A[For each element i] --> B[Remove expired from front]
    B --> C[Remove smaller from back]
    C --> D[Append i to deque]
    D --> E{Window full?}
    E -- Yes --> F[Record deque front as max]
    E -- No --> A
```"""},

# More key problems...
268: {"code": """class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)""", "pattern": "Math / XOR", "time": "O(n)", "space": "O(1)", "approach": "Expected sum of 0..n minus actual sum gives the missing number.", "pseudocode": "1. expected = n*(n+1)/2\n2. Return expected - sum(nums)", "mermaid": ""},

283: {"code": """class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        write = 0
        for num in nums:
            if num != 0:
                nums[write] = num
                write += 1
        for i in range(write, len(nums)):
            nums[i] = 0""", "pattern": "Two Pointers", "time": "O(n)", "space": "O(1)", "approach": "Write non-zero elements to front, fill rest with zeros.", "pseudocode": "1. Write pointer: copy non-zeros forward\n2. Fill remaining with zeros", "mermaid": ""},

295: {"code": """import heapq

class Solution:
    pass

class MedianFinder:
    def __init__(self):
        self.lo = []  # max-heap (negated)
        self.hi = []  # min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2""", "pattern": "Two Heaps / Design", "time": "O(log n) add, O(1) find", "space": "O(n)", "approach": "**Two Heaps:** Max-heap for lower half, min-heap for upper half. Balance sizes.", "pseudocode": "1. addNum: push to lo, rebalance to hi, keep lo >= hi size\n2. findMedian: if unequal sizes, lo top; else average of tops", "mermaid": """```mermaid
flowchart TD
    A["addNum(num)"] --> B[Push to max-heap lo]
    B --> C[Move lo top to min-heap hi]
    C --> D{hi bigger than lo?}
    D -- Yes --> E[Move hi top to lo]
    D -- No --> F[Done]
    G[findMedian] --> H{Equal sizes?}
    H -- Yes --> I[Average of both tops]
    H -- No --> J[Lo top is median]
```"""},

297: {"code": """class Codec:
    def serialize(self, root):
        vals = []
        def dfs(node):
            if not node:
                vals.append('#')
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(vals)

    def deserialize(self, data):
        vals = iter(data.split(','))
        def dfs():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()""", "pattern": "Tree / DFS / Serialization", "time": "O(n)", "space": "O(n)", "approach": "Preorder DFS with '#' for nulls. Deserialize by consuming tokens in same order.", "pseudocode": "1. Serialize: preorder DFS, '#' for null\n2. Deserialize: consume tokens, reconstruct tree recursively", "mermaid": ""},

300: {"code": """class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        from bisect import bisect_left
        tails = []
        for num in nums:
            pos = bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        return len(tails)""", "pattern": "Binary Search / DP", "time": "O(n log n)", "space": "O(n)", "approach": "**Patience Sorting:** Maintain tails array. Binary search for insertion point.", "pseudocode": "1. tails = []\n2. For each num: binary search position in tails\n   If pos == end: append\n   Else: replace tails[pos]\n3. Return len(tails)", "mermaid": """```mermaid
flowchart TD
    A["tails = []"] --> B[For each num]
    B --> C[Binary search position in tails]
    C --> D{pos == end?}
    D -- Yes --> E[Append num]
    D -- No --> F["Replace tails[pos]"]
    E --> B
    F --> B
```"""},

322: {"code": """class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1""", "pattern": "Dynamic Programming", "time": "O(n * amount)", "space": "O(amount)", "approach": "**Unbounded knapsack:** dp[x] = min coins to make amount x. For each coin, update all reachable amounts.", "pseudocode": "1. dp[0] = 0, dp[1..amount] = inf\n2. For each coin: for x >= coin: dp[x] = min(dp[x], dp[x-coin]+1)\n3. Return dp[amount] or -1", "mermaid": """```mermaid
flowchart TD
    A["dp[0]=0, rest=inf"] --> B[For each coin]
    B --> C[For x from coin to amount]
    C --> D["dp[x] = min(dp[x], dp[x-coin]+1)"]
    D --> C
    C --> B
    B --> E[Return dp amount]
```"""},

347: {"code": """from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        return [x for x, _ in count.most_common(k)]""", "pattern": "Hash Map / Heap", "time": "O(n log k)", "space": "O(n)", "approach": "Count frequencies, return k most common elements.", "pseudocode": "1. Count frequencies\n2. Return top k by frequency", "mermaid": ""},

416: {"code": """class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        return dp[target]""", "pattern": "Dynamic Programming (0/1 Knapsack)", "time": "O(n * sum/2)", "space": "O(sum/2)", "approach": "Reduce to subset sum: can we find subset summing to total/2? Use 1D DP.", "pseudocode": "1. If total is odd: False\n2. target = total/2\n3. dp[0] = True\n4. For each num: update dp backwards\n5. Return dp[target]", "mermaid": ""},

# Graph problems
261: {"code": """class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            parent[ra] = rb
        return True""", "pattern": "Union Find", "time": "O(n * alpha(n))", "space": "O(n)", "approach": "A graph is a tree if it has n-1 edges and no cycles. Use Union-Find to detect cycles.", "pseudocode": "1. If edges != n-1: False\n2. Union-Find: for each edge, if same root: cycle\n3. Return True if no cycle", "mermaid": ""},

}

# Make all entries have consistent keys
_DEFAULT_KEYS = {"code": "", "pattern": "", "time": "", "space": "", "approach": "", "pseudocode": "", "mermaid": "", "walkthrough": "", "animation_frames": ""}
for pid in SOLUTIONS_KB:
    for key, default in _DEFAULT_KEYS.items():
        SOLUTIONS_KB[pid].setdefault(key, default)
