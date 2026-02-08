"""
Problem 2418: Sort the People
===========================
Difficulty: Easy
Tags: Array, Hash Table, String, Sorting
Pattern: Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Sort-based approach - O(n log n) time
        names.sort(key=lambda x: x[0] if isinstance(x, (list, tuple)) else x)
        result = [names[0]]
        for i in range(1, len(names)):
            curr = names[i]
            if isinstance(curr, (list, tuple)) and isinstance(result[-1], (list, tuple)):
                if curr[0] <= result[-1][1]:
                    result[-1] = [result[-1][0], max(result[-1][1], curr[1])]
                else:
                    result.append(curr)
            else:
                result.append(curr)
        return result
