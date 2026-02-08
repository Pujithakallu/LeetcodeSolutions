/*
 * Problem 1217: Minimum Cost to Move Chips to The Same Position
 * ===========================================================
 * Difficulty: Easy
 * Tags: Array, Math, Greedy
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
    int minCostToMoveChips(vector<int>& position) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)position.size(); i++) {
            curr_max = max(curr_max, position[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
