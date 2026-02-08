/*
 * Problem 1337: The K Weakest Rows in a Matrix
 * ==========================================
 * Difficulty: Easy
 * Tags: Array, Binary Search, Sorting, Heap (Priority Queue), Matrix
 * Pattern: Heap / Sorting
 *
 * Time Complexity:  O(m*n + k*log m)
 * Space Complexity: O(m)
 */

#include <queue>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : mat) {
            pq.push(val);
            if ((int)pq.size() > k)
                pq.pop();
        }
        return pq.empty() ? {} : pq.top();
    }
};
