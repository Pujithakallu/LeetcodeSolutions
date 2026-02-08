/*
 * Problem 38: Count and Say
 * =========================
 * Difficulty: Medium
 * Tags: String
 * Pattern: String Simulation
 *
 * Time Complexity:  O(2^n) worst case
 * Space Complexity: O(2^n)
 */

#include <algorithm>
#include <cctype>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string countAndSay(int n) {
        // String processing approach - O(n) time
        string processed;
        for (char ch : n) {
            if (isalnum(ch)) {
                processed += tolower(ch);
            }
        }
        string rev = processed;
        reverse(rev.begin(), rev.end());
        return processed == rev;
    }
};
