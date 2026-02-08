"""
Problem 372: Super Pow
=====================
Difficulty: Medium
Tags: Math, Divide and Conquer
Pattern: Divide and Conquer

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        # Divide and conquer approach - O(n log n) time
        def solve(left, right):
            if left >= right:
                return a[left] if left < len(a) else 0
            mid = (left + right) // 2
            left_result = solve(left, mid)
            right_result = solve(mid + 1, right)
            return max(left_result, right_result)  # merge step
        
        return solve(0, len(a) - 1) if a else 0
