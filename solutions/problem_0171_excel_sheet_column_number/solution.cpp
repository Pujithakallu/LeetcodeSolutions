/*
 * Problem 171: Excel Sheet Column Number
 * =====================================
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
    int titleToNumber(string& columnTitle) {
        // Mathematical approach
        long long result = 0;
        int x = columnTitle;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
