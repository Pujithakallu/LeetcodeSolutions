/*
 * Problem 77: Combinations
 * ========================
 * Difficulty: Medium
 * Tags: Backtracking
 * Pattern: Backtracking
 *
 * Time Complexity:  O(C(n,k))
 * Space Complexity: O(k)
 */

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
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
