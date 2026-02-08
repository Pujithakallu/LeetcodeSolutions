/*
 * Problem 1937: Maximum Number of Points with Cost
 * ==============================================
 * Difficulty: Medium
 * Tags: Array, Dynamic Programming, Matrix
 * Pattern: Dynamic Programming (2D Grid/Matrix)
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
    int maxPoints(vector<vector<int>>& points) {
        // Dynamic programming (2D) - O(m*n) time and space
        if (points.empty()) return 0;
        int m = points.size(), n = points[0].size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
        return dp[m][n];
    }
};
