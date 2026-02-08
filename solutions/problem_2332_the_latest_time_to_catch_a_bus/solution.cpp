/*
 * Problem 2332: The Latest Time to Catch a Bus
 * ==========================================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, Binary Search, Sorting
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
    int latestTimeCatchTheBus(vector<int>& buses, vector<int>& passengers, int capacity) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = buses.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (buses[mid] == passengers) {
                return mid;
            } else if (buses[mid] < passengers) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
