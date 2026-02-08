/*
 * Problem 749: Contain Virus
 * =========================
 * Difficulty: Hard
 * Tags: Array, Depth-First Search, Breadth-First Search, Matrix, Simulation
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
    int containVirus(vector<vector<int>>& isInfected) {
        // DFS on grid - O(m*n) time
        if (isInfected.empty()) return 0;
        int rows = isInfected.size(), cols = isInfected[0].size();
        int count = 0;
        function<void(int, int)> dfs = [&](int r, int c) {
            if (r < 0 || r >= rows || c < 0 || c >= cols) return;
            if (isInfected[r][c] == '0') return;
            isInfected[r][c] = '0';
            dfs(r+1, c); dfs(r-1, c);
            dfs(r, c+1); dfs(r, c-1);
        };
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (isInfected[r][c] == '1') {
                    dfs(r, c);
                    count++;
                }
            }
        }
        return count;
    }
};
