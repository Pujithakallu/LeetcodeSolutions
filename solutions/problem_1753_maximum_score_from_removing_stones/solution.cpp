/*
 * Problem 1753: Maximum Score From Removing Stones
 * ==============================================
 * Difficulty: Medium
 * Tags: Math, Greedy, Heap (Priority Queue)
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
    int maximumScore(int a, int b, int c) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : a) {
            pq.push(val);
            if ((int)pq.size() > b)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
