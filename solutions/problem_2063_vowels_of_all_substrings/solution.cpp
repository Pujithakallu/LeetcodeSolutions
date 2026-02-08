/*
 * Problem 2063: Vowels of All Substrings
 * ====================================
 * Difficulty: Medium
 * Tags: Math, String, Dynamic Programming, Combinatorics
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
    int countVowels(string& word) {
        // String DP - O(m*n) time and space
        int m = word.size(), n = word.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word[i-1] == word[j-1])
                    dp[i][j] = dp[i-1][j-1] + 1;
                else
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
        return dp[m][n];
    }
};
