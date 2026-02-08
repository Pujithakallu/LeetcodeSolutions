"""
Problem 621: Task Scheduler
==========================
Difficulty: Medium
Tags: Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Counting
Pattern: Greedy / Math

Time Complexity:  O(n)
Space Complexity: O(1)
"""

from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = Counter(tasks)
        max_count = max(counts.values())
        num_max = sum(1 for v in counts.values() if v == max_count)
        result = (max_count - 1) * (n + 1) + num_max
        return max(result, len(tasks))
