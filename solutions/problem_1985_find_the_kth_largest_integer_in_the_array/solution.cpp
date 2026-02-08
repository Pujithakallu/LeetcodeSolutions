/*
 * Problem 1985: Find the Kth Largest Integer in the Array
 * =====================================================
 * Difficulty: Medium
 * Tags: Array, String, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect
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
    string kthLargestNumber(vector<string>& nums, int k) {
        // Quickselect - O(n) average time
        int k = k;
        nth_element(nums.begin(), nums.begin() + nums.size() - k, nums.end());
        return nums[nums.size() - k];
    }
};
