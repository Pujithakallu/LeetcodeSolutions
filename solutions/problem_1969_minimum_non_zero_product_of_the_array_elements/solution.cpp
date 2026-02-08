/*
 * Problem 1969: Minimum Non-Zero Product of the Array Elements
 * ==========================================================
 * Difficulty: Medium
 * Tags: Math, Greedy, Recursion
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
    int minNonZeroProduct(int p) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)p.size(); i++) {
            curr_max = max(curr_max, p[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
