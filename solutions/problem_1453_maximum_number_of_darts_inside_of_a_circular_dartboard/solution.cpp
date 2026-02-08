/*
 * Problem 1453: Maximum Number of Darts Inside of a Circular Dartboard
 * ==================================================================
 * Difficulty: Hard
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
    int numPoints(vector<vector<int>>& darts, int r) {
        // Geometry approach
        double result = 0;
        for (int i = 0; i < (int)darts.size(); i++) {
            for (int j = i + 1; j < (int)darts.size(); j++) {
                double dx = darts[i][0] - darts[j][0];
                double dy = darts[i][1] - darts[j][1];
                result = max(result, sqrt(dx*dx + dy*dy));
            }
        }
        return result;
    }
};
