/*
 * Problem 781: Rabbits in Forest
 * =============================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Math, Greedy
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
    int numRabbits(vector<int>& answers) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)answers.size(); i++) {
            curr_max = max(curr_max, answers[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
