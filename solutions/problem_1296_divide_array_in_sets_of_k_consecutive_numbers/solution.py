"""
Problem 1296: Divide Array in Sets of K Consecutive Numbers
=========================================================
Difficulty: Medium
Tags: Array, Hash Table, Greedy, Sorting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        # Sort + greedy - O(n log n) time
        nums.sort()
        result = 0
        curr_end = 0
        for item in nums:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
