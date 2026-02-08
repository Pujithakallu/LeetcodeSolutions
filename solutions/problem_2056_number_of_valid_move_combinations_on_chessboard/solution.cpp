/*
 * Problem 2056: Number of Valid Move Combinations On Chessboard
 * ===========================================================
 * Difficulty: Hard
 * Tags: Array, String, Backtracking, Simulation
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
    int countCombinations(vector<string>& pieces, vector<vector<int>>& positions) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)pieces.size(); i++) {
                path.push_back(pieces[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
