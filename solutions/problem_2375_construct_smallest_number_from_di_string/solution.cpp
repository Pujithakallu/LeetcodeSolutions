/*
 * Problem 2375: Construct Smallest Number From DI String
 * ====================================================
 * Difficulty: Medium
 * Tags: String, Backtracking, Stack, Greedy
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
    string smallestNumber(string& pattern) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)pattern.size(); i++) {
                path.push_back(pattern[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
