"""
Problem 1652: Defuse the Bomb
===========================
Difficulty: Easy
Tags: Array, Sliding Window
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(code)):
            window[code[right]] += 1
            while len(window) > (k if isinstance(k, int) else len(code)):
                window[code[left]] -= 1
                if window[code[left]] == 0:
                    del window[code[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
