/*
 * Problem 2433: Find The Original Array of Prefix Xor
 * =================================================
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
    vector<int> findArray(vector<int>& pref) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : pref) {
            result ^= val;
        }
        return result;
    }
};
