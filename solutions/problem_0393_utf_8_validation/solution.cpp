/*
 * Problem 393: UTF-8 Validation
 * ============================
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
    bool validUtf8(vector<int>& data) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : data) {
            result ^= val;
        }
        return result;
    }
};
