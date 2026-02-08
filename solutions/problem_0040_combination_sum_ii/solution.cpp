/*
 * Problem 40: Combination Sum II
 * ==============================
 * Difficulty: Medium
 * Tags: Array, Backtracking
 * Pattern: Backtracking
 *
 * Time Complexity:  O(2^n)
 * Space Complexity: O(n)
 */

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)candidates.size(); i++) {
                path.push_back(candidates[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
