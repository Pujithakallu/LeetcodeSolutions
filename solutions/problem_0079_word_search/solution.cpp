/*
 * Problem 79: Word Search
 * =======================
 * Difficulty: Medium
 * Tags: Array, String, Backtracking, Depth-First Search, Matrix
 * Pattern: Backtracking / DFS
 *
 * Time Complexity:  O(m*n*4^L)
 * Space Complexity: O(L)
 */

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool exist(vector<vector<string>>& board, string& word) {
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
