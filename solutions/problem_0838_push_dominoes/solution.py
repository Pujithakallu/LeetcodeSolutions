"""
Problem 838: Push Dominoes
=========================
Difficulty: Medium
Tags: Two Pointers, String, Dynamic Programming
Pattern: Two Pass Simulation

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        d = list(dominoes)
        n = len(d)
        forces = [0] * n
        f = 0
        for i in range(n):
            if d[i] == 'R':
                f = n
            elif d[i] == 'L':
                f = 0
            else:
                f = max(f - 1, 0)
            forces[i] += f
        f = 0
        for i in range(n - 1, -1, -1):
            if d[i] == 'L':
                f = n
            elif d[i] == 'R':
                f = 0
            else:
                f = max(f - 1, 0)
            forces[i] -= f
        return ''.join('R' if f > 0 else 'L' if f < 0 else '.' for f in forces)
