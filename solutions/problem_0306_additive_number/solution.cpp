/*
 * Problem 306: Additive Number
 * ===========================
 * Difficulty: Medium
 * Tags: String, Backtracking
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
    bool isAdditiveNumber(string& num) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)num.size(); i++) {
                path.push_back(num[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
