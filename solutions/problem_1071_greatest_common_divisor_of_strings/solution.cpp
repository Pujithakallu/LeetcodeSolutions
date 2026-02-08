/*
 * Problem 1071: Greatest Common Divisor of Strings
 * ==============================================
 * Difficulty: Easy
 * Tags: Math, String
 * Pattern: Math / String
 *
 * Time Complexity:  O(n+m)
 * Space Complexity: O(n+m)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string gcdOfStrings(string& str1, string& str2) {
        // Mathematical approach
        long long result = 0;
        int x = str1;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
