/*
 * Problem 973: K Closest Points to Origin
 * ======================================
 * Difficulty: Medium
 * Tags: Array, Math, Divide and Conquer, Geometry, Sorting, Heap (Priority Queue), Quickselect
 * Pattern: Heap / Quickselect
 *
 * Time Complexity:  O(n log k)
 * Space Complexity: O(k)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // Quickselect - O(n) average time
        int k = k;
        nth_element(points.begin(), points.begin() + points.size() - k, points.end());
        return points[points.size() - k];
    }
};
