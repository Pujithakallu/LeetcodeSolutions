/*
 * Problem 923: 3Sum With Multiplicity
 * ==================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Two Pointers, Sorting, Counting
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
    int threeSumMulti(vector<int>& arr, int target) {
        // Sort + two pointers - O(n log n) time
        sort(arr.begin(), arr.end());
        int left = 0, right = arr.size() - 1;
        while (left < right) {
            int curr = arr[left] + arr[right];
            if (curr < target) {
                left++;
            } else {
                right--;
            }
        }
        return 0;
    }
};
