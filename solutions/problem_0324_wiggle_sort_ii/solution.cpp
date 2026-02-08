/*
 * Problem 324: Wiggle Sort II
 * ==========================
 * Difficulty: Medium
 * Tags: Array, Divide and Conquer, Greedy, Sorting, Quickselect
 * Pattern: Quickselect
 *
 * Time Complexity:  O(n) average
 * Space Complexity: O(1)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        // Quickselect - O(n) average time
        int k = nums;
        nth_element(nums.begin(), nums.begin() + nums.size() - k, nums.end());
        return nums[nums.size() - k];
    }
};
