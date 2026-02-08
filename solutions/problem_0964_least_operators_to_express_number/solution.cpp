/*
 * Problem 964: Least Operators to Express Number
 * =============================================
 * Difficulty: Hard
 * Tags: Math, Dynamic Programming, Memoization
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
    int leastOpsExpressTarget(int x, int target) {
        // Dynamic programming (1D) - O(n) time, O(n) space
        int n = x;
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
