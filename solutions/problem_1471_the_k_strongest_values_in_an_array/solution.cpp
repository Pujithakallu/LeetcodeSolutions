/*
 * Problem 1471: The k Strongest Values in an Array
 * ==============================================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, Sorting
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
    vector<int> getStrongest(vector<int>& arr, int k) {
        // Sort + two pointers - O(n log n) time
        sort(arr.begin(), arr.end());
        int left = 0, right = arr.size() - 1;
        while (left < right) {
            int curr = arr[left] + arr[right];
            if (curr < k) {
                left++;
            } else {
                right--;
            }
        }
        return {};
    }
};
