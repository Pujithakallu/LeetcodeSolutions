/*
 * Problem 2306: Naming a Company
 * ============================
 * Difficulty: Hard
 * Tags: Array, Hash Table, String, Bit Manipulation, Enumeration
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
    int distinctNames(vector<string>& ideas) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : ideas) {
            result ^= val;
        }
        return result;
    }
};
