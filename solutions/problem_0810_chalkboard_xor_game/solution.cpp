/*
 * Problem 810: Chalkboard XOR Game
 * ===============================
 * Difficulty: Hard
 * Tags: Array, Math, Bit Manipulation, Brainteaser, Game Theory
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
    bool xorGame(vector<int>& nums) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : nums) {
            result ^= val;
        }
        return result;
    }
};
