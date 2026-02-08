/*
 * Problem 1830: Minimum Number of Operations to Make String Sorted
 * ==============================================================
 * Difficulty: Hard
 * Tags: Math, String, Combinatorics
 * Pattern: Combinatorics
 *
 * Time Complexity:  O(n) or O(n^2)
 * Space Complexity: O(n)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int makeStringSorted(string& s) {
        // Combinatorics approach
        const int MOD = 1e9 + 7;
        int n = s;
        vector<long long> dp(n + 1, 1);
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i-1] * i % MOD;
        }
        return dp[n] % MOD;
    }
};
