"""
Problem 1738: Find Kth Largest XOR Coordinate Value
=================================================
Difficulty: Medium
Tags: Array, Divide and Conquer, Bit Manipulation, Sorting, Heap (Priority Queue), Matrix, Prefix Sum, Quickselect
Pattern: Quickselect

Time Complexity:  O(n) average
Space Complexity: O(1)
"""

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        # Quickselect - O(n) average time
        import random
        def quickselect(arr, k):
            if len(arr) == 1:
                return arr[0]
            pivot = random.choice(arr)
            lows = [x for x in arr if x < pivot]
            highs = [x for x in arr if x > pivot]
            pivots = [x for x in arr if x == pivot]
            if k < len(lows):
                return quickselect(lows, k)
            elif k < len(lows) + len(pivots):
                return pivot
            else:
                return quickselect(highs, k - len(lows) - len(pivots))
        
        k = k if isinstance(k, int) else 1
        return quickselect(matrix, len(matrix) - k)
