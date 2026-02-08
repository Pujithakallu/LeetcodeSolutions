/*
 * Problem 1743: Restore the Array From Adjacent Pairs
 * =================================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Depth-First Search
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
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
        // DFS on graph - O(V+E) time
        vector<bool> visited(adjacentPairs.size(), false);
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
