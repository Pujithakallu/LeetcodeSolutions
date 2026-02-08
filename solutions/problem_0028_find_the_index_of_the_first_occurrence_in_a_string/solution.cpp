/*
 * Problem 28: Find the Index of the First Occurrence in a String
 * ==============================================================
 * Difficulty: Easy
 * Tags: Two Pointers, String, String Matching
 * Pattern: String Matching
 *
 * Time Complexity:  O(m*n)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int strStr(string& haystack, string& needle) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = haystack.size() - 1;
        while (left < right) {
            int curr = haystack[left] + haystack[right];
            if (curr == needle) {
                return {left, right};
            } else if (curr < needle) {
                left++;
            } else {
                right--;
            }
        }
        return 0;
    }
};
