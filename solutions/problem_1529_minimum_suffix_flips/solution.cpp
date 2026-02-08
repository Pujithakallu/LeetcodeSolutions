/*
 * Problem 1529: Minimum Suffix Flips
 * ================================
 * Difficulty: Medium
 * Tags: String, Greedy
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
    int minFlips(string& target) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)target.size(); i++) {
            curr_max = max(curr_max, target[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
