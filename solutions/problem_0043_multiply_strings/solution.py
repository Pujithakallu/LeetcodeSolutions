"""
Problem 43: Multiply Strings
============================
Difficulty: Medium
Tags: Math, String, Simulation
Pattern: Math / String

Time Complexity:  O(m*n)
Space Complexity: O(m+n)
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - 48) * (ord(num2[j]) - 48)
                p1, p2 = i + j, i + j + 1
                total = mul + result[p2]
                result[p2] = total % 10
                result[p1] += total // 10
        result_str = ''.join(map(str, result)).lstrip('0')
        return result_str or '0'
