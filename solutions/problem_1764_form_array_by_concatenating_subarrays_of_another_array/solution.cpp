/*
 * Problem 1764: Form Array by Concatenating Subarrays of Another Array
 * ==================================================================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, Greedy, String Matching
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
    bool canChoose(vector<vector<int>>& groups, vector<int>& nums) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)groups.size(); i++) {
            curr_max = max(curr_max, groups[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
