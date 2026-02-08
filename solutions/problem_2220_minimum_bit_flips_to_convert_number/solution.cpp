/*
 * Problem 2220: Minimum Bit Flips to Convert Number
 * ===============================================
 * Difficulty: Easy
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
    int minBitFlips(int start, int goal) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : start) {
            result ^= val;
        }
        return result;
    }
};
