/*
 * Problem 2425: Bitwise XOR of All Pairings
 * =======================================
 * Difficulty: Medium
 * Tags: Array, Bit Manipulation, Brainteaser
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
    int xorAllNums(vector<int>& nums1, vector<int>& nums2) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : nums1) {
            result ^= val;
        }
        return result;
    }
};
