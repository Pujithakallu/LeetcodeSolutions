/*
 * Problem 2160: Minimum Sum of Four Digit Number After Splitting Digits
 * ===================================================================
 * Difficulty: Easy
 * Tags: Math, Greedy, Sorting
 * Pattern: Greedy with Sorting
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(n)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int minimumSum(int num) {
        // Sort + greedy - O(n log n) time
        sort(num.begin(), num.end());
        int result = 0, curr_end = 0;
        for (auto& item : num) {
            result++;
        }
        return result;
    }
};
