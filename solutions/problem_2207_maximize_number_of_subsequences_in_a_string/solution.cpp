/*
 * Problem 2207: Maximize Number of Subsequences in a String
 * =======================================================
 * Difficulty: Medium
 * Tags: String, Greedy, Prefix Sum
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
    int maximumSubsequenceCount(string& text, string& pattern) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)text.size(); i++) {
            curr_max = max(curr_max, text[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
