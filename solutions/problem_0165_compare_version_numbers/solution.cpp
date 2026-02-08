/*
 * Problem 165: Compare Version Numbers
 * ===================================
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
    int compareVersion(string& version1, string& version2) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = version1.size() - 1;
        while (left < right) {
            int curr = version1[left] + version1[right];
            if (curr == version2) {
                return {left, right};
            } else if (curr < version2) {
                left++;
            } else {
                right--;
            }
        }
        return 0;
    }
};
