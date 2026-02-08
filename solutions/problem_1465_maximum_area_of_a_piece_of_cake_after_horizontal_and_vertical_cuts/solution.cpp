/*
 * Problem 1465: Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
 * ==============================================================================
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
    int maxArea(int h, int w, vector<int>& horizontalCuts, vector<int>& verticalCuts) {
        // Sort + greedy - O(n log n) time
        sort(h.begin(), h.end());
        int result = 0, curr_end = 0;
        for (auto& item : h) {
            result++;
        }
        return result;
    }
};
