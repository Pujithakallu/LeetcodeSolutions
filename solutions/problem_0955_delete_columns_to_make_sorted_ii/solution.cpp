/*
 * Problem 955: Delete Columns to Make Sorted II
 * ============================================
 * Difficulty: Medium
 * Tags: Array, String, Greedy
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
    int minDeletionSize(vector<string>& strs) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)strs.size(); i++) {
            curr_max = max(curr_max, strs[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
