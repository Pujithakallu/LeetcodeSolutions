/*
 * Problem 2200: Find All K-Distant Indices in an Array
 * ==================================================
 * Difficulty: Easy
 * Tags: Array, Two Pointers
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
    vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int curr = nums[left] + nums[right];
            if (curr == key) {
                return {left, right};
            } else if (curr < key) {
                left++;
            } else {
                right--;
            }
        }
        return {};
    }
};
