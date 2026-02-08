/*
 * Problem 1577: Number of Ways Where Square of Number Is Equal to Product of Two Numbers
 * ====================================================================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Math, Two Pointers
 * Pattern: Two Pointers
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int numTriplets(vector<int>& nums1, vector<int>& nums2) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = nums1.size() - 1;
        while (left < right) {
            int curr = nums1[left] + nums1[right];
            if (curr == nums2) {
                return {left, right};
            } else if (curr < nums2) {
                left++;
            } else {
                right--;
            }
        }
        return 0;
    }
};
