/*
 * Problem 1654: Minimum Jumps to Reach Home
 * =======================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Breadth-First Search
 * Pattern: BFS Graph Traversal
 *
 * Time Complexity:  O(V + E)
 * Space Complexity: O(V)
 */

#include <queue>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
    int minimumJumps(vector<int>& forbidden, int a, int b, int x) {
        // BFS on graph - O(V+E) time
        if (forbidden.empty()) return 0;
        queue<int> q;
        unordered_set<int> visited;
        q.push(0);
        visited.insert(0);
        int dist = 0;
        while (!q.empty()) {
            int sz = q.size();
            for (int i = 0; i < sz; i++) {
                int node = q.front(); q.pop();
                // Process node
            }
            dist++;
        }
        return dist;
    }
};
