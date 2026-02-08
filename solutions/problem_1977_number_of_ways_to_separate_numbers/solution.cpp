/*
 * Problem 1977: Number of Ways to Separate Numbers
 * ==============================================
 * Difficulty: Hard
 * Tags: String, Dynamic Programming, Suffix Array
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
    int numberOfCombinations(string& num) {
        // String DP - O(m*n) time and space
        int m = num.size(), n = num.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (num[i-1] == num[j-1])
                    dp[i][j] = dp[i-1][j-1] + 1;
                else
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
        return dp[m][n];
    }
};
