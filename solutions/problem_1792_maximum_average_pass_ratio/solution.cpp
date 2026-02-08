/*
 * Problem 1792: Maximum Average Pass Ratio
 * ======================================
 * Difficulty: Medium
 * Tags: Array, Greedy, Heap (Priority Queue)
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
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : classes) {
            pq.push(val);
            if ((int)pq.size() > extraStudents)
                pq.pop();
        }
        return pq.empty() ? 0.0 : pq.top();
    }
};
