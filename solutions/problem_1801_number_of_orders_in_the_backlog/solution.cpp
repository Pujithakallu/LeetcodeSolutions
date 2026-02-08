/*
 * Problem 1801: Number of Orders in the Backlog
 * ===========================================
 * Difficulty: Medium
 * Tags: Array, Heap (Priority Queue), Simulation
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
    int getNumberOfBacklogOrders(vector<vector<int>>& orders) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : orders) {
            pq.push(val);
            if ((int)pq.size() > orders)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
