/*
 * Problem 1834: Single-Threaded CPU
 * ===============================
 * Difficulty: Medium
 * Tags: Array, Sorting, Heap (Priority Queue)
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
    vector<int> getOrder(vector<vector<int>>& tasks) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : tasks) {
            pq.push(val);
            if ((int)pq.size() > tasks)
                pq.pop();
        }
        return pq.empty() ? {} : pq.top();
    }
};
