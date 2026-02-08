/*
 * Problem 300: Longest Increasing Subsequence
 * ==========================================
 * Difficulty: Medium
 * Tags: Array, Binary Search, Dynamic Programming
 * Pattern: Binary Search / DP
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(n)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = nums.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == nums) {
                return mid;
            } else if (nums[mid] < nums) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
