/*
 * Problem 991: Broken Calculator
 * =============================
 * Difficulty: Medium
 * Tags: Math, Greedy
 * Pattern: Greedy
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(1)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int brokenCalc(int startValue, int target) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)startValue.size(); i++) {
            curr_max = max(curr_max, startValue[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
