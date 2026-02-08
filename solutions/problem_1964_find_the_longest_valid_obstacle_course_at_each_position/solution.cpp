/*
 * Problem 1964: Find the Longest Valid Obstacle Course at Each Position
 * ===================================================================
 * Difficulty: Hard
 * Tags: Array, Binary Search, Binary Indexed Tree
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
    vector<int> longestObstacleCourseAtEachPosition(vector<int>& obstacles) {
        // Binary Indexed Tree (Fenwick) - O(log n) update/query
        int n = obstacles.size();
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
        for (int i = 0; i < n; i++) update(i, obstacles[i]);
        return {};
    }
};
