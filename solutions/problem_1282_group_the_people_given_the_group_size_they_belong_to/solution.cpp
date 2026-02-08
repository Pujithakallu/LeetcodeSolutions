/*
 * Problem 1282: Group the People Given the Group Size They Belong To
 * ================================================================
 * Difficulty: Medium
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
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)groupSizes.size(); i++) {
            curr_max = max(curr_max, groupSizes[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
