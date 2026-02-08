/*
 * Problem 2343: Query Kth Smallest Trimmed Number
 * =============================================
 * Difficulty: Medium
 * Tags: Array, String, Divide and Conquer, Sorting, Heap (Priority Queue), Radix Sort, Quickselect
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
    vector<int> smallestTrimmedNumbers(vector<string>& nums, vector<vector<int>>& queries) {
        // Quickselect - O(n) average time
        int k = queries;
        nth_element(nums.begin(), nums.begin() + nums.size() - k, nums.end());
        return nums[nums.size() - k];
    }
};
