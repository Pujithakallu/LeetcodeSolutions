/*
 * Problem 1584: Min Cost to Connect All Points
 * ==========================================
 * Difficulty: Medium
 * Tags: Array, Union-Find, Graph Theory, Minimum Spanning Tree
 * Pattern: Prim's MST / Graph
 *
 * Time Complexity:  O(n^2 log n)
 * Space Complexity: O(n^2)
 */

#include <functional>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        // Union Find (DSU) - O(n * alpha(n))
        int n = points.size();
        vector<int> parent(n + 1), rnk(n + 1, 0);
        iota(parent.begin(), parent.end(), 0);
        function<int(int)> find = [&](int x) -> int {
            return parent[x] == x ? x : parent[x] = find(parent[x]);
        };
        auto unite = [&](int x, int y) -> bool {
            int px = find(x), py = find(y);
            if (px == py) return false;
            if (rnk[px] < rnk[py]) swap(px, py);
            parent[py] = px;
            if (rnk[px] == rnk[py]) rnk[px]++;
            return true;
        };
        int components = n;
        return components;
    }
};
