/*
 * Problem 1247: Minimum Swaps to Make Strings Equal
 * ===============================================
 * Difficulty: Medium
 * Tags: Math, String, Greedy
 * Pattern: Greedy
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(1)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int minimumSwap(string& s1, string& s2) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)s1.size(); i++) {
            curr_max = max(curr_max, s1[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
