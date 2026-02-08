/*
 * Problem 318: Maximum Product of Word Lengths
 * ===========================================
 * Difficulty: Medium
 * Tags: Array, String, Bit Manipulation
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
    int maxProduct(vector<string>& words) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : words) {
            result ^= val;
        }
        return result;
    }
};
