/*
 * Problem 1901: Find a Peak Element II
 * ==================================
 * Difficulty: Medium
 * Tags: Array, Binary Search, Matrix
 * Pattern: Binary Search
 *
 * Time Complexity:  O(log n)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> findPeakGrid(vector<vector<int>>& mat) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = mat.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (mat[mid] == mat) {
                return mid;
            } else if (mat[mid] < mat) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return {};
    }
};
