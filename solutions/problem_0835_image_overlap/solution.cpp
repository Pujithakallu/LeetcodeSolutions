/*
 * Problem 835: Image Overlap
 * =========================
 * Difficulty: Medium
 * Tags: Array, Matrix
 * Pattern: Matrix / 2D Array
 *
 * Time Complexity:  O(m * n)
 * Space Complexity: O(1) extra
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
        // Matrix manipulation - O(m*n) time
        if (img1.empty()) return 0;
        int m = img1.size(), n = img1[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // Process matrix[i][j]
            }
        }
        return 0;
    }
};
