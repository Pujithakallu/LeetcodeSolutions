/*
 * Problem 2033: Minimum Operations to Make a Uni-Value Grid
 * =======================================================
 * Difficulty: Medium
 * Tags: Array, Math, Sorting, Matrix
 * Pattern: Sorting
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(n)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        // Sort-based approach - O(n log n) time
        sort(grid.begin(), grid.end());
        vector<vector<int>> result;
        result.push_back(grid[0]);
        for (int i = 1; i < (int)grid.size(); i++) {
            if (grid[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], grid[i][1]);
            } else {
                result.push_back(grid[i]);
            }
        }
        return result;
    }
};
