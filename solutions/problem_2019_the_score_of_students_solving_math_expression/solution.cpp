/*
 * Problem 2019: The Score of Students Solving Math Expression
 * =========================================================
 * Difficulty: Hard
 * Tags: Array, Hash Table, Math, String, Dynamic Programming, Stack, Memoization
 * Pattern: Dynamic Programming (String)
 *
 * Time Complexity:  O(m * n)
 * Space Complexity: O(m * n)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int scoreOfStudents(string& s, vector<int>& answers) {
        // String DP - O(m*n) time and space
        int m = s.size(), n = answers.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s[i-1] == answers[j-1])
                    dp[i][j] = dp[i-1][j-1] + 1;
                else
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
        return dp[m][n];
    }
};
