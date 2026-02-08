"""
Problem 2412: Minimum Money Required Before Transactions
======================================================
Difficulty: Hard
Tags: Array, Greedy, Sorting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        # Sort + greedy - O(n log n) time
        transactions.sort()
        result = 0
        curr_end = 0
        for item in transactions:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
