/*
 * Problem 2: Add Two Numbers
 * ===========================
 * Difficulty: Medium
 * Tags: Linked List, Math, Recursion
 * Pattern: Linked List Math
 *
 * Time Complexity:  O(max(m,n))
 * Space Complexity: O(max(m,n))
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // Linked list traversal/manipulation
        ListNode dummy(0);
        dummy.next = l1;
        ListNode* prev = &dummy;
        ListNode* curr = l1;
        while (curr) {
            ListNode* nxt = curr->next;
            // Process current node
            prev = curr;
            curr = nxt;
        }
        return dummy.next;
    }
};
