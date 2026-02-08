/*
 * Problem 1615: Maximal Network Rank
 * ================================
 * Difficulty: Medium
 * Tags: Graph Theory
 * Pattern: Graph Algorithm
 *
 * Time Complexity:  O(V + E)
 * Space Complexity: O(V + E)
 */

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int maximalNetworkRank(int n, vector<vector<int>>& roads) {
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
