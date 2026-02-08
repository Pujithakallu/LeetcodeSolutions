/*
 * Problem 844: Backspace String Compare
 * ====================================
 * Difficulty: Easy
 * Tags: Two Pointers, String, Stack, Simulation
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
    bool backspaceCompare(string& s, string& t) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = s.size() - 1;
        while (left < right) {
            int curr = s[left] + s[right];
            if (curr == t) {
                return {left, right};
            } else if (curr < t) {
                left++;
            } else {
                right--;
            }
        }
        return false;
    }
};
