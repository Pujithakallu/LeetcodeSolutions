/*
 * Problem 514: Freedom Trail
 * =========================
 * Difficulty: Hard
 * Tags: String, Dynamic Programming, Depth-First Search, Breadth-First Search
 * Pattern: DFS Graph Traversal
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
    int findRotateSteps(string& ring, string& key) {
        // DFS on graph - O(V+E) time
        vector<bool> visited(ring.size(), false);
        vector<int> result;
        function<void(int)> dfs = [&](int node) {
            if (visited[node]) return;
            visited[node] = true;
            result.push_back(node);
            // Traverse neighbors
        };
        dfs(0);
        return result;
    }
};
