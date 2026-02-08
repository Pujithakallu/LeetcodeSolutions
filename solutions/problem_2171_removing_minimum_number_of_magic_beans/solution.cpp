/*
 * Problem 2171: Removing Minimum Number of Magic Beans
 * ==================================================
 * Difficulty: Medium
 * Tags: Array, Greedy, Sorting, Enumeration, Prefix Sum
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
    int minimumRemoval(vector<int>& beans) {
        // Sort + greedy - O(n log n) time
        sort(beans.begin(), beans.end());
        int result = 0, curr_end = 0;
        for (auto& item : beans) {
            result++;
        }
        return result;
    }
};
