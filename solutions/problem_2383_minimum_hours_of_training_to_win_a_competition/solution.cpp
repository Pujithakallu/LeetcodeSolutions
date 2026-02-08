/*
 * Problem 2383: Minimum Hours of Training to Win a Competition
 * ==========================================================
 * Difficulty: Easy
 * Tags: Array, Greedy
 * Pattern: Greedy
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(1)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int minNumberOfHours(int initialEnergy, int initialExperience, vector<int>& energy, vector<int>& experience) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)initialEnergy.size(); i++) {
            curr_max = max(curr_max, initialEnergy[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
