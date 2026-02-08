/*
 * Problem 1870: Minimum Speed to Arrive on Time
 * ===========================================
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
    int minSpeedOnTime(vector<int>& dist, double hour) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = dist.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (dist[mid] == hour) {
                return mid;
            } else if (dist[mid] < hour) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
