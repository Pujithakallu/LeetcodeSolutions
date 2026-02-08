/*
 * Problem 949: Largest Time for Given Digits
 * =========================================
 * Difficulty: Medium
 * Tags: Array, String, Backtracking, Enumeration
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
    string largestTimeFromDigits(vector<int>& arr) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)arr.size(); i++) {
                path.push_back(arr[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
