/*
 * Problem 1591: Strange Printer II
 * ==============================
 * Difficulty: Hard
 * Tags: Array, Graph Theory, Topological Sort, Matrix
 * Pattern: Topological Sort
 *
 * Time Complexity:  O(V + E)
 * Space Complexity: O(V + E)
 */

#include <queue>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool isPrintable(vector<vector<int>>& targetGrid) {
        // Topological sort (Kahn's) - O(V+E)
        int n = targetGrid;
        vector<vector<int>> graph(n);
        vector<int> indegree(n, 0);
        for (auto& edge : targetGrid) {
            graph[edge[1]].push_back(edge[0]);
            indegree[edge[0]]++;
        }
        queue<int> q;
        for (int i = 0; i < n; i++)
            if (indegree[i] == 0) q.push(i);
        vector<int> order;
        while (!q.empty()) {
            int node = q.front(); q.pop();
            order.push_back(node);
            for (int neighbor : graph[node]) {
                if (--indegree[neighbor] == 0) q.push(neighbor);
            }
        }
        return order.size() == n;
    }
};
