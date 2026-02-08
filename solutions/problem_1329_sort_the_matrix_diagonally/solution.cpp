/*
 * Problem 1329: Sort the Matrix Diagonally
 * ======================================
 * Difficulty: Medium
 * Tags: Array, Sorting, Matrix
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
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        // Sort-based approach - O(n log n) time
        sort(mat.begin(), mat.end());
        vector<vector<int>> result;
        result.push_back(mat[0]);
        for (int i = 1; i < (int)mat.size(); i++) {
            if (mat[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], mat[i][1]);
            } else {
                result.push_back(mat[i]);
            }
        }
        return result;
    }
};
