/*
 * Problem 1942: The Number of the Smallest Unoccupied Chair
 * =======================================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Heap (Priority Queue)
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
    int smallestChair(vector<vector<int>>& times, int targetFriend) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : times) {
            pq.push(val);
            if ((int)pq.size() > targetFriend)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
