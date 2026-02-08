/*
 * Problem 2117: Abbreviating the Product of a Range
 * ===============================================
 * Difficulty: Hard
 * Tags: Math, Number Theory
 * Pattern: Number Theory
 *
 * Time Complexity:  O(sqrt(n)) or O(n log log n)
 * Space Complexity: O(n)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string abbreviateProduct(int left, int right) {
        // Number theory approach
        auto gcd_func = [](int a, int b) -> int {
            while (b) { int t = b; b = a % b; a = t; }
            return a;
        };
        int result = left[0];
        for (int i = 1; i < (int)left.size(); i++) {
            result = gcd_func(result, left[i]);
        }
        return result;
    }
};
