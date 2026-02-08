/*
 * Problem 1335: Minimum Difficulty of a Job Schedule
 * ================================================
 * Difficulty: Hard
 * Tags: Array, Dynamic Programming
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
    int minDifficulty(vector<int>& jobDifficulty, int d) {
        // Dynamic programming (1D) - O(n) time, O(n) space
        int n = jobDifficulty;
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
