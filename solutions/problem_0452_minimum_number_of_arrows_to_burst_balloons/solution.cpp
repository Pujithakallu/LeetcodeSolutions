/*
 * Problem 452: Minimum Number of Arrows to Burst Balloons
 * ======================================================
 * Difficulty: Medium
 * Tags: Array, Greedy, Sorting
 * Pattern: Greedy with Sorting
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
    int findMinArrowShots(vector<vector<int>>& points) {
        // Sort + greedy - O(n log n) time
        sort(points.begin(), points.end());
        int result = 0, curr_end = 0;
        for (auto& item : points) {
            result++;
        }
        return result;
    }
};
