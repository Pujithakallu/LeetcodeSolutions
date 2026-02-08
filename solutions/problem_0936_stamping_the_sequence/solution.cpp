/*
 * Problem 936: Stamping The Sequence
 * =================================
 * Difficulty: Hard
 * Tags: String, Stack, Greedy, Queue
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
    vector<int> movesToStamp(string& stamp, string& target) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)stamp.size(); i++) {
            curr_max = max(curr_max, stamp[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
