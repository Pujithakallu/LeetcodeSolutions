/*
 * Problem 2161: Partition Array According to Given Pivot
 * ====================================================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, Simulation
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
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int curr = nums[left] + nums[right];
            if (curr == pivot) {
                return {left, right};
            } else if (curr < pivot) {
                left++;
            } else {
                right--;
            }
        }
        return {};
    }
};
