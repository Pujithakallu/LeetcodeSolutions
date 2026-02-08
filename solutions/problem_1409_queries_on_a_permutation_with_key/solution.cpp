/*
 * Problem 1409: Queries on a Permutation With Key
 * =============================================
 * Difficulty: Medium
 * Tags: Array, Binary Indexed Tree, Simulation
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
    vector<int> processQueries(vector<int>& queries, int m) {
        // Binary Indexed Tree (Fenwick) - O(log n) update/query
        int n = queries.size();
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
        for (int i = 0; i < n; i++) update(i, queries[i]);
        return {};
    }
};
