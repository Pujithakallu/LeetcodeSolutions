/*
 * Problem 838: Push Dominoes
 * =========================
 * Difficulty: Medium
 * Tags: Two Pointers, String, Dynamic Programming
 * Pattern: Two Pass Simulation
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string pushDominoes(string& dominoes) {
        // String DP - O(m*n) time and space
        int m = dominoes.size(), n = dominoes.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (dominoes[i-1] == dominoes[j-1])
                    dp[i][j] = dp[i-1][j-1] + 1;
                else
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
        return dp[m][n];
    }
};
