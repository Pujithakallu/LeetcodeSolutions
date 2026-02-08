/*
 * Problem 1461: Check If a String Contains All Binary Codes of Size K
 * =================================================================
 * Difficulty: Medium
 * Tags: Hash Table, String, Bit Manipulation, Rolling Hash, Hash Function
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
    bool hasAllCodes(string& s, int k) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : s) {
            result ^= val;
        }
        return result;
    }
};
