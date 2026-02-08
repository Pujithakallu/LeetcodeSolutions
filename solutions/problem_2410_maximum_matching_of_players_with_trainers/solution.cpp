/*
 * Problem 2410: Maximum Matching of Players With Trainers
 * =====================================================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, Greedy, Sorting
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
    int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
        // Sort + greedy - O(n log n) time
        sort(players.begin(), players.end());
        int result = 0, curr_end = 0;
        for (auto& item : players) {
            result++;
        }
        return result;
    }
};
