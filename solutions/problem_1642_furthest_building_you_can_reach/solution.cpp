/*
 * Problem 1642: Furthest Building You Can Reach
 * ===========================================
 * Difficulty: Medium
 * Tags: Array, Greedy, Heap (Priority Queue)
 * Pattern: Heap / Greedy
 *
 * Time Complexity:  O(n log L)
 * Space Complexity: O(L)
 */

#include <queue>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : heights) {
            pq.push(val);
            if ((int)pq.size() > bricks)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
