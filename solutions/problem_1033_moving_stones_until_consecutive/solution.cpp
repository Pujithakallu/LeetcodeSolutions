/*
 * Problem 1033: Moving Stones Until Consecutive
 * ===========================================
 * Difficulty: Medium
 * Tags: Math, Brainteaser
 * Pattern: Math
 *
 * Time Complexity:  O(n) or O(sqrt(n))
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> numMovesStones(int a, int b, int c) {
        // Mathematical approach
        long long result = 0;
        int x = a;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
