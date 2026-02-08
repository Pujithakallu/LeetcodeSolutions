/*
 * Problem 521: Longest Uncommon Subsequence I
 * ==========================================
 * Difficulty: Easy
 * Tags: String
 * Pattern: String Processing
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n)
 */

#include <algorithm>
#include <cctype>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int findLUSlength(string& a, string& b) {
        // String processing approach - O(n) time
        string processed;
        for (char ch : a) {
            if (isalnum(ch)) {
                processed += tolower(ch);
            }
        }
        string rev = processed;
        reverse(rev.begin(), rev.end());
        return processed == rev;
    }
};
