/*
 * Problem 2350: Shortest Impossible Sequence of Rolls
 * =================================================
 * Difficulty: Hard
 * Tags: Array, Hash Table, Greedy
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
    int shortestSequence(vector<int>& rolls, int k) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)rolls.size(); i++) {
            curr_max = max(curr_max, rolls[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
