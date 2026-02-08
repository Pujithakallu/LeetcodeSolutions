/*
 * Problem 2258: Escape the Spreading Fire
 * =====================================
 * Difficulty: Hard
 * Tags: Array, Binary Search, Breadth-First Search, Matrix
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
    int maximumMinutes(vector<vector<int>>& grid) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = grid.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (grid[mid] == grid) {
                return mid;
            } else if (grid[mid] < grid) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
