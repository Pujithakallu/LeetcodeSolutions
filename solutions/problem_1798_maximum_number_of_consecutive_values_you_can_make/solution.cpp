/*
 * Problem 1798: Maximum Number of Consecutive Values You Can Make
 * =============================================================
 * Difficulty: Medium
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
    int getMaximumConsecutive(vector<int>& coins) {
        // Sort + greedy - O(n log n) time
        sort(coins.begin(), coins.end());
        int result = 0, curr_end = 0;
        for (auto& item : coins) {
            result++;
        }
        return result;
    }
};
