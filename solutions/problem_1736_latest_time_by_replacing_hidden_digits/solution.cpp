/*
 * Problem 1736: Latest Time by Replacing Hidden Digits
 * ==================================================
 * Difficulty: Easy
 * Tags: String, Greedy
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
    string maximumTime(string& time) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)time.size(); i++) {
            curr_max = max(curr_max, time[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
