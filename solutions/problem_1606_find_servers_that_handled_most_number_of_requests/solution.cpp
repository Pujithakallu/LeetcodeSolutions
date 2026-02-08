/*
 * Problem 1606: Find Servers That Handled Most Number of Requests
 * =============================================================
 * Difficulty: Hard
 * Tags: Array, Heap (Priority Queue), Simulation, Ordered Set
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
    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
        // Ordered set - O(n log n) time
        set<int> ordered;
        int result = 0;
        for (int val : k) {
            auto it = ordered.lower_bound(val);
            if (it != ordered.end()) {
                result = max(result, *it - val);
            }
            ordered.insert(val);
        }
        return result;
    }
};
