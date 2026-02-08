/*
 * Problem 62: Unique Paths
 * ========================
 * Difficulty: Medium
 * Tags: Math, Dynamic Programming, Combinatorics
 * Pattern: Dynamic Programming
 *
 * Time Complexity:  O(m*n)
 * Space Complexity: O(n)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        // Dynamic programming (1D) - O(n) time, O(n) space
        int n = m;
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
