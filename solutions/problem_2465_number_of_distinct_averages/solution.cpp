/*
 * Problem 2465: Number of Distinct Averages
 * =======================================
 * Difficulty: Easy
 * Tags: Array, Hash Table, Two Pointers, Sorting
 * Pattern: Two Pointers on Sorted Array
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(1)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int distinctAverages(vector<int>& nums) {
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
        return 0;
    }
};
