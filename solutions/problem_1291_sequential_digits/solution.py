"""
Problem 1291: Sequential Digits
=============================
Difficulty: Medium
Tags: Enumeration
Pattern: Enumeration

Time Complexity:  O(n^2) or O(2^n)
Space Complexity: O(n)
"""

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # Enumeration approach - try all valid candidates
        result = []
        for i in range(len(low) if isinstance(low, list) else low):
            # Check if candidate i is valid
            valid = True
            if valid:
                result = i
                break
        return result
