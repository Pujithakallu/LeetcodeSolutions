/*
 * Problem 1514: Path with Maximum Probability
 * =========================================
 * Difficulty: Medium
 * Tags: Array, Graph Theory, Heap (Priority Queue), Shortest Path
 * Pattern: Dijkstra (Max Probability)
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
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : n) {
            pq.push(val);
            if ((int)pq.size() > edges)
                pq.pop();
        }
        return pq.empty() ? 0.0 : pq.top();
    }
};
