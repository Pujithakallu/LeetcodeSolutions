/*
 * Problem 1561: Maximum Number of Coins You Can Get
 * ===============================================
 * Difficulty: Medium
 * Tags: Array, Math, Greedy, Sorting, Game Theory
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
    int maxCoins(vector<int>& piles) {
        // Sort + greedy - O(n log n) time
        sort(piles.begin(), piles.end());
        int result = 0, curr_end = 0;
        for (auto& item : piles) {
            result++;
        }
        return result;
    }
};
