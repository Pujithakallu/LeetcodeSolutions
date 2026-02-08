/*
 * Problem 927: Three Equal Parts
 * =============================
 * Difficulty: Hard
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
    vector<int> threeEqualParts(vector<int>& arr) {
        // Mathematical approach
        long long result = 0;
        int x = arr;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
