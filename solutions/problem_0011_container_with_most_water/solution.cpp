/*
 * Problem 11: Container With Most Water
 * =====================================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, Greedy
 * Pattern: Two Pointers
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
    int maxArea(vector<int>& height) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)height.size(); i++) {
            curr_max = max(curr_max, height[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
