/*
 * Problem 436: Find Right Interval
 * ===============================
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
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = intervals.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (intervals[mid] == intervals) {
                return mid;
            } else if (intervals[mid] < intervals) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return {};
    }
};
