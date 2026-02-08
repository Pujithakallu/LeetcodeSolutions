/*
 * Problem 757: Set Intersection Size At Least Two
 * ==============================================
 * Difficulty: Hard
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
    int intersectionSizeTwo(vector<vector<int>>& intervals) {
        // Sort + greedy - O(n log n) time
        sort(intervals.begin(), intervals.end());
        int result = 0, curr_end = 0;
        for (auto& item : intervals) {
            result++;
        }
        return result;
    }
};
