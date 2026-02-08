"""
Problem 38: Count and Say
=========================
Difficulty: Medium
Tags: String
Pattern: String Simulation

Time Complexity:  O(2^n) worst case
Space Complexity: O(2^n)
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            result = []
            i = 0
            while i < len(s):
                count = 1
                while i + count < len(s) and s[i + count] == s[i]:
                    count += 1
                result.append(str(count) + s[i])
                i += count
            s = ''.join(result)
        return s
