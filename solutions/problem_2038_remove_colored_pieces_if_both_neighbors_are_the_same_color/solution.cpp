/*
 * Problem 2038: Remove Colored Pieces if Both Neighbors are the Same Color
 * ======================================================================
 * Difficulty: Medium
 * Tags: Math, String, Greedy, Game Theory
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
    bool winnerOfGame(string& colors) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)colors.size(); i++) {
            curr_max = max(curr_max, colors[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
