"""
Problem 1850: Minimum Adjacent Swaps to Reach the Kth Smallest Number
===================================================================
Difficulty: Medium
Tags: Two Pointers, String, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(num)):
            if isinstance(num[i], int):
                curr_max = max(curr_max, num[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
