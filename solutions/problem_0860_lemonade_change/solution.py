"""
Problem 860: Lemonade Change
===========================
Difficulty: Easy
Tags: Array, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(bills)):
            if isinstance(bills[i], int):
                curr_max = max(curr_max, bills[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
