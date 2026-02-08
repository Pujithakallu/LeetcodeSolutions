/*
 * Problem 1185: Day of the Week
 * ===========================
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
    string dayOfTheWeek(int day, int month, int year) {
        // Mathematical approach
        long long result = 0;
        int x = day;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
