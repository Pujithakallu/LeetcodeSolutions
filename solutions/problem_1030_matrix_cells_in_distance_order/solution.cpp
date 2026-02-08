/*
 * Problem 1030: Matrix Cells in Distance Order
 * ==========================================
 * Difficulty: Easy
 * Tags: Array, Math, Geometry, Sorting, Matrix
 * Pattern: Sorting
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(n)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
        // Sort-based approach - O(n log n) time
        sort(rows.begin(), rows.end());
        vector<vector<int>> result;
        result.push_back(rows[0]);
        for (int i = 1; i < (int)rows.size(); i++) {
            if (rows[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], rows[i][1]);
            } else {
                result.push_back(rows[i]);
            }
        }
        return result;
    }
};
