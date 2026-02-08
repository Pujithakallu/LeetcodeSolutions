"""
Problem 1491: Average Salary Excluding the Minimum and Maximum Salary
===================================================================
Difficulty: Easy
Tags: Array, Sorting
Pattern: Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def average(self, salary: List[int]) -> float:
        # Sort-based approach - O(n log n) time
        salary.sort(key=lambda x: x[0] if isinstance(x, (list, tuple)) else x)
        result = [salary[0]]
        for i in range(1, len(salary)):
            curr = salary[i]
            if isinstance(curr, (list, tuple)) and isinstance(result[-1], (list, tuple)):
                if curr[0] <= result[-1][1]:
                    result[-1] = [result[-1][0], max(result[-1][1], curr[1])]
                else:
                    result.append(curr)
            else:
                result.append(curr)
        return result
