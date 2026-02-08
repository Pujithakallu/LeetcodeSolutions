/*
 * Problem 18: 4Sum
 * ================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, Sorting
 * Pattern: Two Pointers
 *
 * Time Complexity:  O(n^3)
 * Space Complexity: O(1) extra
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        // Sort + two pointers - O(n log n) time
        sort(nums.begin(), nums.end());
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int curr = nums[left] + nums[right];
            if (curr < target) {
                left++;
            } else {
                right--;
            }
        }
        return {};
    }
};
