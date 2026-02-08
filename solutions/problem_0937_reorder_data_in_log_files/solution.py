"""
Problem 937: Reorder Data in Log Files
=====================================
Difficulty: Medium
Tags: Array, String, Sorting
Pattern: Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # Sort-based approach - O(n log n) time
        logs.sort(key=lambda x: x[0] if isinstance(x, (list, tuple)) else x)
        result = [logs[0]]
        for i in range(1, len(logs)):
            curr = logs[i]
            if isinstance(curr, (list, tuple)) and isinstance(result[-1], (list, tuple)):
                if curr[0] <= result[-1][1]:
                    result[-1] = [result[-1][0], max(result[-1][1], curr[1])]
                else:
                    result.append(curr)
            else:
                result.append(curr)
        return result
