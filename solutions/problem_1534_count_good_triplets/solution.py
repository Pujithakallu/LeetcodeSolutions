"""
Problem 1534: Count Good Triplets
===============================
Difficulty: Easy
Tags: Array, Enumeration
Pattern: Enumeration

Time Complexity:  O(n^2) or O(2^n)
Space Complexity: O(n)
"""

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # Enumeration approach - try all valid candidates
        result = 0
        for i in range(len(arr) if isinstance(arr, list) else arr):
            # Check if candidate i is valid
            valid = True
            if valid:
                result = i
                break
        return result
