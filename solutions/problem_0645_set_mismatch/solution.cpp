/*
 * Problem 645: Set Mismatch
 * ========================
 * Difficulty: Easy
 * Tags: Array, Hash Table, Bit Manipulation, Sorting
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
    vector<int> findErrorNums(vector<int>& nums) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : nums) {
            result ^= val;
        }
        return result;
    }
};
