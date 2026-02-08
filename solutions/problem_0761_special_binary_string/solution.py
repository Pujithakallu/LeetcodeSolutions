"""
Problem 761: Special Binary String
=================================
Difficulty: Hard
Tags: String, Divide and Conquer, Sorting
Pattern: Divide and Conquer

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # Divide and conquer approach - O(n log n) time
        def solve(left, right):
            if left >= right:
                return s[left] if left < len(s) else 0
            mid = (left + right) // 2
            left_result = solve(left, mid)
            right_result = solve(mid + 1, right)
            return max(left_result, right_result)  # merge step
        
        return solve(0, len(s) - 1) if s else ""
