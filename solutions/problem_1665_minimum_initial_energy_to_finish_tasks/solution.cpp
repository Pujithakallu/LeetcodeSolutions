/*
 * Problem 1665: Minimum Initial Energy to Finish Tasks
 * ==================================================
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
    int minimumEffort(vector<vector<int>>& tasks) {
        // Sort + greedy - O(n log n) time
        sort(tasks.begin(), tasks.end());
        int result = 0, curr_end = 0;
        for (auto& item : tasks) {
            result++;
        }
        return result;
    }
};
