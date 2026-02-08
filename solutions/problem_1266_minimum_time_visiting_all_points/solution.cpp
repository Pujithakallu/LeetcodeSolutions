/*
 * Problem 1266: Minimum Time Visiting All Points
 * ============================================
 * Difficulty: Easy
 * Tags: Array, Math, Geometry
 * Pattern: Geometry
 *
 * Time Complexity:  O(n^2) or O(n log n)
 * Space Complexity: O(n)
 */

#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        // Geometry approach
        double result = 0;
        for (int i = 0; i < (int)points.size(); i++) {
            for (int j = i + 1; j < (int)points.size(); j++) {
                double dx = points[i][0] - points[j][0];
                double dy = points[i][1] - points[j][1];
                result = max(result, sqrt(dx*dx + dy*dy));
            }
        }
        return result;
    }
};
