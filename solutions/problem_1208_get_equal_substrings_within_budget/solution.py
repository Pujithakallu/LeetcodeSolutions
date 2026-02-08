"""
Problem 1208: Get Equal Substrings Within Budget
==============================================
Difficulty: Medium
Tags: String, Binary Search, Sliding Window, Prefix Sum
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(s)):
            window[s[right]] += 1
            while len(window) > (t if isinstance(t, int) else len(s)):
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
