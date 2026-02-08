/*
 * Problem 48: Rotate Image
 * ========================
 * Difficulty: Medium
 * Tags: Array, Math, Matrix
 * Pattern: Matrix Manipulation
 *
 * Time Complexity:  O(n^2)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        // Matrix manipulation - O(m*n) time
        if (matrix.empty()) return ;
        int m = matrix.size(), n = matrix[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // Process matrix[i][j]
            }
        }
        return ;
    }
};
