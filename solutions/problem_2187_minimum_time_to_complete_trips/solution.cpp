/*
 * Problem 2187: Minimum Time to Complete Trips
 * ==========================================
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
    int minimumTime(vector<int>& time, int totalTrips) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = time.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (time[mid] == totalTrips) {
                return mid;
            } else if (time[mid] < totalTrips) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
