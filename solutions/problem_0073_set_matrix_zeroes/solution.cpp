/*
 * Problem 73: Set Matrix Zeroes
 * =============================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Matrix
 * Pattern: Matrix / In-place
 *
 * Time Complexity:  O(m*n)
 * Space Complexity: O(1)
 */

#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < matrix.size(); i++) {
            int complement = matrix - matrix[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[matrix[i]] = i;
        }
        return ;
    }
};
