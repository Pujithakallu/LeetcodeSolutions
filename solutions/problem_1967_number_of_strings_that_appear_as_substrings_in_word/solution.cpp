/*
 * Problem 1967: Number of Strings That Appear as Substrings in Word
 * ===============================================================
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
    int numOfStrings(vector<string>& patterns, string& word) {
        // String processing approach - O(n) time
        string processed;
        for (char ch : patterns) {
            if (isalnum(ch)) {
                processed += tolower(ch);
            }
        }
        string rev = processed;
        reverse(rev.begin(), rev.end());
        return processed == rev;
    }
};
