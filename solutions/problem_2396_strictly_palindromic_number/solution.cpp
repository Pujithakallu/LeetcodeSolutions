/*
 * Problem 2396: Strictly Palindromic Number
 * =======================================
 * Difficulty: Medium
 * Tags: Math, Two Pointers, Brainteaser
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
    bool isStrictlyPalindromic(int n) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = n.size() - 1;
        while (left < right) {
            int curr = n[left] + n[right];
            if (curr == n) {
                return {left, right};
            } else if (curr < n) {
                left++;
            } else {
                right--;
            }
        }
        return false;
    }
};
