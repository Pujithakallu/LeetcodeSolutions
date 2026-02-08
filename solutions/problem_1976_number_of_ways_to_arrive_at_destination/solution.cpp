/*
 * Problem 1976: Number of Ways to Arrive at Destination
 * ===================================================
 * Difficulty: Medium
 * Tags: Dynamic Programming, Graph Theory, Topological Sort, Shortest Path
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
    int countPaths(int n, vector<vector<int>>& roads) {
        // Topological sort (Kahn's) - O(V+E)
        int n = n;
        vector<vector<int>> graph(n);
        vector<int> indegree(n, 0);
        for (auto& edge : roads) {
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
