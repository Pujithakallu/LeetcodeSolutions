/*
 * Problem 861: Score After Flipping Matrix
 * =======================================
 * Difficulty: Medium
 * Tags: Array, Greedy, Bit Manipulation, Matrix
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
    int matrixScore(vector<vector<int>>& grid) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)grid.size(); i++) {
            curr_max = max(curr_max, grid[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
