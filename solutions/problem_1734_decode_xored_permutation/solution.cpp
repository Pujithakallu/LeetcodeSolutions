/*
 * Problem 1734: Decode XORed Permutation
 * ====================================
 * Difficulty: Medium
 * Tags: Array, Bit Manipulation
 * Pattern: Bit Manipulation
 *
 * Time Complexity:  O(n) or O(log n)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> decode(vector<int>& encoded) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : encoded) {
            result ^= val;
        }
        return result;
    }
};
