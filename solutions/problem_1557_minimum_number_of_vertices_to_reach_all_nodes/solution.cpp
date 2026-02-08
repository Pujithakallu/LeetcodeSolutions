/*
 * Problem 1557: Minimum Number of Vertices to Reach All Nodes
 * =========================================================
 * Difficulty: Medium
 * Tags: Graph Theory
 * Pattern: Graph / Indegree
 *
 * Time Complexity:  O(V + E)
 * Space Complexity: O(V)
 */

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
        // Graph traversal - O(V+E) time
        int n = n.size();
        vector<vector<int>> graph(n);
        vector<bool> visited(n, false);
        int result = 0;
        function<void(int)> dfs = [&](int node) {
            visited[node] = true;
            for (int neighbor : graph[node]) {
                if (!visited[neighbor]) dfs(neighbor);
            }
        };
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i);
                result++;
            }
        }
        return result;
    }
};
