/*
 * Problem 1143: Longest Common Subsequence
 * ======================================
 * Difficulty: Medium
 * Tags: String, Dynamic Programming
 * Pattern: Dynamic Programming
 *
 * Time Complexity:  O(m*n)
 * Space Complexity: O(n)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string& text1, string& text2) {
        // String DP - O(m*n) time and space
        int m = text1.size(), n = text2.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (text1[i-1] == text2[j-1])
                    dp[i][j] = dp[i-1][j-1] + 1;
                else
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
        return dp[m][n];
    }
};
