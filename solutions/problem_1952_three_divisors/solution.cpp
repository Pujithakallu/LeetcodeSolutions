/*
 * Problem 1952: Three Divisors
 * ==========================
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
    bool isThree(int n) {
        // Number theory approach
        auto gcd_func = [](int a, int b) -> int {
            while (b) { int t = b; b = a % b; a = t; }
            return a;
        };
        int result = n[0];
        for (int i = 1; i < (int)n.size(); i++) {
            result = gcd_func(result, n[i]);
        }
        return result;
    }
};
