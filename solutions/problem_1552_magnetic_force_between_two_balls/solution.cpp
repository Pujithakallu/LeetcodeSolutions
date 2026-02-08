/*
 * Problem 1552: Magnetic Force Between Two Balls
 * ============================================
 * Difficulty: Medium
 * Tags: Array, Binary Search, Sorting
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
    int maxDistance(vector<int>& position, int m) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = position.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (position[mid] == m) {
                return mid;
            } else if (position[mid] < m) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
