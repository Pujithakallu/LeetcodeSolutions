/*
 * Problem 2437: Number of Valid Clock Times
 * =======================================
 * Difficulty: Easy
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
    int countTime(string& time) {
        // String processing approach - O(n) time
        string processed;
        for (char ch : time) {
            if (isalnum(ch)) {
                processed += tolower(ch);
            }
        }
        string rev = processed;
        reverse(rev.begin(), rev.end());
        return processed == rev;
    }
};
