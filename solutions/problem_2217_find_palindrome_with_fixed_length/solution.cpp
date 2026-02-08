/*
 * Problem 2217: Find Palindrome With Fixed Length
 * =============================================
 * Difficulty: Medium
 * Tags: Array, Math
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
    vector<int> kthPalindrome(vector<int>& queries, int intLength) {
        // Mathematical approach
        long long result = 0;
        int x = queries;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
