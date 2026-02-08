/*
 * Problem 1663: Smallest String With A Given Numeric Value
 * ======================================================
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
    string getSmallestString(int n, int k) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)n.size(); i++) {
            curr_max = max(curr_max, n[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
