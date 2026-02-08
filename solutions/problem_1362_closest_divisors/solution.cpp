/*
 * Problem 1362: Closest Divisors
 * ============================
 * Difficulty: Medium
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
    vector<int> closestDivisors(int num) {
        // Mathematical approach
        long long result = 0;
        int x = num;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
