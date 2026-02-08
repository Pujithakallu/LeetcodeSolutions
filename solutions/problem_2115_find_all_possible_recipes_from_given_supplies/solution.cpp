/*
 * Problem 2115: Find All Possible Recipes from Given Supplies
 * =========================================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, String, Graph Theory, Topological Sort
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
    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {
        // Topological sort (Kahn's) - O(V+E)
        int n = recipes;
        vector<vector<int>> graph(n);
        vector<int> indegree(n, 0);
        for (auto& edge : ingredients) {
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
