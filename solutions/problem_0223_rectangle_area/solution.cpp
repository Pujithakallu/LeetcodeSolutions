/*
 * Problem 223: Rectangle Area
 * ==========================
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
    int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
        // Geometry approach
        double result = 0;
        for (int i = 0; i < (int)ax1.size(); i++) {
            for (int j = i + 1; j < (int)ax1.size(); j++) {
                double dx = ax1[i][0] - ax1[j][0];
                double dy = ax1[i][1] - ax1[j][1];
                result = max(result, sqrt(dx*dx + dy*dy));
            }
        }
        return result;
    }
};
