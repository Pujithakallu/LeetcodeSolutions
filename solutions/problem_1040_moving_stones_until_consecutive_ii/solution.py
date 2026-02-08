"""
Problem 1040: Moving Stones Until Consecutive II
==============================================
Difficulty: Medium
Tags: Array, Math, Sliding Window, Sorting
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(stones)):
            window[stones[right]] += 1
            while len(window) > (stones if isinstance(stones, int) else len(stones)):
                window[stones[left]] -= 1
                if window[stones[left]] == 0:
                    del window[stones[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
