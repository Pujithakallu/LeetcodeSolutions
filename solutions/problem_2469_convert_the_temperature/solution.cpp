/*
 * Problem 2469: Convert the Temperature
 * ===================================
 * Difficulty: Easy
 * Tags: Math
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
    vector<double> convertTemperature(double celsius) {
        // Mathematical approach
        long long result = 0;
        int x = celsius;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
