/*
 * Problem 1388: Pizza With 3n Slices
 * ================================
 * Difficulty: Hard
 * Tags: Array, Dynamic Programming, Greedy, Heap (Priority Queue)
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
    int maxSizeSlices(vector<int>& slices) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : slices) {
            pq.push(val);
            if ((int)pq.size() > slices)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
