"""
Problem 1268: Search Suggestions System
=====================================
Difficulty: Medium
Tags: Array, String, Binary Search, Trie, Sorting, Heap (Priority Queue)
Pattern: Binary Search / Trie

Time Complexity:  O(n log n + m*log n)
Space Complexity: O(1) extra
"""

class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        result = []
        prefix = ''
        start = 0
        for c in searchWord:
            prefix += c
            import bisect
            start = bisect.bisect_left(products, prefix, start)
            end = bisect.bisect_left(products, prefix[:-1] + chr(ord(prefix[-1]) + 1), start)
            result.append(products[start:min(start + 3, end)])
        return result
