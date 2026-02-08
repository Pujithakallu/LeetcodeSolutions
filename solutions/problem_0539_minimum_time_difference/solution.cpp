/*
 * Problem 539: Minimum Time Difference
 * ===================================
 * Difficulty: Medium
 * Tags: Array, Math, String, Sorting
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
    int findMinDifference(vector<string>& timePoints) {
        // Sort-based approach - O(n log n) time
        sort(timePoints.begin(), timePoints.end());
        vector<vector<int>> result;
        result.push_back(timePoints[0]);
        for (int i = 1; i < (int)timePoints.size(); i++) {
            if (timePoints[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], timePoints[i][1]);
            } else {
                result.push_back(timePoints[i]);
            }
        }
        return result;
    }
};
