/*
 * Problem 2144: Minimum Cost of Buying Candies With Discount
 * ========================================================
 * Difficulty: Easy
 * Tags: Array, Greedy, Sorting
 * Pattern: Greedy with Sorting
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
    int minimumCost(vector<int>& cost) {
        // Sort + greedy - O(n log n) time
        sort(cost.begin(), cost.end());
        int result = 0, curr_end = 0;
        for (auto& item : cost) {
            result++;
        }
        return result;
    }
};
