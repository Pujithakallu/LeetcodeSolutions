/*
 * Problem 17: Letter Combinations of a Phone Number
 * =================================================
 * Difficulty: Medium
 * Tags: Hash Table, String, Backtracking
 * Pattern: Backtracking
 *
 * Time Complexity:  O(4^n) where n = len(digits)
 * Space Complexity: O(n)
 */

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string& digits) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)digits.size(); i++) {
                path.push_back(digits[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
