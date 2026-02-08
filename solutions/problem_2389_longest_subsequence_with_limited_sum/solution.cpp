/*
 * Problem 2389: Longest Subsequence With Limited Sum
 * ================================================
 * Difficulty: Easy
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
    vector<int> answerQueries(vector<int>& nums, vector<int>& queries) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = nums.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == queries) {
                return mid;
            } else if (nums[mid] < queries) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return {};
    }
};
