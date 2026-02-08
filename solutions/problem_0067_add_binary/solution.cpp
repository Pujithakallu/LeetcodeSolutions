/*
 * Problem 67: Add Binary
 * ======================
 * Difficulty: Easy
 * Tags: Math, String, Bit Manipulation, Simulation
 * Pattern: Math / String
 *
 * Time Complexity:  O(max(m,n))
 * Space Complexity: O(max(m,n))
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string addBinary(string& a, string& b) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : a) {
            result ^= val;
        }
        return result;
    }
};
