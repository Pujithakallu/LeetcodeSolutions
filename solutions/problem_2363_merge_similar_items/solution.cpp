/*
 * Problem 2363: Merge Similar Items
 * ===============================
 * Difficulty: Easy
 * Tags: Array, Hash Table, Sorting, Ordered Set
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
    vector<vector<int>> mergeSimilarItems(vector<vector<int>>& items1, vector<vector<int>>& items2) {
        // Ordered set - O(n log n) time
        set<int> ordered;
        int result = 0;
        for (int val : items1) {
            auto it = ordered.lower_bound(val);
            if (it != ordered.end()) {
                result = max(result, *it - val);
            }
            ordered.insert(val);
        }
        return result;
    }
};
