/*
 * Problem 1333: Filter Restaurants by Vegan-Friendly, Price and Distance
 * ====================================================================
 * Difficulty: Medium
 * Tags: Array, Sorting
 * Pattern: Sorting
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
    vector<int> filterRestaurants(vector<vector<int>>& restaurants, int veganFriendly, int maxPrice, int maxDistance) {
        // Sort-based approach - O(n log n) time
        sort(restaurants.begin(), restaurants.end());
        vector<vector<int>> result;
        result.push_back(restaurants[0]);
        for (int i = 1; i < (int)restaurants.size(); i++) {
            if (restaurants[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], restaurants[i][1]);
            } else {
                result.push_back(restaurants[i]);
            }
        }
        return result;
    }
};
