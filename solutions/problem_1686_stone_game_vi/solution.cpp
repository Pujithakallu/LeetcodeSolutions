/*
 * Problem 1686: Stone Game VI
 * =========================
 * Difficulty: Medium
 * Tags: Array, Math, Greedy, Sorting, Heap (Priority Queue), Game Theory
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
    int stoneGameVI(vector<int>& aliceValues, vector<int>& bobValues) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : aliceValues) {
            pq.push(val);
            if ((int)pq.size() > bobValues)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
