/*
 * Problem 2086: Minimum Number of Food Buckets to Feed the Hamsters
 * ===============================================================
 * Difficulty: Medium
 * Tags: String, Dynamic Programming, Greedy
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
    int minimumBuckets(string& hamsters) {
        // String DP - O(m*n) time and space
        int m = hamsters.size(), n = hamsters.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (hamsters[i-1] == hamsters[j-1])
                    dp[i][j] = dp[i-1][j-1] + 1;
                else
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
        return dp[m][n];
    }
};
