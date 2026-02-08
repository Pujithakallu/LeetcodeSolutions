/*
 * Problem 1812: Determine Color of a Chessboard Square
 * ==================================================
 * Difficulty: Easy
 * Tags: Math, String
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
    bool squareIsWhite(string& coordinates) {
        // Mathematical approach
        long long result = 0;
        int x = coordinates;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
