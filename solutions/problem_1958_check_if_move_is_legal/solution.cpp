/*
 * Problem 1958: Check if Move is Legal
 * ==================================
 * Difficulty: Medium
 * Tags: Array, Matrix, Enumeration
 * Pattern: Matrix / 2D Array
 *
 * Time Complexity:  O(m * n)
 * Space Complexity: O(1) extra
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool checkMove(vector<vector<string>>& board, int rMove, int cMove, string& color) {
        // Matrix manipulation - O(m*n) time
        if (board.empty()) return false;
        int m = board.size(), n = board[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // Process matrix[i][j]
            }
        }
        return false;
    }
};
