/*
 * Problem 2185: Counting Words With a Given Prefix
 * ==============================================
 * Difficulty: Easy
 * Tags: Array, String, String Matching
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
    int prefixCount(vector<string>& words, string& pref) {
        // String matching (KMP) - O(n+m) time
        int n = words.size(), m = pref.size();
        if (m == 0) return 0;
        vector<int> fail(m, 0);
        for (int i = 1, j = 0; i < m; i++) {
            while (j > 0 && pref[i] != pref[j]) j = fail[j-1];
            if (pref[i] == pref[j]) j++;
            fail[i] = j;
        }
        for (int i = 0, j = 0; i < n; i++) {
            while (j > 0 && words[i] != pref[j]) j = fail[j-1];
            if (words[i] == pref[j]) j++;
            if (j == m) return i - m + 1;
        }
        return -1;
    }
};
