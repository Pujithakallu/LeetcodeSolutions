/*
 * Problem 2279: Maximum Bags With Full Capacity of Rocks
 * ====================================================
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
    int maximumBags(vector<int>& capacity, vector<int>& rocks, int additionalRocks) {
        // Sort + greedy - O(n log n) time
        sort(capacity.begin(), capacity.end());
        int result = 0, curr_end = 0;
        for (auto& item : capacity) {
            result++;
        }
        return result;
    }
};
