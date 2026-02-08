/*
 * Problem 1131: Maximum of Absolute Value Expression
 * ================================================
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
    int maxAbsValExpr(vector<int>& arr1, vector<int>& arr2) {
        // Mathematical approach
        long long result = 0;
        int x = arr1;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
