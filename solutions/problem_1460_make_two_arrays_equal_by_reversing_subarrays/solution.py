"""
Problem 1460: Make Two Arrays Equal by Reversing Subarrays
========================================================
Difficulty: Easy
Tags: Array, Hash Table, Sorting
Pattern: Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # Sort-based approach - O(n log n) time
        target.sort(key=lambda x: x[0] if isinstance(x, (list, tuple)) else x)
        result = [target[0]]
        for i in range(1, len(target)):
            curr = target[i]
            if isinstance(curr, (list, tuple)) and isinstance(result[-1], (list, tuple)):
                if curr[0] <= result[-1][1]:
                    result[-1] = [result[-1][0], max(result[-1][1], curr[1])]
                else:
                    result.append(curr)
            else:
                result.append(curr)
        return result
