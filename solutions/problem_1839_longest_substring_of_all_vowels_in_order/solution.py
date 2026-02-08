"""
Problem 1839: Longest Substring Of All Vowels in Order
====================================================
Difficulty: Medium
Tags: String, Sliding Window
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(word)):
            window[word[right]] += 1
            while len(window) > (word if isinstance(word, int) else len(word)):
                window[word[left]] -= 1
                if window[word[left]] == 0:
                    del window[word[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
