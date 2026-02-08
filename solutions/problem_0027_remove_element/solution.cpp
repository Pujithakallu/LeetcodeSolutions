/*
 * Problem 27: Remove Element
 * ==========================
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
    int removeElement(vector<int>& nums, int val) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int curr = nums[left] + nums[right];
            if (curr == val) {
                return {left, right};
            } else if (curr < val) {
                left++;
            } else {
                right--;
            }
        }
        return 0;
    }
};
