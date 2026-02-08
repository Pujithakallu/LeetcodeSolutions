/*
 * Problem 1808: Maximize Number of Nice Divisors
 * ============================================
 * Difficulty: Hard
 * Tags: Math, Recursion, Number Theory
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
    int maxNiceDivisors(int primeFactors) {
        // Number theory approach
        auto gcd_func = [](int a, int b) -> int {
            while (b) { int t = b; b = a % b; a = t; }
            return a;
        };
        int result = primeFactors[0];
        for (int i = 1; i < (int)primeFactors.size(); i++) {
            result = gcd_func(result, primeFactors[i]);
        }
        return result;
    }
};
