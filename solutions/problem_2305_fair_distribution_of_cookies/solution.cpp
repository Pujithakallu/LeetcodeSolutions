/*
 * Problem 2305: Fair Distribution of Cookies
 * ========================================
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
    int distributeCookies(vector<int>& cookies, int k) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)cookies.size(); i++) {
                path.push_back(cookies[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
