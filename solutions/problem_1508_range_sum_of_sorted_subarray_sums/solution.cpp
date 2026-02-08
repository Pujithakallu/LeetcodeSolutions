/*
 * Problem 1508: Range Sum of Sorted Subarray Sums
 * =============================================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, Binary Search, Sorting, Prefix Sum
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
    int rangeSum(vector<int>& nums, int n, int left, int right) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = nums.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == n) {
                return mid;
            } else if (nums[mid] < n) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
