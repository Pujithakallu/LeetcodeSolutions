/*
 * Problem 743: Network Delay Time
 * ==============================
 * Difficulty: Medium
 * Tags: Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Shortest Path
 * Pattern: Dijkstra / Shortest Path
 *
 * Time Complexity:  O(E log V)
 * Space Complexity: O(V + E)
 */

#include <queue>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : times) {
            pq.push(val);
            if ((int)pq.size() > n)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
