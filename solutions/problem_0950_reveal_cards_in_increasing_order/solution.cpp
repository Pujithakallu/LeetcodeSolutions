/*
 * Problem 950: Reveal Cards In Increasing Order
 * ============================================
 * Difficulty: Medium
 * Tags: Array, Queue, Sorting, Simulation
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
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        // Queue-based approach - O(n) time
        queue<int> q;
        for (int val : deck) {
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
