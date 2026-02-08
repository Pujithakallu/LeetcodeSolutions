/*
 * Problem 2446: Determine if Two Events Have Conflict
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
    bool haveConflict(vector<string>& event1, vector<string>& event2) {
        // String processing approach - O(n) time
        string processed;
        for (char ch : event1) {
            if (isalnum(ch)) {
                processed += tolower(ch);
            }
        }
        string rev = processed;
        reverse(rev.begin(), rev.end());
        return processed == rev;
    }
};
