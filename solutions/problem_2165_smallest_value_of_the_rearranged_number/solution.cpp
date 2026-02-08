/*
 * Problem 2165: Smallest Value of the Rearranged Number
 * ===================================================
 * Difficulty: Medium
 * Tags: Math, Sorting
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
    int smallestNumber(int num) {
        // Sort-based approach - O(n log n) time
        sort(num.begin(), num.end());
        vector<vector<int>> result;
        result.push_back(num[0]);
        for (int i = 1; i < (int)num.size(); i++) {
            if (num[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], num[i][1]);
            } else {
                result.push_back(num[i]);
            }
        }
        return result;
    }
};
