/*
 * Problem 939: Minimum Area Rectangle
 * ==================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Math, Geometry, Sorting
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
    int minAreaRect(vector<vector<int>>& points) {
        // Sort-based approach - O(n log n) time
        sort(points.begin(), points.end());
        vector<vector<int>> result;
        result.push_back(points[0]);
        for (int i = 1; i < (int)points.size(); i++) {
            if (points[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], points[i][1]);
            } else {
                result.push_back(points[i]);
            }
        }
        return result;
    }
};
