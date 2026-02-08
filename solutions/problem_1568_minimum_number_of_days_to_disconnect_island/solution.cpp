/*
 * Problem 1568: Minimum Number of Days to Disconnect Island
 * =======================================================
 * Difficulty: Hard
 * Tags: Array, Depth-First Search, Breadth-First Search, Matrix, Strongly Connected Component
 * Pattern: DFS on Matrix / Grid
 *
 * Time Complexity:  O(m * n)
 * Space Complexity: O(m * n)
 */

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int minDays(vector<vector<int>>& grid) {
        // DFS on grid - O(m*n) time
        if (grid.empty()) return 0;
        int rows = grid.size(), cols = grid[0].size();
        int count = 0;
        function<void(int, int)> dfs = [&](int r, int c) {
            if (r < 0 || r >= rows || c < 0 || c >= cols) return;
            if (grid[r][c] == '0') return;
            grid[r][c] = '0';
            dfs(r+1, c); dfs(r-1, c);
            dfs(r, c+1); dfs(r, c-1);
        };
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1') {
                    dfs(r, c);
                    count++;
                }
            }
        }
        return count;
    }
};
