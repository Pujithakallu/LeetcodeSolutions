/*
 * Problem 37: Sudoku Solver
 * =========================
 * Difficulty: Hard
 * Tags: Array, Hash Table, Backtracking, Matrix
 * Pattern: Backtracking
 *
 * Time Complexity:  O(9^(empty cells))
 * Space Complexity: O(81)
 */

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    void solveSudoku(vector<vector<string>>& board) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)board.size(); i++) {
                path.push_back(board[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
