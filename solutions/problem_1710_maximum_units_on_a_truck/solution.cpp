/*
 * Problem 1710: Maximum Units on a Truck
 * ====================================
 * Difficulty: Easy
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
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        // Sort + greedy - O(n log n) time
        sort(boxTypes.begin(), boxTypes.end());
        int result = 0, curr_end = 0;
        for (auto& item : boxTypes) {
            result++;
        }
        return result;
    }
};
