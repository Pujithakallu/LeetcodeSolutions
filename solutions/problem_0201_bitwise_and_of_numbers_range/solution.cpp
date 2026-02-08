/*
 * Problem 201: Bitwise AND of Numbers Range
 * ========================================
 * Difficulty: Medium
 * Tags: Bit Manipulation
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
    int rangeBitwiseAnd(int left, int right) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : left) {
            result ^= val;
        }
        return result;
    }
};
