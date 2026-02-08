/*
 * Problem 1397: Find All Good Strings
 * =================================
 * Difficulty: Hard
 * Tags: String, Dynamic Programming, String Matching
 * Pattern: Dynamic Programming (String)
 *
 * Time Complexity:  O(m * n)
 * Space Complexity: O(m * n)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int findGoodStrings(int n, string& s1, string& s2, string& evil) {
        // String DP - O(m*n) time and space
        int m = n.size(), n = s1.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (n[i-1] == s1[j-1])
                    dp[i][j] = dp[i-1][j-1] + 1;
                else
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
        return dp[m][n];
    }
};
