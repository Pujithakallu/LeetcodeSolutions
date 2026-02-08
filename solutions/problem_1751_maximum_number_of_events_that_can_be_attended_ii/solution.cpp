/*
 * Problem 1751: Maximum Number of Events That Can Be Attended II
 * ============================================================
 * Difficulty: Hard
 * Tags: Array, Binary Search, Dynamic Programming, Sorting
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
    int maxValue(vector<vector<int>>& events, int k) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = events.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (events[mid] == k) {
                return mid;
            } else if (events[mid] < k) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
