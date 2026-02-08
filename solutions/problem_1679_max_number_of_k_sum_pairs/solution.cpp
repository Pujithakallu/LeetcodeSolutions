/*
 * Problem 1679: Max Number of K-Sum Pairs
 * =====================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Two Pointers, Sorting
 * Pattern: Hash Map / Two Sum Variant
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        // Sort + two pointers - O(n log n) time
        sort(nums.begin(), nums.end());
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int curr = nums[left] + nums[right];
            if (curr < k) {
                left++;
            } else {
                right--;
            }
        }
        return 0;
    }
};
