/*
 * Problem 1488: Avoid Flood in The City
 * ===================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Binary Search, Greedy, Heap (Priority Queue)
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
    vector<int> avoidFlood(vector<int>& rains) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : rains) {
            pq.push(val);
            if ((int)pq.size() > rains)
                pq.pop();
        }
        return pq.empty() ? {} : pq.top();
    }
};
