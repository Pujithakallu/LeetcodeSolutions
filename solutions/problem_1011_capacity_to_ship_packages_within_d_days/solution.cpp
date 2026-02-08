/*
 * Problem 1011: Capacity To Ship Packages Within D Days
 * ===================================================
 * Difficulty: Medium
 * Tags: Array, Binary Search
 * Pattern: Binary Search on Answer
 *
 * Time Complexity:  O(n log S)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = weights.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (weights[mid] == days) {
                return mid;
            } else if (weights[mid] < days) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
