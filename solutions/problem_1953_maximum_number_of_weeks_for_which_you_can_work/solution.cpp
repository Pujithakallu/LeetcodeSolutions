/*
 * Problem 1953: Maximum Number of Weeks for Which You Can Work
 * ==========================================================
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
    int numberOfWeeks(vector<int>& milestones) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)milestones.size(); i++) {
            curr_max = max(curr_max, milestones[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
