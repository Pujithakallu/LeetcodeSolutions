/*
 * Problem 1569: Number of Ways to Reorder Array to Get Same BST
 * ===========================================================
 * Difficulty: Hard
 * Tags: Array, Math, Divide and Conquer, Dynamic Programming, Tree, Union-Find, Binary Search Tree, Memoization, Combinatorics, Binary Tree
 * Pattern: Union-Find / Disjoint Set
 *
 * Time Complexity:  O(n * alpha(n))
 * Space Complexity: O(n)
 */

#include <functional>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int numOfWays(vector<int>& nums) {
        // Union Find (DSU) - O(n * alpha(n))
        int n = nums.size();
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
