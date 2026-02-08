/*
 * Problem 1219: Path with Maximum Gold
 * ==================================
 * Difficulty: Medium
 * Tags: Array, Backtracking, Matrix
 * Pattern: Backtracking
 *
 * Time Complexity:  O(k^n) or O(n!)
 * Space Complexity: O(n)
 */

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int getMaximumGold(vector<vector<int>>& grid) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)grid.size(); i++) {
                path.push_back(grid[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
