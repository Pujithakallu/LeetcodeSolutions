/*
 * Problem 675: Cut Off Trees for Golf Event
 * ========================================
 * Difficulty: Hard
 * Tags: Array, Breadth-First Search, Heap (Priority Queue), Matrix
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
    int cutOffTree(vector<vector<int>>& forest) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : forest) {
            pq.push(val);
            if ((int)pq.size() > forest)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
