/*
 * Problem 1089: Duplicate Zeros
 * ===========================
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
    void duplicateZeros(vector<int>& arr) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = arr.size() - 1;
        while (left < right) {
            int curr = arr[left] + arr[right];
            if (curr == arr) {
                return {left, right};
            } else if (curr < arr) {
                left++;
            } else {
                right--;
            }
        }
        return ;
    }
};
