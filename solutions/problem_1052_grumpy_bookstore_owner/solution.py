"""
Problem 1052: Grumpy Bookstore Owner
==================================
Difficulty: Medium
Tags: Array, Sliding Window
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(customers)):
            window[customers[right]] += 1
            while len(window) > (grumpy if isinstance(grumpy, int) else len(customers)):
                window[customers[left]] -= 1
                if window[customers[left]] == 0:
                    del window[customers[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
