/*
 * Problem 1691: Maximum Height by Stacking Cuboids 
 * ===============================================
 * Difficulty: Hard
 * Tags: Array, Dynamic Programming, Sorting
 * Pattern: Dynamic Programming (1D)
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int maxHeight(vector<vector<int>>& cuboids) {
        // Dynamic programming (1D) - O(n) time, O(n) space
        int n = cuboids;
        if (n <= 0) return 0;
        vector<int> dp(n + 1, 0);
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            dp[i] = dp[i-1];
            if (i >= 2) dp[i] += dp[i-2];
        }
        return dp[n];
    }
};
