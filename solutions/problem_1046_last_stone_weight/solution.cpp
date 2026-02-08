/*
 * Problem 1046: Last Stone Weight
 * =============================
 * Difficulty: Easy
 * Tags: Array, Heap (Priority Queue)
 * Pattern: Heap
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
    int lastStoneWeight(vector<int>& stones) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : stones) {
            pq.push(val);
            if ((int)pq.size() > stones)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
