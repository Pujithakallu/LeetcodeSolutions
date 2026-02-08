/*
 * Problem 2337: Move Pieces to Obtain a String
 * ==========================================
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
    bool canChange(string& start, string& target) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = start.size() - 1;
        while (left < right) {
            int curr = start[left] + start[right];
            if (curr == target) {
                return {left, right};
            } else if (curr < target) {
                left++;
            } else {
                right--;
            }
        }
        return false;
    }
};
