"""
Problem 2160: Minimum Sum of Four Digit Number After Splitting Digits
===================================================================
Difficulty: Easy
Tags: Math, Greedy, Sorting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def minimumSum(self, num: int) -> int:
        # Sort + greedy - O(n log n) time
        num.sort()
        result = 0
        curr_end = 0
        for item in num:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
