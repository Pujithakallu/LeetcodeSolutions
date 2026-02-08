/*
 * Problem 2274: Maximum Consecutive Floors Without Special Floors
 * =============================================================
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
    int maxConsecutive(int bottom, int top, vector<int>& special) {
        // Sort-based approach - O(n log n) time
        sort(bottom.begin(), bottom.end());
        vector<vector<int>> result;
        result.push_back(bottom[0]);
        for (int i = 1; i < (int)bottom.size(); i++) {
            if (bottom[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], bottom[i][1]);
            } else {
                result.push_back(bottom[i]);
            }
        }
        return result;
    }
};
