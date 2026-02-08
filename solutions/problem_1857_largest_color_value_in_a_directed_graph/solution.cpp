/*
 * Problem 1857: Largest Color Value in a Directed Graph
 * ===================================================
 * Difficulty: Hard
 * Tags: Hash Table, String, Dynamic Programming, Graph Theory, Topological Sort, Memoization, Counting
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
    int largestPathValue(string& colors, vector<vector<int>>& edges) {
        // Topological sort (Kahn's) - O(V+E)
        int n = colors;
        vector<vector<int>> graph(n);
        vector<int> indegree(n, 0);
        for (auto& edge : edges) {
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
