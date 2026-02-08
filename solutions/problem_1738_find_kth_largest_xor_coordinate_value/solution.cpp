/*
 * Problem 1738: Find Kth Largest XOR Coordinate Value
 * =================================================
 * Difficulty: Medium
 * Tags: Array, Divide and Conquer, Bit Manipulation, Sorting, Heap (Priority Queue), Matrix, Prefix Sum, Quickselect
 * Pattern: Quickselect
 *
 * Time Complexity:  O(n) average
 * Space Complexity: O(1)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int kthLargestValue(vector<vector<int>>& matrix, int k) {
        // Quickselect - O(n) average time
        int k = k;
        nth_element(matrix.begin(), matrix.begin() + matrix.size() - k, matrix.end());
        return matrix[matrix.size() - k];
    }
};
