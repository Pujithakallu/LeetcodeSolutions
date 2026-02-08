/*
 * Problem 2203: Minimum Weighted Subgraph With the Required Paths
 * =============================================================
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
    int minimumWeight(int n, vector<vector<int>>& edges, int src1, int src2, int dest) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : n) {
            pq.push(val);
            if ((int)pq.size() > edges)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
