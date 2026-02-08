/*
 * Problem 2000: Reverse Prefix of Word
 * ==================================
 * Difficulty: Easy
 * Tags: Two Pointers, String, Stack
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
    string reversePrefix(string& word, string& ch) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = word.size() - 1;
        while (left < right) {
            int curr = word[left] + word[right];
            if (curr == ch) {
                return {left, right};
            } else if (curr < ch) {
                left++;
            } else {
                right--;
            }
        }
        return "";
    }
};
