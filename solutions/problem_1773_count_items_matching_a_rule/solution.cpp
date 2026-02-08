/*
 * Problem 1773: Count Items Matching a Rule
 * =======================================
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
    int countMatches(vector<vector<string>>& items, string& ruleKey, string& ruleValue) {
        // String processing approach - O(n) time
        string processed;
        for (char ch : items) {
            if (isalnum(ch)) {
                processed += tolower(ch);
            }
        }
        string rev = processed;
        reverse(rev.begin(), rev.end());
        return processed == rev;
    }
};
