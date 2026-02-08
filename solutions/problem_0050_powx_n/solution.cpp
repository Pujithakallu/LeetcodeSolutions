/*
 * Problem 50: Pow(x, n)
 * =====================
 * Difficulty: Medium
 * Tags: Math, Recursion
 * Pattern: Math / Binary Exponentiation
 *
 * Time Complexity:  O(log n)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    double myPow(double x, int n) {
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
