/*
 * Problem 75: Sort Colors
 * =======================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, Sorting
 * Pattern: Dutch National Flag / Three Pointers
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(1)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        // Sort + two pointers - O(n log n) time
        sort(nums.begin(), nums.end());
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int curr = nums[left] + nums[right];
            if (curr < nums) {
                left++;
            } else {
                right--;
            }
        }
        return ;
    }
};
