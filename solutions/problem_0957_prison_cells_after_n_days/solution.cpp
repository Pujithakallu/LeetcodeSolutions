/*
 * Problem 957: Prison Cells After N Days
 * =====================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Math, Bit Manipulation
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
    vector<int> prisonAfterNDays(vector<int>& cells, int n) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : cells) {
            result ^= val;
        }
        return result;
    }
};
