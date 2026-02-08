"""
Problem 981: Time Based Key-Value Store
======================================
Difficulty: Medium
Tags: Hash Table, String, Binary Search, Design
Pattern: Binary Search / Design

Time Complexity:  O(log n) get, O(1) set
Space Complexity: O(n)
"""

class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''
        vals = self.store[key]
        lo, hi = 0, len(vals) - 1
        result = ''
        while lo <= hi:
            mid = (lo + hi) // 2
            if vals[mid][0] <= timestamp:
                result = vals[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
        return result
