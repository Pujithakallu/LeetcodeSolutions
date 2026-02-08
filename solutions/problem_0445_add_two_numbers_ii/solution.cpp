/*
 * Problem 445: Add Two Numbers II
 * ==============================
 * Difficulty: Medium
 * Tags: Linked List, Math, Stack
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
