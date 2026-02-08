"""
Problem 2094: Finding 3-Digit Even Numbers
========================================
Difficulty: Easy
Tags: Array, Hash Table, Recursion, Sorting, Enumeration
Pattern: Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # Sort-based approach - O(n log n) time
        digits.sort(key=lambda x: x[0] if isinstance(x, (list, tuple)) else x)
        result = [digits[0]]
        for i in range(1, len(digits)):
            curr = digits[i]
            if isinstance(curr, (list, tuple)) and isinstance(result[-1], (list, tuple)):
                if curr[0] <= result[-1][1]:
                    result[-1] = [result[-1][0], max(result[-1][1], curr[1])]
                else:
                    result.append(curr)
            else:
                result.append(curr)
        return result
