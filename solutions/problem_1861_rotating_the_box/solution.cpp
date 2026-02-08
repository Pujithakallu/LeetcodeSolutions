/*
 * Problem 1861: Rotating the Box
 * ============================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, Matrix
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
    vector<vector<string>> rotateTheBox(vector<vector<string>>& boxGrid) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = boxGrid.size() - 1;
        while (left < right) {
            int curr = boxGrid[left] + boxGrid[right];
            if (curr == boxGrid) {
                return {left, right};
            } else if (curr < boxGrid) {
                left++;
            } else {
                right--;
            }
        }
        return {};
    }
};
