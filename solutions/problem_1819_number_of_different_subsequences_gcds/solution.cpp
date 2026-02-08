/*
 * Problem 1819: Number of Different Subsequences GCDs
 * =================================================
 * Difficulty: Hard
 * Tags: Array, Math, Counting, Number Theory
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
    int countDifferentSubsequenceGCDs(vector<int>& nums) {
        // Number theory approach
        auto gcd_func = [](int a, int b) -> int {
            while (b) { int t = b; b = a % b; a = t; }
            return a;
        };
        int result = nums[0];
        for (int i = 1; i < (int)nums.size(); i++) {
            result = gcd_func(result, nums[i]);
        }
        return result;
    }
};
