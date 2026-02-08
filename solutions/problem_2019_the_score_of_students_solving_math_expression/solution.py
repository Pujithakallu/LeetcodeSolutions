"""
Problem 2019: The Score of Students Solving Math Expression
=========================================================
Difficulty: Hard
Tags: Array, Hash Table, Math, String, Dynamic Programming, Stack, Memoization
Pattern: Dynamic Programming (String)

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""

class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        # String DP - O(m*n) time and space
        m, n = len(s), len(answers)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i-1] == answers[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
