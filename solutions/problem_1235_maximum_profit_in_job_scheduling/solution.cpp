/*
 * Problem 1235: Maximum Profit in Job Scheduling
 * ============================================
 * Difficulty: Hard
 * Tags: Array, Binary Search, Dynamic Programming, Sorting
 * Pattern: Dynamic Programming + Binary Search
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(n)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = startTime.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (startTime[mid] == endTime) {
                return mid;
            } else if (startTime[mid] < endTime) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
