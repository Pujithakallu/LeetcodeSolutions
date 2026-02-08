/*
 * Problem 780: Reaching Points
 * ===========================
 * Difficulty: Hard
 * Tags: Math
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
    bool reachingPoints(int sx, int sy, int tx, int ty) {
        // Mathematical approach
        long long result = 0;
        int x = sx;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
