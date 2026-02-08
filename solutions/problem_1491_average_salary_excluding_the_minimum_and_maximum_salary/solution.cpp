/*
 * Problem 1491: Average Salary Excluding the Minimum and Maximum Salary
 * ===================================================================
 * Difficulty: Easy
 * Tags: Array, Sorting
 * Pattern: Sorting
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(n)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    double average(vector<int>& salary) {
        // Sort-based approach - O(n log n) time
        sort(salary.begin(), salary.end());
        vector<vector<int>> result;
        result.push_back(salary[0]);
        for (int i = 1; i < (int)salary.size(); i++) {
            if (salary[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], salary[i][1]);
            } else {
                result.push_back(salary[i]);
            }
        }
        return result;
    }
};
