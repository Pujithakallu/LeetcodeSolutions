/*
 * Problem 1338: Reduce Array Size to The Half
 * =========================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Greedy, Sorting, Heap (Priority Queue)
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
    int minSetSize(vector<int>& arr) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : arr) {
            pq.push(val);
            if ((int)pq.size() > arr)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
