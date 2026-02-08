/*
 * Problem 1694: Reformat Phone Number
 * =================================
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
    string reformatNumber(string& number) {
        // String processing approach - O(n) time
        string processed;
        for (char ch : number) {
            if (isalnum(ch)) {
                processed += tolower(ch);
            }
        }
        string rev = processed;
        reverse(rev.begin(), rev.end());
        return processed == rev;
    }
};
