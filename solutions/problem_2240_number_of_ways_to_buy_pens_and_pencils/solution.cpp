/*
 * Problem 2240: Number of Ways to Buy Pens and Pencils
 * ==================================================
 * Difficulty: Medium
 * Tags: Math, Enumeration
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
    int waysToBuyPensPencils(int total, int cost1, int cost2) {
        // Mathematical approach
        long long result = 0;
        int x = total;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
