/*
 * Problem 2280: Minimum Lines to Represent a Line Chart
 * ===================================================
 * Difficulty: Medium
 * Tags: Array, Math, Geometry, Sorting, Number Theory
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
    int minimumLines(vector<vector<int>>& stockPrices) {
        // Sort-based approach - O(n log n) time
        sort(stockPrices.begin(), stockPrices.end());
        vector<vector<int>> result;
        result.push_back(stockPrices[0]);
        for (int i = 1; i < (int)stockPrices.size(); i++) {
            if (stockPrices[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], stockPrices[i][1]);
            } else {
                result.push_back(stockPrices[i]);
            }
        }
        return result;
    }
};
