"""
Problem 2037: Minimum Number of Moves to Seat Everyone
====================================================
Difficulty: Easy
Tags: Array, Greedy, Sorting, Counting Sort
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Sort + greedy - O(n log n) time
        seats.sort()
        result = 0
        curr_end = 0
        for item in seats:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
