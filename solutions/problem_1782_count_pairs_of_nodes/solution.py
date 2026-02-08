"""
Problem 1782: Count Pairs Of Nodes
================================
Difficulty: Hard
Tags: Array, Hash Table, Two Pointers, Binary Search, Graph Theory, Sorting, Counting
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(n) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if n[mid] == edges:
                return mid
            elif n[mid] < edges:
                lo = mid + 1
            else:
                hi = mid - 1
        return []
