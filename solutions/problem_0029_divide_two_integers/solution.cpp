/*
 * Problem 29: Divide Two Integers
 * ===============================
 * Difficulty: Medium
 * Tags: Math, Bit Manipulation
 * Pattern: Bit Manipulation / Math
 *
 * Time Complexity:  O(log^2 n)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int divide(int dividend, int divisor) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : dividend) {
            result ^= val;
        }
        return result;
    }
};
