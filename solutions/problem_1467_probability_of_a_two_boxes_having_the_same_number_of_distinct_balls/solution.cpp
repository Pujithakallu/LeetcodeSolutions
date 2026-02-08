/*
 * Problem 1467: Probability of a Two Boxes Having The Same Number of Distinct Balls
 * ===============================================================================
 * Difficulty: Hard
 * Tags: Array, Math, Dynamic Programming, Backtracking, Combinatorics, Probability and Statistics
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
    double getProbability(vector<int>& balls) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)balls.size(); i++) {
                path.push_back(balls[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
