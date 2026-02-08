/*
 * Problem 435: Non-overlapping Intervals
 * =====================================
 * Difficulty: Medium
 * Tags: Array, Dynamic Programming, Greedy, Sorting
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
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        // Dynamic programming (1D) - O(n) time, O(n) space
        int n = intervals;
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
