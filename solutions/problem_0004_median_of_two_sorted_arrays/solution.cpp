/*
 * Problem 4: Median of Two Sorted Arrays
 * =======================================
 * Difficulty: Hard
 * Tags: Array, Binary Search, Divide and Conquer
 * Pattern: Binary Search
 *
 * Time Complexity:  O(log(min(m,n)))
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = nums1.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums1[mid] == nums2) {
                return mid;
            } else if (nums1[mid] < nums2) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0.0;
    }
};
