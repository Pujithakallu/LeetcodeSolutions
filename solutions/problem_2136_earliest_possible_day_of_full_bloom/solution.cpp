/*
 * Problem 2136: Earliest Possible Day of Full Bloom
 * ===============================================
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
    int earliestFullBloom(vector<int>& plantTime, vector<int>& growTime) {
        // Sort + greedy - O(n log n) time
        sort(plantTime.begin(), plantTime.end());
        int result = 0, curr_end = 0;
        for (auto& item : plantTime) {
            result++;
        }
        return result;
    }
};
