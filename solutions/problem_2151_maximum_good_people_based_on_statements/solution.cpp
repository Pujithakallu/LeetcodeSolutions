/*
 * Problem 2151: Maximum Good People Based on Statements
 * ===================================================
 * Difficulty: Hard
 * Tags: Array, Backtracking, Bit Manipulation, Enumeration
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
    int maximumGood(vector<vector<int>>& statements) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)statements.size(); i++) {
                path.push_back(statements[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
