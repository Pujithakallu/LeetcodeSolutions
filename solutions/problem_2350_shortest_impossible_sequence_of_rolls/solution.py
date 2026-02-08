"""
Problem 2350: Shortest Impossible Sequence of Rolls
=================================================
Difficulty: Hard
Tags: Array, Hash Table, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(rolls)):
            if isinstance(rolls[i], int):
                curr_max = max(curr_max, rolls[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
