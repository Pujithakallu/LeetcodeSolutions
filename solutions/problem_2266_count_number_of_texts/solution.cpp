/*
 * Problem 2266: Count Number of Texts
 * =================================
 * Difficulty: Medium
 * Tags: Hash Table, Math, String, Dynamic Programming
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
    int countTexts(string& pressedKeys) {
        // String DP - O(m*n) time and space
        int m = pressedKeys.size(), n = pressedKeys.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (pressedKeys[i-1] == pressedKeys[j-1])
                    dp[i][j] = dp[i-1][j-1] + 1;
                else
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
        return dp[m][n];
    }
};
