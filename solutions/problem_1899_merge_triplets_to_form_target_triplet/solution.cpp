/*
 * Problem 1899: Merge Triplets to Form Target Triplet
 * =================================================
 * Difficulty: Medium
 * Tags: Array, Greedy
 * Pattern: Greedy
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(1)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)triplets.size(); i++) {
            curr_max = max(curr_max, triplets[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
