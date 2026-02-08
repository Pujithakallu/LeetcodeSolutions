/*
 * Problem 2251: Number of Flowers in Full Bloom
 * ===========================================
 * Difficulty: Hard
 * Tags: Array, Hash Table, Binary Search, Sorting, Prefix Sum, Ordered Set
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
    vector<int> fullBloomFlowers(vector<vector<int>>& flowers, vector<int>& people) {
        // Ordered set - O(n log n) time
        set<int> ordered;
        int result = 0;
        for (int val : flowers) {
            auto it = ordered.lower_bound(val);
            if (it != ordered.end()) {
                result = max(result, *it - val);
            }
            ordered.insert(val);
        }
        return result;
    }
};
