/*
 * Problem 2299: Strong Password Checker II
 * ======================================
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
    bool strongPasswordCheckerII(string& password) {
        // String processing approach - O(n) time
        string processed;
        for (char ch : password) {
            if (isalnum(ch)) {
                processed += tolower(ch);
            }
        }
        string rev = processed;
        reverse(rev.begin(), rev.end());
        return processed == rev;
    }
};
