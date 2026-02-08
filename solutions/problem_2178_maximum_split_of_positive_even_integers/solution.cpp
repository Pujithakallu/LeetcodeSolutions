/*
 * Problem 2178: Maximum Split of Positive Even Integers
 * ===================================================
 * Difficulty: Medium
 * Tags: Math, Backtracking, Greedy
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
    vector<int> maximumEvenSplit(int finalSum) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)finalSum.size(); i++) {
                path.push_back(finalSum[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
