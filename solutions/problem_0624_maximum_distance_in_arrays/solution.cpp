/*
 * Problem 624: Maximum Distance in Arrays
 * ======================================
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
    int maxDistance(vector<vector<int>>& arrays) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)arrays.size(); i++) {
            curr_max = max(curr_max, arrays[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
