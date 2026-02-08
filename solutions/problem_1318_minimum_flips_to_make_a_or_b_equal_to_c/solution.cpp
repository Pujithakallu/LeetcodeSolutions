/*
 * Problem 1318: Minimum Flips to Make a OR b Equal to c
 * ===================================================
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
    int minFlips(int a, int b, int c) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : a) {
            result ^= val;
        }
        return result;
    }
};
