/*
 * Problem 210: Course Schedule II
 * ==============================
 * Difficulty: Medium
 * Tags: Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort
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
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        // Topological sort (Kahn's) - O(V+E)
        int n = numCourses;
        vector<vector<int>> graph(n);
        vector<int> indegree(n, 0);
        for (auto& edge : prerequisites) {
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
