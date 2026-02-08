"""
Problem 1604: Alert Using Same Key-Card Three or More Times in a One Hour Period
==============================================================================
Difficulty: Medium
Tags: Array, Hash Table, String, Sorting
Pattern: Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        # Sort-based approach - O(n log n) time
        keyName.sort(key=lambda x: x[0] if isinstance(x, (list, tuple)) else x)
        result = [keyName[0]]
        for i in range(1, len(keyName)):
            curr = keyName[i]
            if isinstance(curr, (list, tuple)) and isinstance(result[-1], (list, tuple)):
                if curr[0] <= result[-1][1]:
                    result[-1] = [result[-1][0], max(result[-1][1], curr[1])]
                else:
                    result.append(curr)
            else:
                result.append(curr)
        return result
