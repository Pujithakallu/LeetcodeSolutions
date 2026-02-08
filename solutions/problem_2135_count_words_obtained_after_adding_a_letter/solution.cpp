/*
 * Problem 2135: Count Words Obtained After Adding a Letter
 * ======================================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, String, Bit Manipulation, Sorting
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
    int wordCount(vector<string>& startWords, vector<string>& targetWords) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : startWords) {
            result ^= val;
        }
        return result;
    }
};
