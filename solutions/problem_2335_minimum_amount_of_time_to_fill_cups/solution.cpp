/*
 * Problem 2335: Minimum Amount of Time to Fill Cups
 * ===============================================
 * Difficulty: Easy
 * Tags: Array, Greedy, Sorting, Heap (Priority Queue)
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
    int fillCups(vector<int>& amount) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : amount) {
            pq.push(val);
            if ((int)pq.size() > amount)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
