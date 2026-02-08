/*
 * Problem 363: Max Sum of Rectangle No Larger Than K
 * =================================================
 * Difficulty: Hard
 * Tags: Array, Binary Search, Matrix, Prefix Sum, Ordered Set
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
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        // Ordered set - O(n log n) time
        set<int> ordered;
        int result = 0;
        for (int val : matrix) {
            auto it = ordered.lower_bound(val);
            if (it != ordered.end()) {
                result = max(result, *it - val);
            }
            ordered.insert(val);
        }
        return result;
    }
};
