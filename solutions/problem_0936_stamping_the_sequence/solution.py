"""
Problem 936: Stamping The Sequence
=================================
Difficulty: Hard
Tags: String, Stack, Greedy, Queue
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(stamp)):
            if isinstance(stamp[i], int):
                curr_max = max(curr_max, stamp[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
