/*
 * Problem 787: Cheapest Flights Within K Stops
 * ===========================================
 * Difficulty: Medium
 * Tags: Dynamic Programming, Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Shortest Path
 * Pattern: Bellman-Ford (k stops)
 *
 * Time Complexity:  O(k * E)
 * Space Complexity: O(V)
 */

#include <queue>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : n) {
            pq.push(val);
            if ((int)pq.size() > flights)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
