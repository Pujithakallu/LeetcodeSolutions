/*
 * Problem 2087: Minimum Cost Homecoming of a Robot in a Grid
 * ========================================================
 * Difficulty: Medium
 * Tags: Array, Greedy
 * Pattern: Greedy
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(1)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int minCost(vector<int>& startPos, vector<int>& homePos, vector<int>& rowCosts, vector<int>& colCosts) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)startPos.size(); i++) {
            curr_max = max(curr_max, startPos[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
