/*
 * Problem 841: Keys and Rooms
 * ==========================
 * Difficulty: Medium
 * Tags: Depth-First Search, Breadth-First Search, Graph Theory
 * Pattern: DFS / Graph
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
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        // DFS on graph - O(V+E) time
        vector<bool> visited(rooms.size(), false);
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
