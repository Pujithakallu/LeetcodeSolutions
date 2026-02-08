/*
 * Problem 2462: Total Cost to Hire K Workers
 * ========================================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, Heap (Priority Queue), Simulation
 * Pattern: Two Heaps / Greedy
 *
 * Time Complexity:  O((k+c) log c)
 * Space Complexity: O(c)
 */

#include <queue>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int totalCost(vector<int>& costs, int k, int candidates) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : costs) {
            pq.push(val);
            if ((int)pq.size() > k)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
