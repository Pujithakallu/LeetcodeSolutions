/*
 * Problem 1823: Find the Winner of the Circular Game
 * ================================================
 * Difficulty: Medium
 * Tags: Array, Math, Recursion, Queue, Simulation
 * Pattern: Queue / BFS
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n)
 */

#include <queue>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int findTheWinner(int n, int k) {
        // Queue-based approach - O(n) time
        queue<int> q;
        for (int val : n) {
            q.push(val);
        }
        vector<int> result;
        while (!q.empty()) {
            result.push_back(q.front());
            q.pop();
        }
        return result;
    }
};
