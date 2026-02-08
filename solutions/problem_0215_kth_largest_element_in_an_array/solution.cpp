/*
 * Problem 215: Kth Largest Element in an Array
 * ===========================================
 * Difficulty: Medium
 * Tags: Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect
 * Pattern: Heap / Quickselect
 *
 * Time Complexity:  O(n log k)
 * Space Complexity: O(k)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Quickselect - O(n) average time
        int k = k;
        nth_element(nums.begin(), nums.begin() + nums.size() - k, nums.end());
        return nums[nums.size() - k];
    }
};
