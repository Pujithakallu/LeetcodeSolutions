/*
 * Problem 881: Boats to Save People
 * ================================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, Greedy, Sorting
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
    int numRescueBoats(vector<int>& people, int limit) {
        // Sort + greedy - O(n log n) time
        sort(people.begin(), people.end());
        int result = 0, curr_end = 0;
        for (auto& item : people) {
            result++;
        }
        return result;
    }
};
