/*
 * Problem 518: Coin Change II
 * ==========================
 * Difficulty: Medium
 * Tags: Array, Dynamic Programming
 * Pattern: Dynamic Programming (Unbounded Knapsack)
 *
 * Time Complexity:  O(n * amount)
 * Space Complexity: O(amount)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int change(int amount, vector<int>& coins) {
        // Dynamic programming (1D) - O(n) time, O(n) space
        int n = amount;
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
