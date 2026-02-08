/*
 * Problem 322: Coin Change
 * =======================
 * Difficulty: Medium
 * Tags: Array, Dynamic Programming, Breadth-First Search
 * Pattern: Dynamic Programming
 *
 * Time Complexity:  O(n * amount)
 * Space Complexity: O(amount)
 */

#include <queue>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // BFS on graph - O(V+E) time
        if (coins.empty()) return 0;
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
