/*
 * Problem 1418: Display Table of Food Orders in a Restaurant
 * ========================================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, String, Sorting, Ordered Set
 * Pattern: Ordered Set / SortedList
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(n)
 */

#include <algorithm>
#include <set>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<string>> displayTable(vector<vector<string>>& orders) {
        // Ordered set - O(n log n) time
        set<int> ordered;
        int result = 0;
        for (int val : orders) {
            auto it = ordered.lower_bound(val);
            if (it != ordered.end()) {
                result = max(result, *it - val);
            }
            ordered.insert(val);
        }
        return result;
    }
};
