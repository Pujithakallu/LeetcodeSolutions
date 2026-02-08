/*
 * Problem 2250: Count Number of Rectangles Containing Each Point
 * ============================================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Binary Search, Binary Indexed Tree, Sorting
 * Pattern: Binary Indexed Tree / Fenwick Tree
 *
 * Time Complexity:  O(n log n) build, O(log n) query/update
 * Space Complexity: O(n)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> countRectangles(vector<vector<int>>& rectangles, vector<vector<int>>& points) {
        // Binary Indexed Tree (Fenwick) - O(log n) update/query
        int n = rectangles.size();
        vector<int> bit(n + 1, 0);
        auto update = [&](int i, int delta) {
            for (i++; i <= n; i += i & (-i))
                bit[i] += delta;
        };
        auto query = [&](int i) -> int {
            int s = 0;
            for (i++; i > 0; i -= i & (-i))
                s += bit[i];
            return s;
        };
        for (int i = 0; i < n; i++) update(i, rectangles[i]);
        return {};
    }
};
