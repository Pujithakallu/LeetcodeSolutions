/*
 * Problem 854: K-Similar Strings
 * =============================
 * Difficulty: Hard
 * Tags: Hash Table, String, Breadth-First Search
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
    int kSimilarity(string& s1, string& s2) {
        // BFS on graph - O(V+E) time
        if (s1.empty()) return 0;
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
