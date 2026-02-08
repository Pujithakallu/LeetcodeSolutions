/*
 * Problem 836: Rectangle Overlap
 * =============================
 * Difficulty: Easy
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
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        // Geometry approach
        double result = 0;
        for (int i = 0; i < (int)rec1.size(); i++) {
            for (int j = i + 1; j < (int)rec1.size(); j++) {
                double dx = rec1[i][0] - rec1[j][0];
                double dy = rec1[i][1] - rec1[j][1];
                result = max(result, sqrt(dx*dx + dy*dy));
            }
        }
        return result;
    }
};
