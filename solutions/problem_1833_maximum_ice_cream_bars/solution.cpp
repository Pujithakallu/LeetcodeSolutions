/*
 * Problem 1833: Maximum Ice Cream Bars
 * ==================================
 * Difficulty: Medium
 * Tags: Array, Greedy, Sorting, Counting Sort
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
    int maxIceCream(vector<int>& costs, int coins) {
        // Sort + greedy - O(n log n) time
        sort(costs.begin(), costs.end());
        int result = 0, curr_end = 0;
        for (auto& item : costs) {
            result++;
        }
        return result;
    }
};
