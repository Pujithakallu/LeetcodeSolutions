/*
 * Problem 1616: Split Two Strings to Make Palindrome
 * ================================================
 * Difficulty: Medium
 * Tags: Two Pointers, String
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
    bool checkPalindromeFormation(string& a, string& b) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = a.size() - 1;
        while (left < right) {
            int curr = a[left] + a[right];
            if (curr == b) {
                return {left, right};
            } else if (curr < b) {
                left++;
            } else {
                right--;
            }
        }
        return false;
    }
};
