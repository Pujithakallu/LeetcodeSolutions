/*
 * Problem 686: Repeated String Match
 * =================================
 * Difficulty: Medium
 * Tags: String, String Matching
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
    int repeatedStringMatch(string& a, string& b) {
        // String matching (KMP) - O(n+m) time
        int n = a.size(), m = b.size();
        if (m == 0) return 0;
        vector<int> fail(m, 0);
        for (int i = 1, j = 0; i < m; i++) {
            while (j > 0 && b[i] != b[j]) j = fail[j-1];
            if (b[i] == b[j]) j++;
            fail[i] = j;
        }
        for (int i = 0, j = 0; i < n; i++) {
            while (j > 0 && a[i] != b[j]) j = fail[j-1];
            if (a[i] == b[j]) j++;
            if (j == m) return i - m + 1;
        }
        return -1;
    }
};
