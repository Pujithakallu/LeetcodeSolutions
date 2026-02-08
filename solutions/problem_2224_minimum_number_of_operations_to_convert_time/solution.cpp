/*
 * Problem 2224: Minimum Number of Operations to Convert Time
 * ========================================================
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
    int convertTime(string& current, string& correct) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)current.size(); i++) {
            curr_max = max(curr_max, current[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
