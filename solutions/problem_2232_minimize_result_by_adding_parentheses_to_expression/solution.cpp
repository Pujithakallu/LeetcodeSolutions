/*
 * Problem 2232: Minimize Result by Adding Parentheses to Expression
 * ===============================================================
 * Difficulty: Medium
 * Tags: String, Enumeration
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
    string minimizeResult(string& expression) {
        // String processing approach - O(n) time
        string processed;
        for (char ch : expression) {
            if (isalnum(ch)) {
                processed += tolower(ch);
            }
        }
        string rev = processed;
        reverse(rev.begin(), rev.end());
        return processed == rev;
    }
};
