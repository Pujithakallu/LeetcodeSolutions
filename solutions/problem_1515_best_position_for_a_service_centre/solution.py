"""
Problem 1515: Best Position for a Service Centre
==============================================
Difficulty: Hard
Tags: Array, Math, Geometry, Randomized
Pattern: Randomized Algorithm

Time Complexity:  O(n) or varies
Space Complexity: O(n)
"""

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        # Randomized approach
        import random
        # Fisher-Yates shuffle or random sampling
        arr = list(positions)
        for i in range(len(arr) - 1, 0, -1):
            j = random.randint(0, i)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
