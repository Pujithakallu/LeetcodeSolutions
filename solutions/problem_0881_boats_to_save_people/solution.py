"""
Problem 881: Boats to Save People
================================
Difficulty: Medium
Tags: Array, Two Pointers, Greedy, Sorting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort + greedy - O(n log n) time
        people.sort()
        result = 0
        curr_end = 0
        for item in people:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
