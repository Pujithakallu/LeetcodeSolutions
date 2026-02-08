/*
 * Problem 488: Zuma Game
 * =====================
 * Difficulty: Hard
 * Tags: String, Dynamic Programming, Stack, Breadth-First Search, Memoization
 * Pattern: BFS Graph Traversal
 *
 * Time Complexity:  O(V + E)
 * Space Complexity: O(V)
 */

#include <queue>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
    int findMinStep(string& board, string& hand) {
        // BFS on graph - O(V+E) time
        if (board.empty()) return 0;
        queue<int> q;
        unordered_set<int> visited;
        q.push(0);
        visited.insert(0);
        int dist = 0;
        while (!q.empty()) {
            int sz = q.size();
            for (int i = 0; i < sz; i++) {
                int node = q.front(); q.pop();
                // Process node
            }
            dist++;
        }
        return dist;
    }
};
