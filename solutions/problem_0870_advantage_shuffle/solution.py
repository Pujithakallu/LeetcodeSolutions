"""
Problem 870: Advantage Shuffle
=============================
Difficulty: Medium
Tags: Array, Two Pointers, Greedy, Sorting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Sort + greedy - O(n log n) time
        nums1.sort()
        result = 0
        curr_end = 0
        for item in nums1:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
