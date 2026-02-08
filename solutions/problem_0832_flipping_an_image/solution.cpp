/*
 * Problem 832: Flipping an Image
 * =============================
 * Difficulty: Easy
 * Tags: Array, Two Pointers, Bit Manipulation, Matrix, Simulation
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
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = image.size() - 1;
        while (left < right) {
            int curr = image[left] + image[right];
            if (curr == image) {
                return {left, right};
            } else if (curr < image) {
                left++;
            } else {
                right--;
            }
        }
        return {};
    }
};
