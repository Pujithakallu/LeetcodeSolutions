"""
Problem 1481: Least Number of Unique Integers after K Removals
============================================================
Difficulty: Medium
Tags: Array, Hash Table, Greedy, Sorting, Counting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Sort + greedy - O(n log n) time
        arr.sort()
        result = 0
        curr_end = 0
        for item in arr:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
