/*
 * Problem 168: Excel Sheet Column Title
 * ====================================
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
    string convertToTitle(int columnNumber) {
        // Mathematical approach
        long long result = 0;
        int x = columnNumber;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
