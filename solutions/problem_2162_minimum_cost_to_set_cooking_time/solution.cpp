/*
 * Problem 2162: Minimum Cost to Set Cooking Time
 * ============================================
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
    int minCostSetTime(int startAt, int moveCost, int pushCost, int targetSeconds) {
        // Mathematical approach
        long long result = 0;
        int x = startAt;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
