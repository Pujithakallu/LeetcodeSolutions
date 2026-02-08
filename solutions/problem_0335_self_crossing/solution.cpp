/*
 * Problem 335: Self Crossing
 * =========================
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
    bool isSelfCrossing(vector<int>& distance) {
        // Geometry approach
        double result = 0;
        for (int i = 0; i < (int)distance.size(); i++) {
            for (int j = i + 1; j < (int)distance.size(); j++) {
                double dx = distance[i][0] - distance[j][0];
                double dy = distance[i][1] - distance[j][1];
                result = max(result, sqrt(dx*dx + dy*dy));
            }
        }
        return result;
    }
};
