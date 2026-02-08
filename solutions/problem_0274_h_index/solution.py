"""
Problem 274: H-Index
===================
Difficulty: Medium
Tags: Array, Sorting, Counting Sort
Pattern: Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort-based approach - O(n log n) time
        citations.sort(key=lambda x: x[0] if isinstance(x, (list, tuple)) else x)
        result = [citations[0]]
        for i in range(1, len(citations)):
            curr = citations[i]
            if isinstance(curr, (list, tuple)) and isinstance(result[-1], (list, tuple)):
                if curr[0] <= result[-1][1]:
                    result[-1] = [result[-1][0], max(result[-1][1], curr[1])]
                else:
                    result.append(curr)
            else:
                result.append(curr)
        return result
