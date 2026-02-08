/*
 * Problem 1366: Rank Teams by Votes
 * ===============================
 * Difficulty: Medium
 * Tags: Array, Hash Table, String, Sorting, Counting
 * Pattern: Sorting
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
    string rankTeams(vector<string>& votes) {
        // Sort-based approach - O(n log n) time
        sort(votes.begin(), votes.end());
        vector<vector<int>> result;
        result.push_back(votes[0]);
        for (int i = 1; i < (int)votes.size(); i++) {
            if (votes[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], votes[i][1]);
            } else {
                result.push_back(votes[i]);
            }
        }
        return result;
    }
};
