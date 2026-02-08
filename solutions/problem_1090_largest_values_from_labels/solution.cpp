/*
 * Problem 1090: Largest Values From Labels
 * ======================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Greedy, Sorting, Counting
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
    int largestValsFromLabels(vector<int>& values, vector<int>& labels, int numWanted, int useLimit) {
        // Sort + greedy - O(n log n) time
        sort(values.begin(), values.end());
        int result = 0, curr_end = 0;
        for (auto& item : values) {
            result++;
        }
        return result;
    }
};
