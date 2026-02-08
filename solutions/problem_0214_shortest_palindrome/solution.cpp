/*
 * Problem 214: Shortest Palindrome
 * ===============================
 * Difficulty: Hard
 * Tags: String, Rolling Hash, String Matching, Hash Function
 * Pattern: String Matching
 *
 * Time Complexity:  O(n + m)
 * Space Complexity: O(m)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string shortestPalindrome(string& s) {
        // String matching (KMP) - O(n+m) time
        int n = s.size(), m = s.size();
        if (m == 0) return 0;
        vector<int> fail(m, 0);
        for (int i = 1, j = 0; i < m; i++) {
            while (j > 0 && s[i] != s[j]) j = fail[j-1];
            if (s[i] == s[j]) j++;
            fail[i] = j;
        }
        for (int i = 0, j = 0; i < n; i++) {
            while (j > 0 && s[i] != s[j]) j = fail[j-1];
            if (s[i] == s[j]) j++;
            if (j == m) return i - m + 1;
        }
        return -1;
    }
};
