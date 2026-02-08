/*
 * Problem 1936: Add Minimum Number of Rungs
 * =======================================
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
    int addRungs(vector<int>& rungs, int dist) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)rungs.size(); i++) {
            curr_max = max(curr_max, rungs[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
