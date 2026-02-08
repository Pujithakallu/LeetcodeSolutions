/*
 * Problem 63: Unique Paths II
 * ===========================
 * Difficulty: Medium
 * Tags: Array, Dynamic Programming, Matrix
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
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        // Dynamic programming (2D) - O(m*n) time and space
        if (obstacleGrid.empty()) return 0;
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
        return dp[m][n];
    }
};
