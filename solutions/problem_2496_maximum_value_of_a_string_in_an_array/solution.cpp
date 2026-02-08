/*
 * Problem 2496: Maximum Value of a String in an Array
 * =================================================
 * Difficulty: Easy
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
    int maximumValue(vector<string>& strs) {
        // String processing approach - O(n) time
        string processed;
        for (char ch : strs) {
            if (isalnum(ch)) {
                processed += tolower(ch);
            }
        }
        string rev = processed;
        reverse(rev.begin(), rev.end());
        return processed == rev;
    }
};
