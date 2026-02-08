/*
 * Problem 2367: Number of Arithmetic Triplets
 * =========================================
 * Difficulty: Easy
 * Tags: Array, Hash Table, Two Pointers, Enumeration
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
    int arithmeticTriplets(vector<int>& nums, int diff) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int curr = nums[left] + nums[right];
            if (curr == diff) {
                return {left, right};
            } else if (curr < diff) {
                left++;
            } else {
                right--;
            }
        }
        return 0;
    }
};
