/*
 * Problem 2326: Spiral Matrix IV
 * ============================
 * Difficulty: Medium
 * Tags: Array, Linked List, Matrix, Simulation
 * Pattern: Linked List
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) {
        // Linked list traversal/manipulation
        ListNode dummy(0);
        dummy.next = m;
        ListNode* prev = &dummy;
        ListNode* curr = m;
        while (curr) {
            ListNode* nxt = curr->next;
            // Process current node
            prev = curr;
            curr = nxt;
        }
        return dummy.next;
    }
};
