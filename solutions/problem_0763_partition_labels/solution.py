"""
Problem 763: Partition Labels
============================
Difficulty: Medium
Tags: Hash Table, Two Pointers, String, Greedy
Pattern: Greedy / Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {c: i for i, c in enumerate(s)}
        result = []
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                result.append(end - start + 1)
                start = end + 1
        return result
