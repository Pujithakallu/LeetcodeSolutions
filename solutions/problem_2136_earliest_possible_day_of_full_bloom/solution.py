"""
Problem 2136: Earliest Possible Day of Full Bloom
===============================================
Difficulty: Hard
Tags: Array, Greedy, Sorting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # Sort + greedy - O(n log n) time
        plantTime.sort()
        result = 0
        curr_end = 0
        for item in plantTime:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
