/*
 * Problem 2244: Minimum Rounds to Complete All Tasks
 * ================================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Greedy, Counting
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
    int minimumRounds(vector<int>& tasks) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)tasks.size(); i++) {
            curr_max = max(curr_max, tasks[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
