/*
 * Problem 858: Mirror Reflection
 * =============================
 * Difficulty: Medium
 * Tags: Math, Geometry, Number Theory
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
    int mirrorReflection(int p, int q) {
        // Geometry approach
        double result = 0;
        for (int i = 0; i < (int)p.size(); i++) {
            for (int j = i + 1; j < (int)p.size(); j++) {
                double dx = p[i][0] - p[j][0];
                double dy = p[i][1] - p[j][1];
                result = max(result, sqrt(dx*dx + dy*dy));
            }
        }
        return result;
    }
};
