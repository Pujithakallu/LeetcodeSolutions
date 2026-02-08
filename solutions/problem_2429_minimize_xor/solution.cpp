/*
 * Problem 2429: Minimize XOR
 * ========================
 * Difficulty: Medium
 * Tags: Greedy, Bit Manipulation
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
    int minimizeXor(int num1, int num2) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)num1.size(); i++) {
            curr_max = max(curr_max, num1[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
