/*
 * Problem 2108: Find First Palindromic String in the Array
 * ======================================================
 * Difficulty: Easy
 * Tags: Array, Two Pointers, String
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
    string firstPalindrome(vector<string>& words) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = words.size() - 1;
        while (left < right) {
            int curr = words[left] + words[right];
            if (curr == words) {
                return {left, right};
            } else if (curr < words) {
                left++;
            } else {
                right--;
            }
        }
        return "";
    }
};
