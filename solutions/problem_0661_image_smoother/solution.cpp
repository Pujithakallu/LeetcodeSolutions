/*
 * Problem 661: Image Smoother
 * ==========================
 * Difficulty: Easy
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
    vector<vector<int>> imageSmoother(vector<vector<int>>& img) {
        // Matrix manipulation - O(m*n) time
        if (img.empty()) return {};
        int m = img.size(), n = img[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // Process matrix[i][j]
            }
        }
        return {};
    }
};
