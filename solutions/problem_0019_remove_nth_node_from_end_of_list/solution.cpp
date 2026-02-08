/*
 * Problem 19: Remove Nth Node From End of List
 * ============================================
 * Difficulty: Medium
 * Tags: Linked List, Two Pointers
 * Pattern: Fast and Slow Pointers
 *
 * Time Complexity:  O(L) where L = list length
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // Linked list traversal/manipulation
        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy;
        ListNode* curr = head;
        while (curr) {
            ListNode* nxt = curr->next;
            // Process current node
            prev = curr;
            curr = nxt;
        }
        return dummy.next;
    }
};
