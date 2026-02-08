/*
 * Problem 51: N-Queens
 * ====================
 * Difficulty: Hard
 * Tags: Array, Backtracking
 * Pattern: Backtracking
 *
 * Time Complexity:  O(n!)
 * Space Complexity: O(n^2)
 */

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)n.size(); i++) {
                path.push_back(n[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
