/*
 * Problem 847: Shortest Path Visiting All Nodes
 * ============================================
 * Difficulty: Hard
 * Tags: Dynamic Programming, Bit Manipulation, Breadth-First Search, Graph Theory, Bitmask
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
    int shortestPathLength(vector<vector<int>>& graph) {
        // BFS on graph - O(V+E) time
        if (graph.empty()) return 0;
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
