/*
 * Problem 1419: Minimum Number of Frogs Croaking
 * ============================================
 * Difficulty: Medium
 * Tags: String, Counting
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
    int minNumberOfFrogs(string& croakOfFrogs) {
        // String processing approach - O(n) time
        string processed;
        for (char ch : croakOfFrogs) {
            if (isalnum(ch)) {
                processed += tolower(ch);
            }
        }
        string rev = processed;
        reverse(rev.begin(), rev.end());
        return processed == rev;
    }
};
