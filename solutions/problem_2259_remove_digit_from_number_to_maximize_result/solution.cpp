/*
 * Problem 2259: Remove Digit From Number to Maximize Result
 * =======================================================
 * Difficulty: Easy
 * Tags: String, Greedy, Enumeration
 * Pattern: Greedy
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(1)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string removeDigit(string& number, string& digit) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)number.size(); i++) {
            curr_max = max(curr_max, number[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
