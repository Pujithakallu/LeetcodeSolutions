/*
 * Problem 1723: Find Minimum Time to Finish All Jobs
 * ================================================
 * Difficulty: Hard
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
    int minimumTimeRequired(vector<int>& jobs, int k) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)jobs.size(); i++) {
                path.push_back(jobs[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
