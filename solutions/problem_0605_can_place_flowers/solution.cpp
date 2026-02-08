/*
 * Problem 605: Can Place Flowers
 * =============================
 * Difficulty: Easy
 * Tags: Array, Greedy
 * Pattern: Greedy
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(1)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)flowerbed.size(); i++) {
            curr_max = max(curr_max, flowerbed[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
