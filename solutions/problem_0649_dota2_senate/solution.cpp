/*
 * Problem 649: Dota2 Senate
 * ========================
 * Difficulty: Medium
 * Tags: String, Greedy, Queue
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
    string predictPartyVictory(string& senate) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)senate.size(); i++) {
            curr_max = max(curr_max, senate[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
