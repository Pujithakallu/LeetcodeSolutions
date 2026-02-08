/*
 * Problem 1253: Reconstruct a 2-Row Binary Matrix
 * =============================================
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
    vector<vector<int>> reconstructMatrix(int upper, int lower, vector<int>& colsum) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)upper.size(); i++) {
            curr_max = max(curr_max, upper[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
