/*
 * Problem 541: Reverse String II
 * =============================
 * Difficulty: Easy
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
    string reverseStr(string& s, int k) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = s.size() - 1;
        while (left < right) {
            int curr = s[left] + s[right];
            if (curr == k) {
                return {left, right};
            } else if (curr < k) {
                left++;
            } else {
                right--;
            }
        }
        return "";
    }
};
