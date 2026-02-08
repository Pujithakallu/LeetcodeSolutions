/*
 * Problem 796: Rotate String
 * =========================
 * Difficulty: Easy
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
    bool rotateString(string& s, string& goal) {
        // String matching (KMP) - O(n+m) time
        int n = s.size(), m = goal.size();
        if (m == 0) return 0;
        vector<int> fail(m, 0);
        for (int i = 1, j = 0; i < m; i++) {
            while (j > 0 && goal[i] != goal[j]) j = fail[j-1];
            if (goal[i] == goal[j]) j++;
            fail[i] = j;
        }
        for (int i = 0, j = 0; i < n; i++) {
            while (j > 0 && s[i] != goal[j]) j = fail[j-1];
            if (s[i] == goal[j]) j++;
            if (j == m) return i - m + 1;
        }
        return -1;
    }
};
