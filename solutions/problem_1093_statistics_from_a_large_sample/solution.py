"""
Problem 1093: Statistics from a Large Sample
==========================================
Difficulty: Medium
Tags: Array, Math, Probability and Statistics
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        # Mathematical approach
        result = 0
        x = count
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
