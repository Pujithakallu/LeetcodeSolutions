/*
 * Problem 1401: Circle and Rectangle Overlapping
 * ============================================
 * Difficulty: Medium
 * Tags: Math, Geometry
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
    bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        // Geometry approach
        double result = 0;
        for (int i = 0; i < (int)radius.size(); i++) {
            for (int j = i + 1; j < (int)radius.size(); j++) {
                double dx = radius[i][0] - radius[j][0];
                double dy = radius[i][1] - radius[j][1];
                result = max(result, sqrt(dx*dx + dy*dy));
            }
        }
        return result;
    }
};
