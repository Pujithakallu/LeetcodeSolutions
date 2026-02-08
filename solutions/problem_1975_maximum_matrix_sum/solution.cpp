/*
 * Problem 1975: Maximum Matrix Sum
 * ==============================
 * Difficulty: Medium
 * Tags: Array, Greedy, Matrix
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
    int maxMatrixSum(vector<vector<int>>& matrix) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)matrix.size(); i++) {
            curr_max = max(curr_max, matrix[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
