"""
Problem 984: String Without AAA or BBB
=====================================
Difficulty: Medium
Tags: String, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(a)):
            if isinstance(a[i], int):
                curr_max = max(curr_max, a[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
