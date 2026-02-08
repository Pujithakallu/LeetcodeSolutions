"""
Problem 2193: Minimum Number of Moves to Make Palindrome
======================================================
Difficulty: Hard
Tags: Two Pointers, String, Greedy, Binary Indexed Tree
Pattern: Binary Indexed Tree / Fenwick Tree

Time Complexity:  O(n log n) build, O(log n) query/update
Space Complexity: O(n)
"""

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        # Binary Indexed Tree (Fenwick) - O(log n) update/query
        n = len(s)
        bit = [0] * (n + 1)
        
        def update(i, delta):
            i += 1
            while i <= n:
                bit[i] += delta
                i += i & (-i)
        
        def query(i):
            i += 1
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s
        
        for i, val in enumerate(s):
            update(i, val)
        return 0
