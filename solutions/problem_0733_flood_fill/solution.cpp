/*
 * Problem 733: Flood Fill
 * ======================
 * Difficulty: Easy
 * Tags: Array, Depth-First Search, Breadth-First Search, Matrix
 * Pattern: DFS / Graph
 *
 * Time Complexity:  O(m*n)
 * Space Complexity: O(m*n)
 */

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        // DFS on grid - O(m*n) time
        if (image.empty()) return 0;
        int rows = image.size(), cols = image[0].size();
        int count = 0;
        function<void(int, int)> dfs = [&](int r, int c) {
            if (r < 0 || r >= rows || c < 0 || c >= cols) return;
            if (image[r][c] == '0') return;
            image[r][c] = '0';
            dfs(r+1, c); dfs(r-1, c);
            dfs(r, c+1); dfs(r, c-1);
        };
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (image[r][c] == '1') {
                    dfs(r, c);
                    count++;
                }
            }
        }
        return count;
    }
};
