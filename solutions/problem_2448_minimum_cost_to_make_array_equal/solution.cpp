/*
 * Problem 2448: Minimum Cost to Make Array Equal
 * ============================================
 * Difficulty: Hard
 * Tags: Array, Binary Search, Greedy, Sorting, Prefix Sum
 * Pattern: Binary Search
 *
 * Time Complexity:  O(log n)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int minCost(vector<int>& nums, vector<int>& cost) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = nums.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == cost) {
                return mid;
            } else if (nums[mid] < cost) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
