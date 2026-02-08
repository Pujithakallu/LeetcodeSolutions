/*
 * Problem 925: Long Pressed Name
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
    bool isLongPressedName(string& name, string& typed) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = name.size() - 1;
        while (left < right) {
            int curr = name[left] + name[right];
            if (curr == typed) {
                return {left, right};
            } else if (curr < typed) {
                left++;
            } else {
                right--;
            }
        }
        return false;
    }
};
