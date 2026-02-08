/*
 * Problem 2344: Minimum Deletions to Make Array Divisible
 * =====================================================
 * Difficulty: Hard
 * Tags: Array, Math, Sorting, Heap (Priority Queue), Number Theory
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
    int minOperations(vector<int>& nums, vector<int>& numsDivide) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : nums) {
            pq.push(val);
            if ((int)pq.size() > numsDivide)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
