/*
 * Problem 2029: Stone Game IX
 * =========================
 * Difficulty: Medium
 * Tags: Array, Math, Greedy, Counting, Game Theory
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
    bool stoneGameIX(vector<int>& stones) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)stones.size(); i++) {
            curr_max = max(curr_max, stones[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
