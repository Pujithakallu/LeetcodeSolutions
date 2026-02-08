/*
 * Problem 2126: Destroying Asteroids
 * ================================
 * Difficulty: Medium
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
    bool asteroidsDestroyed(int mass, vector<int>& asteroids) {
        // Sort + greedy - O(n log n) time
        sort(mass.begin(), mass.end());
        int result = 0, curr_end = 0;
        for (auto& item : mass) {
            result++;
        }
        return result;
    }
};
