/*
 * Problem 1961: Check If String Is a Prefix of Array
 * ================================================
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
    bool isPrefixString(string& s, vector<string>& words) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = s.size() - 1;
        while (left < right) {
            int curr = s[left] + s[right];
            if (curr == words) {
                return {left, right};
            } else if (curr < words) {
                left++;
            } else {
                right--;
            }
        }
        return false;
    }
};
