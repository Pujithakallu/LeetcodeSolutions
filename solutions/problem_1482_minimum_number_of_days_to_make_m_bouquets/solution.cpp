/*
 * Problem 1482: Minimum Number of Days to Make m Bouquets
 * =====================================================
 * Difficulty: Medium
 * Tags: Array, Binary Search
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
    int minDays(vector<int>& bloomDay, int m, int k) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = bloomDay.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (bloomDay[mid] == m) {
                return mid;
            } else if (bloomDay[mid] < m) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
