/*
 * Problem 88: Merge Sorted Array
 * ==============================
 * Difficulty: Easy
 * Tags: Array, Two Pointers, Sorting
 * Pattern: Two Pointers / Merge
 *
 * Time Complexity:  O(m+n)
 * Space Complexity: O(1)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // Sort + two pointers - O(n log n) time
        sort(nums1.begin(), nums1.end());
        int left = 0, right = nums1.size() - 1;
        while (left < right) {
            int curr = nums1[left] + nums1[right];
            if (curr < m) {
                left++;
            } else {
                right--;
            }
        }
        return ;
    }
};
