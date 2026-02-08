/*
 * Problem 1356: Sort Integers by The Number of 1 Bits
 * =================================================
 * Difficulty: Easy
 * Tags: Array, Bit Manipulation, Sorting, Counting
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
    vector<int> sortByBits(vector<int>& arr) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : arr) {
            result ^= val;
        }
        return result;
    }
};
