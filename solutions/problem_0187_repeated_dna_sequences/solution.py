"""
Problem 187: Repeated DNA Sequences
==================================
Difficulty: Medium
Tags: Hash Table, String, Bit Manipulation, Sliding Window, Rolling Hash, Hash Function
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(s)):
            window[s[right]] += 1
            while len(window) > (s if isinstance(s, int) else len(s)):
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
