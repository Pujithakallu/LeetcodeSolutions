/*
 * Problem 2427: Number of Common Factors
 * ====================================
 * Difficulty: Easy
 * Tags: Math, Enumeration, Number Theory
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
    int commonFactors(int a, int b) {
        // Number theory approach
        auto gcd_func = [](int a, int b) -> int {
            while (b) { int t = b; b = a % b; a = t; }
            return a;
        };
        int result = a[0];
        for (int i = 1; i < (int)a.size(); i++) {
            result = gcd_func(result, a[i]);
        }
        return result;
    }
};
