/*
 * Problem 1835: Find XOR Sum of All Pairs Bitwise AND
 * =================================================
 * Difficulty: Hard
 * Tags: Array, Math, Bit Manipulation
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
    int getXORSum(vector<int>& arr1, vector<int>& arr2) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : arr1) {
            result ^= val;
        }
        return result;
    }
};
