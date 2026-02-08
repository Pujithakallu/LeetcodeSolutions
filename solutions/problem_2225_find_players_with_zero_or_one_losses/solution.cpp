/*
 * Problem 2225: Find Players With Zero or One Losses
 * ================================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Sorting, Counting
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
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        // Sort-based approach - O(n log n) time
        sort(matches.begin(), matches.end());
        vector<vector<int>> result;
        result.push_back(matches[0]);
        for (int i = 1; i < (int)matches.size(); i++) {
            if (matches[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], matches[i][1]);
            } else {
                result.push_back(matches[i]);
            }
        }
        return result;
    }
};
