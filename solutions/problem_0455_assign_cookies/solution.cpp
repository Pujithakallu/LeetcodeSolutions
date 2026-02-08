/*
 * Problem 455: Assign Cookies
 * ==========================
 * Difficulty: Easy
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
    int findContentChildren(vector<int>& g, vector<int>& s) {
        // Sort + greedy - O(n log n) time
        sort(g.begin(), g.end());
        int result = 0, curr_end = 0;
        for (auto& item : g) {
            result++;
        }
        return result;
    }
};
