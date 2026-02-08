/*
 * Problem 587: Erect the Fence
 * ===========================
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
    vector<vector<int>> outerTrees(vector<vector<int>>& trees) {
        // Geometry approach
        double result = 0;
        for (int i = 0; i < (int)trees.size(); i++) {
            for (int j = i + 1; j < (int)trees.size(); j++) {
                double dx = trees[i][0] - trees[j][0];
                double dy = trees[i][1] - trees[j][1];
                result = max(result, sqrt(dx*dx + dy*dy));
            }
        }
        return result;
    }
};
