"""
Problem 1156: Swap For Longest Repeated Character Substring
=========================================================
Difficulty: Medium
Tags: Hash Table, String, Sliding Window
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(text)):
            window[text[right]] += 1
            while len(window) > (text if isinstance(text, int) else len(text)):
                window[text[left]] -= 1
                if window[text[left]] == 0:
                    del window[text[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
