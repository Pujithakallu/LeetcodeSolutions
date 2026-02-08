/*
 * Problem 1947: Maximum Compatibility Score Sum
 * ===========================================
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
    int maxCompatibilitySum(vector<vector<int>>& students, vector<vector<int>>& mentors) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)students.size(); i++) {
                path.push_back(students[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
