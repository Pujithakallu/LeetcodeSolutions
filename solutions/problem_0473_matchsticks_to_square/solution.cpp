/*
 * Problem 473: Matchsticks to Square
 * =================================
 * Difficulty: Medium
 * Tags: Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask
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
    bool makesquare(vector<int>& matchsticks) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)matchsticks.size(); i++) {
                path.push_back(matchsticks[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
