/*
 * Problem 1096: Brace Expansion II
 * ==============================
 * Difficulty: Hard
 * Tags: Hash Table, String, Backtracking, Stack, Breadth-First Search, Sorting
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
    vector<string> braceExpansionII(string& expression) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)expression.size(); i++) {
                path.push_back(expression[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
