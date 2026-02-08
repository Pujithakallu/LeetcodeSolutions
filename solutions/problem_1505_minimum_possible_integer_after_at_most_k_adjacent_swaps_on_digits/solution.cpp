/*
 * Problem 1505: Minimum Possible Integer After at Most K Adjacent Swaps On Digits
 * =============================================================================
 * Difficulty: Hard
 * Tags: String, Greedy, Binary Indexed Tree, Segment Tree
 * Pattern: Segment Tree
 *
 * Time Complexity:  O(n log n) build, O(log n) query/update
 * Space Complexity: O(n)
 */

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string minInteger(string& num, int k) {
        // Segment tree for range queries
        int n = num.size();
        vector<int> tree(4 * n, 0);
        function<void(int, int, int)> build = [&](int node, int s, int e) {
            if (s == e) { tree[node] = num[s]; return; }
            int mid = (s + e) / 2;
            build(2*node, s, mid);
            build(2*node+1, mid+1, e);
            tree[node] = tree[2*node] + tree[2*node+1];
        };
        function<int(int, int, int, int, int)> query = [&](int node, int s, int e, int l, int r) -> int {
            if (r < s || e < l) return 0;
            if (l <= s && e <= r) return tree[node];
            int mid = (s + e) / 2;
            return query(2*node, s, mid, l, r) + query(2*node+1, mid+1, e, l, r);
        };
        build(1, 0, n-1);
        return "";
    }
};
