/*
 * Problem 1276: Number of Burgers with No Waste of Ingredients
 * ==========================================================
 * Difficulty: Medium
 * Tags: Math
 * Pattern: Math
 *
 * Time Complexity:  O(n) or O(sqrt(n))
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> numOfBurgers(int tomatoSlices, int cheeseSlices) {
        // Mathematical approach
        long long result = 0;
        int x = tomatoSlices;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
