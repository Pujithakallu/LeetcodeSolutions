"""
Problem 1702: Maximum Binary String After Change
==============================================
Difficulty: Medium
Tags: String, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(binary)):
            if isinstance(binary[i], int):
                curr_max = max(curr_max, binary[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
