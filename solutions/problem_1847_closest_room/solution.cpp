/*
 * Problem 1847: Closest Room
 * ========================
 * Difficulty: Hard
 * Tags: Array, Binary Search, Sorting, Ordered Set
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
    vector<int> closestRoom(vector<vector<int>>& rooms, vector<vector<int>>& queries) {
        // Ordered set - O(n log n) time
        set<int> ordered;
        int result = 0;
        for (int val : rooms) {
            auto it = ordered.lower_bound(val);
            if (it != ordered.end()) {
                result = max(result, *it - val);
            }
            ordered.insert(val);
        }
        return result;
    }
};
