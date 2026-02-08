"""
Problem 135: Candy
=================
Difficulty: Hard
Tags: Array, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(ratings)):
            if isinstance(ratings[i], int):
                curr_max = max(curr_max, ratings[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
