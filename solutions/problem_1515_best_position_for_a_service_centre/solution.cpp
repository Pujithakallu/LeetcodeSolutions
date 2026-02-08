/*
 * Problem 1515: Best Position for a Service Centre
 * ==============================================
 * Difficulty: Hard
 * Tags: Array, Math, Geometry, Randomized
 * Pattern: Randomized Algorithm
 *
 * Time Complexity:  O(n) or varies
 * Space Complexity: O(n)
 */

#include <cstdlib>
#include <ctime>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    double getMinDistSum(vector<vector<int>>& positions) {
        // Randomized approach (Fisher-Yates shuffle)
        vector<int> arr = positions;
        srand(time(0));
        for (int i = arr.size() - 1; i > 0; i--) {
            int j = rand() % (i + 1);
            swap(arr[i], arr[j]);
        }
        return arr;
    }
};
