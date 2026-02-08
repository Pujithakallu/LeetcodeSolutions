/*
 * Problem 7: Reverse Integer
 * ===========================
 * Difficulty: Medium
 * Tags: Math
 * Pattern: Math
 *
 * Time Complexity:  O(log x)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        // Mathematical approach
        long long result = 0;
        int x = x;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
