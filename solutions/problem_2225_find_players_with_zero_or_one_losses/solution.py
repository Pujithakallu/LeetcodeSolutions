"""
Problem 2225: Find Players With Zero or One Losses
================================================
Difficulty: Medium
Tags: Array, Hash Table, Sorting, Counting
Pattern: Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Sort-based approach - O(n log n) time
        matches.sort(key=lambda x: x[0] if isinstance(x, (list, tuple)) else x)
        result = [matches[0]]
        for i in range(1, len(matches)):
            curr = matches[i]
            if isinstance(curr, (list, tuple)) and isinstance(result[-1], (list, tuple)):
                if curr[0] <= result[-1][1]:
                    result[-1] = [result[-1][0], max(result[-1][1], curr[1])]
                else:
                    result.append(curr)
            else:
                result.append(curr)
        return result
