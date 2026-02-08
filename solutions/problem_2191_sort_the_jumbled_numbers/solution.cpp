/*
 * Problem 2191: Sort the Jumbled Numbers
 * ====================================
 * Difficulty: Medium
 * Tags: Array, Sorting
 * Pattern: Sorting
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(n)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> sortJumbled(vector<int>& mapping, vector<int>& nums) {
        // Sort-based approach - O(n log n) time
        sort(mapping.begin(), mapping.end());
        vector<vector<int>> result;
        result.push_back(mapping[0]);
        for (int i = 1; i < (int)mapping.size(); i++) {
            if (mapping[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], mapping[i][1]);
            } else {
                result.push_back(mapping[i]);
            }
        }
        return result;
    }
};
