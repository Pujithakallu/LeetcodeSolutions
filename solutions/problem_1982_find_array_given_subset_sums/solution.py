"""
Problem 1982: Find Array Given Subset Sums
========================================
Difficulty: Hard
Tags: Array, Divide and Conquer
Pattern: Divide and Conquer

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        # Divide and conquer approach - O(n log n) time
        def solve(left, right):
            if left >= right:
                return n[left] if left < len(n) else 0
            mid = (left + right) // 2
            left_result = solve(left, mid)
            right_result = solve(mid + 1, right)
            return max(left_result, right_result)  # merge step
        
        return solve(0, len(n) - 1) if n else []
