/*
 * Problem 630: Course Schedule III
 * ===============================
 * Difficulty: Hard
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
    int scheduleCourse(vector<vector<int>>& courses) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : courses) {
            pq.push(val);
            if ((int)pq.size() > courses)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
