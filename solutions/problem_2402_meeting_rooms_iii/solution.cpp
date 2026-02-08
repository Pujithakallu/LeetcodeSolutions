/*
 * Problem 2402: Meeting Rooms III
 * =============================
 * Difficulty: Hard
 * Tags: Array, Hash Table, Sorting, Heap (Priority Queue), Simulation
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
    int mostBooked(int n, vector<vector<int>>& meetings) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : n) {
            pq.push(val);
            if ((int)pq.size() > meetings)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
