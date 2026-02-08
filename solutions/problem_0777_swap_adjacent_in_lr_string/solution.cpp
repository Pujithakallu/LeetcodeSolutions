/*
 * Problem 777: Swap Adjacent in LR String
 * ======================================
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
    bool canTransform(string& start, string& result) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = start.size() - 1;
        while (left < right) {
            int curr = start[left] + start[right];
            if (curr == result) {
                return {left, right};
            } else if (curr < result) {
                left++;
            } else {
                right--;
            }
        }
        return false;
    }
};
