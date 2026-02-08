/*
 * Problem 1921: Eliminate Maximum Number of Monsters
 * ================================================
 * Difficulty: Medium
 * Tags: Array, Greedy, Sorting
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
    int eliminateMaximum(vector<int>& dist, vector<int>& speed) {
        // Sort + greedy - O(n log n) time
        sort(dist.begin(), dist.end());
        int result = 0, curr_end = 0;
        for (auto& item : dist) {
            result++;
        }
        return result;
    }
};
