"""
Problem 1016: Binary String With Substrings Representing 1 To N
=============================================================
Difficulty: Medium
Tags: Hash Table, String, Bit Manipulation, Sliding Window
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def queryString(self, s: str, n: int) -> bool:
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(s)):
            window[s[right]] += 1
            while len(window) > (n if isinstance(n, int) else len(s)):
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
