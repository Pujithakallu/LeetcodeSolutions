/*
 * Problem 517: Super Washing Machines
 * ==================================
 * Difficulty: Hard
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
    int findMinMoves(vector<int>& machines) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)machines.size(); i++) {
            curr_max = max(curr_max, machines[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
