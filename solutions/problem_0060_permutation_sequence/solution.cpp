/*
 * Problem 60: Permutation Sequence
 * ================================
 * Difficulty: Hard
 * Tags: Math, Recursion
 * Pattern: Math
 *
 * Time Complexity:  O(n^2)
 * Space Complexity: O(n)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string getPermutation(int n, int k) {
        // Mathematical approach
        long long result = 0;
        int x = n;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
