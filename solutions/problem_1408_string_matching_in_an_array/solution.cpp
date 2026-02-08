/*
 * Problem 1408: String Matching in an Array
 * =======================================
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
    vector<string> stringMatching(vector<string>& words) {
        // String matching (KMP) - O(n+m) time
        int n = words.size(), m = words.size();
        if (m == 0) return 0;
        vector<int> fail(m, 0);
        for (int i = 1, j = 0; i < m; i++) {
            while (j > 0 && words[i] != words[j]) j = fail[j-1];
            if (words[i] == words[j]) j++;
            fail[i] = j;
        }
        for (int i = 0, j = 0; i < n; i++) {
            while (j > 0 && words[i] != words[j]) j = fail[j-1];
            if (words[i] == words[j]) j++;
            if (j == m) return i - m + 1;
        }
        return -1;
    }
};
