/*
 * Problem 2481: Minimum Cuts to Divide a Circle
 * ===========================================
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
    int numberOfCuts(int n) {
        // Geometry approach
        double result = 0;
        for (int i = 0; i < (int)n.size(); i++) {
            for (int j = i + 1; j < (int)n.size(); j++) {
                double dx = n[i][0] - n[j][0];
                double dy = n[i][1] - n[j][1];
                result = max(result, sqrt(dx*dx + dy*dy));
            }
        }
        return result;
    }
};
