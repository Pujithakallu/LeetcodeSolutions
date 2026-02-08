/*
 * Problem 1051: Height Checker
 * ==========================
 * Difficulty: Easy
 * Tags: Array, Sorting, Counting Sort
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
    int heightChecker(vector<int>& heights) {
        // Sort-based approach - O(n log n) time
        sort(heights.begin(), heights.end());
        vector<vector<int>> result;
        result.push_back(heights[0]);
        for (int i = 1; i < (int)heights.size(); i++) {
            if (heights[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], heights[i][1]);
            } else {
                result.push_back(heights[i]);
            }
        }
        return result;
    }
};
