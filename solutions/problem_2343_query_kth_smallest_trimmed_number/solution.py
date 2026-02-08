"""
Problem 2343: Query Kth Smallest Trimmed Number
=============================================
Difficulty: Medium
Tags: Array, String, Divide and Conquer, Sorting, Heap (Priority Queue), Radix Sort, Quickselect
Pattern: Quickselect

Time Complexity:  O(n) average
Space Complexity: O(1)
"""

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
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
        
        k = queries if isinstance(queries, int) else 1
        return quickselect(nums, len(nums) - k)
