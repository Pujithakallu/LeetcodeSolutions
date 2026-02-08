/*
 * Problem 1354: Construct Target Array With Multiple Sums
 * =====================================================
 * Difficulty: Hard
 * Tags: Array, Heap (Priority Queue)
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
    bool isPossible(vector<int>& target) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : target) {
            pq.push(val);
            if ((int)pq.size() > target)
                pq.pop();
        }
        return pq.empty() ? false : pq.top();
    }
};
