/*
 * Problem 476: Number Complement
 * =============================
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
    int findComplement(int num) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : num) {
            result ^= val;
        }
        return result;
    }
};
