/*
 * Problem 722: Remove Comments
 * ===========================
 * Difficulty: Medium
 * Tags: Array, String
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
    vector<string> removeComments(vector<string>& source) {
        // String processing approach - O(n) time
        string processed;
        for (char ch : source) {
            if (isalnum(ch)) {
                processed += tolower(ch);
            }
        }
        string rev = processed;
        reverse(rev.begin(), rev.end());
        return processed == rev;
    }
};
