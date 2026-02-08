/*
 * Problem 2231: Largest Number After Digit Swaps by Parity
 * ======================================================
 * Difficulty: Easy
 * Tags: Sorting, Heap (Priority Queue)
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
    int largestInteger(int num) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : num) {
            pq.push(val);
            if ((int)pq.size() > num)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
