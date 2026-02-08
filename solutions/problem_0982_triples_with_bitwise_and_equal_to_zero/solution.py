"""
Problem 982: Triples with Bitwise AND Equal To Zero
==================================================
Difficulty: Hard
Tags: Array, Hash Table, Bit Manipulation
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in nums:
            result ^= val
        return result
