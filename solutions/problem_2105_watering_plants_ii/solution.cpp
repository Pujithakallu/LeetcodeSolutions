/*
 * Problem 2105: Watering Plants II
 * ==============================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, Simulation
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
    int minimumRefill(vector<int>& plants, int capacityA, int capacityB) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = plants.size() - 1;
        while (left < right) {
            int curr = plants[left] + plants[right];
            if (curr == capacityA) {
                return {left, right};
            } else if (curr < capacityA) {
                left++;
            } else {
                right--;
            }
        }
        return 0;
    }
};
