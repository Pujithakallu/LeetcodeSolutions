"""
Problem 470: Implement Rand10() Using Rand7()
============================================
Difficulty: Medium
Tags: Math, Rejection Sampling, Randomized, Probability and Statistics
Pattern: Randomized Algorithm

Time Complexity:  O(n) or varies
Space Complexity: O(n)
"""

class Solution:
    def rand10(self) -> None:
        # Randomized approach
        import random
        # Fisher-Yates shuffle or random sampling
        arr = list(nums)
        for i in range(len(arr) - 1, 0, -1):
            j = random.randint(0, i)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
