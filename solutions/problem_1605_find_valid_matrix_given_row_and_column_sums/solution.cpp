/*
 * Problem 1605: Find Valid Matrix Given Row and Column Sums
 * =======================================================
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
    vector<vector<int>> restoreMatrix(vector<int>& rowSum, vector<int>& colSum) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)rowSum.size(); i++) {
            curr_max = max(curr_max, rowSum[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
