/*
 * Problem 593: Valid Square
 * ========================
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
    bool validSquare(vector<int>& p1, vector<int>& p2, vector<int>& p3, vector<int>& p4) {
        // Geometry approach
        double result = 0;
        for (int i = 0; i < (int)p1.size(); i++) {
            for (int j = i + 1; j < (int)p1.size(); j++) {
                double dx = p1[i][0] - p1[j][0];
                double dy = p1[i][1] - p1[j][1];
                result = max(result, sqrt(dx*dx + dy*dy));
            }
        }
        return result;
    }
};
