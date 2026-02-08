/*
 * Problem 39: Combination Sum
 * ===========================
 * Difficulty: Medium
 * Tags: Array, Backtracking
 * Pattern: Backtracking
 *
 * Time Complexity:  O(n^(target/min))
 * Space Complexity: O(target/min)
 */

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
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
