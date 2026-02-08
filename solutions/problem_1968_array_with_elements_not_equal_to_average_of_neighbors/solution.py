"""
Problem 1968: Array With Elements Not Equal to Average of Neighbors
=================================================================
Difficulty: Medium
Tags: Array, Greedy, Sorting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
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
