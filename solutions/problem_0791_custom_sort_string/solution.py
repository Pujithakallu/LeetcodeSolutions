"""
Problem 791: Custom Sort String
==============================
Difficulty: Medium
Tags: Hash Table, String, Sorting
Pattern: Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Sort-based approach - O(n log n) time
        order.sort(key=lambda x: x[0] if isinstance(x, (list, tuple)) else x)
        result = [order[0]]
        for i in range(1, len(order)):
            curr = order[i]
            if isinstance(curr, (list, tuple)) and isinstance(result[-1], (list, tuple)):
                if curr[0] <= result[-1][1]:
                    result[-1] = [result[-1][0], max(result[-1][1], curr[1])]
                else:
                    result.append(curr)
            else:
                result.append(curr)
        return result
