/*
 * Problem 1904: The Number of Full Rounds You Have Played
 * =====================================================
 * Difficulty: Medium
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
    int numberOfRounds(string& loginTime, string& logoutTime) {
        // Mathematical approach
        long long result = 0;
        int x = loginTime;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
