/*
 * Problem 416: Partition Equal Subset Sum
 * ======================================
 * Difficulty: Medium
 * Tags: Array, Dynamic Programming
 * Pattern: Dynamic Programming (0/1 Knapsack)
 *
 * Time Complexity:  O(n * sum/2)
 * Space Complexity: O(sum/2)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        // Dynamic programming (1D) - O(n) time, O(n) space
        int n = nums;
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
