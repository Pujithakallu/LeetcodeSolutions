/*
 * Problem 385: Mini Parser
 * =======================
 * Difficulty: Medium
 * Tags: String, Stack, Depth-First Search
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
    NestedInteger deserialize(string& s) {
        // DFS on graph - O(V+E) time
        vector<bool> visited(s.size(), false);
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
