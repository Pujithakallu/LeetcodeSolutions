/*
 * Problem 1414: Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
 * =======================================================================
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
    int findMinFibonacciNumbers(int k) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)k.size(); i++) {
            curr_max = max(curr_max, k[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
