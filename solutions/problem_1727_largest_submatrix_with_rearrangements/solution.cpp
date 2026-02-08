/*
 * Problem 1727: Largest Submatrix With Rearrangements
 * =================================================
 * Difficulty: Medium
 * Tags: Array, Greedy, Sorting, Matrix
 * Pattern: Greedy with Sorting
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
    int largestSubmatrix(vector<vector<int>>& matrix) {
        // Sort + greedy - O(n log n) time
        sort(matrix.begin(), matrix.end());
        int result = 0, curr_end = 0;
        for (auto& item : matrix) {
            result++;
        }
        return result;
    }
};
