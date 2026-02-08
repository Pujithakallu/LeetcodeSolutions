/*
 * Problem 1232: Check If It Is a Straight Line
 * ==========================================
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
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        // Geometry approach
        double result = 0;
        for (int i = 0; i < (int)coordinates.size(); i++) {
            for (int j = i + 1; j < (int)coordinates.size(); j++) {
                double dx = coordinates[i][0] - coordinates[j][0];
                double dy = coordinates[i][1] - coordinates[j][1];
                result = max(result, sqrt(dx*dx + dy*dy));
            }
        }
        return result;
    }
};
