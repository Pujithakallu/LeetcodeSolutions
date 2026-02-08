/*
 * Problem 882: Reachable Nodes In Subdivided Graph
 * ===============================================
 * Difficulty: Hard
 * Tags: Graph Theory, Heap (Priority Queue), Shortest Path
 * Pattern: Heap / Priority Queue
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(n)
 */

#include <queue>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int reachableNodes(vector<vector<int>>& edges, int maxMoves, int n) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : edges) {
            pq.push(val);
            if ((int)pq.size() > maxMoves)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
