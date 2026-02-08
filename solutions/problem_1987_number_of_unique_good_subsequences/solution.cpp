/*
 * Problem 1987: Number of Unique Good Subsequences
 * ==============================================
 * Difficulty: Hard
 * Tags: String, Dynamic Programming
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
    int numberOfUniqueGoodSubsequences(string& binary) {
        // String DP - O(m*n) time and space
        int m = binary.size(), n = binary.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (binary[i-1] == binary[j-1])
                    dp[i][j] = dp[i-1][j-1] + 1;
                else
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
        return dp[m][n];
    }
};
