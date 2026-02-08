/*
 * Problem 1986: Minimum Number of Work Sessions to Finish the Tasks
 * ===============================================================
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
    int minSessions(vector<int>& tasks, int sessionTime) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)tasks.size(); i++) {
                path.push_back(tasks[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
