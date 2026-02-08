"""
Problem 1859: Sorting the Sentence
================================
Difficulty: Easy
Tags: String, Sorting
Pattern: Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def sortSentence(self, s: str) -> str:
        # Sort-based approach - O(n log n) time
        s.sort(key=lambda x: x[0] if isinstance(x, (list, tuple)) else x)
        result = [s[0]]
        for i in range(1, len(s)):
            curr = s[i]
            if isinstance(curr, (list, tuple)) and isinstance(result[-1], (list, tuple)):
                if curr[0] <= result[-1][1]:
                    result[-1] = [result[-1][0], max(result[-1][1], curr[1])]
                else:
                    result.append(curr)
            else:
                result.append(curr)
        return result
