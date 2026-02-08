/*
 * Problem 2397: Maximum Rows Covered by Columns
 * ===========================================
 * Difficulty: Medium
 * Tags: Array, Backtracking, Bit Manipulation, Matrix, Enumeration
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
    int maximumRows(vector<vector<int>>& matrix, int numSelect) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)matrix.size(); i++) {
                path.push_back(matrix[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
