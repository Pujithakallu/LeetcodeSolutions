/*
 * Problem 1643: Kth Smallest Instructions
 * =====================================
 * Difficulty: Hard
 * Tags: Array, Math, Dynamic Programming, Combinatorics
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
    string kthSmallestPath(vector<int>& destination, int k) {
        // Dynamic programming (1D) - O(n) time, O(n) space
        int n = destination;
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
