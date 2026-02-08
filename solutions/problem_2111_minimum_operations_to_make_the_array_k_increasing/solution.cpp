/*
 * Problem 2111: Minimum Operations to Make the Array K-Increasing
 * =============================================================
 * Difficulty: Hard
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
    int kIncreasing(vector<int>& arr, int k) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = arr.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] == k) {
                return mid;
            } else if (arr[mid] < k) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
