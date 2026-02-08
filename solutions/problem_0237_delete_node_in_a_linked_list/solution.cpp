/*
 * Problem 237: Delete Node in a Linked List
 * ========================================
 * Difficulty: Medium
 * Tags: Linked List
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
    void deleteNode(int node) {
        // Linked list traversal/manipulation
        ListNode dummy(0);
        dummy.next = node;
        ListNode* prev = &dummy;
        ListNode* curr = node;
        while (curr) {
            ListNode* nxt = curr->next;
            // Process current node
            prev = curr;
            curr = nxt;
        }
        return dummy.next;
    }
};
