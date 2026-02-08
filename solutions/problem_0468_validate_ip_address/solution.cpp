/*
 * Problem 468: Validate IP Address
 * ===============================
 * Difficulty: Medium
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
    string validIPAddress(string& queryIP) {
        // String processing approach - O(n) time
        string processed;
        for (char ch : queryIP) {
            if (isalnum(ch)) {
                processed += tolower(ch);
            }
        }
        string rev = processed;
        reverse(rev.begin(), rev.end());
        return processed == rev;
    }
};
