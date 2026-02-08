/*
 * Problem 2035: Partition Array Into Two Arrays to Minimize Sum Difference
 * ======================================================================
 * Difficulty: Hard
 * Tags: Array, Two Pointers, Binary Search, Dynamic Programming, Bit Manipulation, Sorting, Ordered Set, Bitmask
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
    int minimumDifference(vector<int>& nums) {
        // Ordered set - O(n log n) time
        set<int> ordered;
        int result = 0;
        for (int val : nums) {
            auto it = ordered.lower_bound(val);
            if (it != ordered.end()) {
                result = max(result, *it - val);
            }
            ordered.insert(val);
        }
        return result;
    }
};
