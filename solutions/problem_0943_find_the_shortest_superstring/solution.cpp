/*
 * Problem 943: Find the Shortest Superstring
 * =========================================
 * Difficulty: Hard
 * Tags: Array, String, Dynamic Programming, Bit Manipulation, Bitmask
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
    string shortestSuperstring(vector<string>& words) {
        // String DP - O(m*n) time and space
        int m = words.size(), n = words.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (words[i-1] == words[j-1])
                    dp[i][j] = dp[i-1][j-1] + 1;
                else
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
        return dp[m][n];
    }
};
