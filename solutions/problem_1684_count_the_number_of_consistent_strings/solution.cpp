/*
 * Problem 1684: Count the Number of Consistent Strings
 * ==================================================
 * Difficulty: Easy
 * Tags: Array, Hash Table, String, Bit Manipulation, Counting
 * Pattern: Bit Manipulation
 *
 * Time Complexity:  O(n) or O(log n)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int countConsistentStrings(string& allowed, vector<string>& words) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : allowed) {
            result ^= val;
        }
        return result;
    }
};
