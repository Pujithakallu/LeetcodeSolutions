/*
 * Problem 1629: Slowest Key
 * =======================
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
    string slowestKey(vector<int>& releaseTimes, string& keysPressed) {
        // String processing approach - O(n) time
        string processed;
        for (char ch : releaseTimes) {
            if (isalnum(ch)) {
                processed += tolower(ch);
            }
        }
        string rev = processed;
        reverse(rev.begin(), rev.end());
        return processed == rev;
    }
};
