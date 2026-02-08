/*
 * Problem 795: Number of Subarrays with Bounded Maximum
 * ====================================================
 * Difficulty: Medium
 * Tags: Array, Two Pointers
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
    int numSubarrayBoundedMax(vector<int>& nums, int left, int right) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int curr = nums[left] + nums[right];
            if (curr == left) {
                return {left, right};
            } else if (curr < left) {
                left++;
            } else {
                right--;
            }
        }
        return 0;
    }
};
