/*
 * Problem 1360: Number of Days Between Two Dates
 * ============================================
 * Difficulty: Easy
 * Tags: Math, String
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
    int daysBetweenDates(string& date1, string& date2) {
        // Mathematical approach
        long long result = 0;
        int x = date1;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
