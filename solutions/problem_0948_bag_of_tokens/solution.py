"""
Problem 948: Bag of Tokens
=========================
Difficulty: Medium
Tags: Array, Two Pointers, Greedy, Sorting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # Sort + greedy - O(n log n) time
        tokens.sort()
        result = 0
        curr_end = 0
        for item in tokens:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
