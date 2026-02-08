/*
 * Problem 66: Plus One
 * ====================
 * Difficulty: Easy
 * Tags: Array, Math
 * Pattern: Math / Array
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        // Mathematical approach
        long long result = 0;
        int x = digits;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
