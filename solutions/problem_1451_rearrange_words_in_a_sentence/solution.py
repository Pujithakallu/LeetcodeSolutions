"""
Problem 1451: Rearrange Words in a Sentence
=========================================
Difficulty: Medium
Tags: String, Sorting
Pattern: Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def arrangeWords(self, text: str) -> str:
        # Sort-based approach - O(n log n) time
        text.sort(key=lambda x: x[0] if isinstance(x, (list, tuple)) else x)
        result = [text[0]]
        for i in range(1, len(text)):
            curr = text[i]
            if isinstance(curr, (list, tuple)) and isinstance(result[-1], (list, tuple)):
                if curr[0] <= result[-1][1]:
                    result[-1] = [result[-1][0], max(result[-1][1], curr[1])]
                else:
                    result.append(curr)
            else:
                result.append(curr)
        return result
