/*
 * Problem 1007: Minimum Domino Rotations For Equal Row
 * ==================================================
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
    int minDominoRotations(vector<int>& tops, vector<int>& bottoms) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)tops.size(); i++) {
            curr_max = max(curr_max, tops[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
