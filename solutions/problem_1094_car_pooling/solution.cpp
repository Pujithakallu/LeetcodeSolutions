/*
 * Problem 1094: Car Pooling
 * =======================
 * Difficulty: Medium
 * Tags: Array, Sorting, Heap (Priority Queue), Simulation, Prefix Sum
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
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : trips) {
            pq.push(val);
            if ((int)pq.size() > capacity)
                pq.pop();
        }
        return pq.empty() ? false : pq.top();
    }
};
