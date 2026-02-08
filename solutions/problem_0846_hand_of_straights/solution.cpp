/*
 * Problem 846: Hand of Straights
 * =============================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Greedy, Sorting
 * Pattern: Greedy / Hash Map
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
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        // Sort + greedy - O(n log n) time
        sort(hand.begin(), hand.end());
        int result = 0, curr_end = 0;
        for (auto& item : hand) {
            result++;
        }
        return result;
    }
};
