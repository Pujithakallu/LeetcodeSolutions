/*
 * Problem 1433: Check If a String Can Break Another String
 * ======================================================
 * Difficulty: Medium
 * Tags: String, Greedy, Sorting
 * Pattern: Greedy with Sorting
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(n)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool checkIfCanBreak(string& s1, string& s2) {
        // Sort + greedy - O(n log n) time
        sort(s1.begin(), s1.end());
        int result = 0, curr_end = 0;
        for (auto& item : s1) {
            result++;
        }
        return result;
    }
};
