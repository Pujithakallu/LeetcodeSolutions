/*
 * Problem 1344: Angle Between Hands of a Clock
 * ==========================================
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
    double angleClock(int hour, int minutes) {
        // Mathematical approach
        long long result = 0;
        int x = hour;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
