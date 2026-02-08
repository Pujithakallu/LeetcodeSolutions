/*
 * Problem 1404: Number of Steps to Reduce a Number in Binary Representation to One
 * ==============================================================================
 * Difficulty: Medium
 * Tags: String, Bit Manipulation, Simulation
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
    int numSteps(string& s) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : s) {
            result ^= val;
        }
        return result;
    }
};
