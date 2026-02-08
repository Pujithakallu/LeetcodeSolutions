/*
 * Problem 8: String to Integer (atoi)
 * ====================================
 * Difficulty: Medium
 * Tags: String
 * Pattern: String Parsing
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(1)
 */

#include <algorithm>
#include <cctype>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int myAtoi(string& s) {
        // String processing approach - O(n) time
        string processed;
        for (char ch : s) {
            if (isalnum(ch)) {
                processed += tolower(ch);
            }
        }
        string rev = processed;
        reverse(rev.begin(), rev.end());
        return processed == rev;
    }
};
