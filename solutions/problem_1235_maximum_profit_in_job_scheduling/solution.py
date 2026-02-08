"""
Problem 1235: Maximum Profit in Job Scheduling
============================================
Difficulty: Hard
Tags: Array, Binary Search, Dynamic Programming, Sorting
Pattern: Dynamic Programming + Binary Search

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

import bisect

class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)
        dp = [0] * (n + 1)
        ends = [j[1] for j in jobs]
        for i in range(1, n + 1):
            s, e, p = jobs[i-1]
            j = bisect.bisect_right(ends, s, 0, i-1)
            dp[i] = max(dp[i-1], dp[j] + p)
        return dp[n]
