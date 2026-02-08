/*
 * Problem 2172: Maximum AND Sum of Array
 * ====================================
 * Difficulty: Hard
 * Tags: Array, Dynamic Programming, Bit Manipulation, Bitmask
 * Pattern: Dynamic Programming (Bitmask)
 *
 * Time Complexity:  O(2^n * n)
 * Space Complexity: O(2^n)
 */

#include <algorithm>
#include <climits>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int maximumANDSum(vector<int>& nums, int numSlots) {
        // Bitmask DP - O(2^n * n) time
        int n = nums.size();
        vector<int> dp(1 << n, INT_MAX);
        dp[0] = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) continue;
                int new_mask = mask | (1 << i);
                dp[new_mask] = min(dp[new_mask], dp[mask] + 1);
            }
        }
        return dp[(1 << n) - 1];
    }
};
