/*
 * Problem 160: Intersection of Two Linked Lists
 * ============================================
 * Difficulty: Easy
 * Tags: Hash Table, Linked List, Two Pointers
 * Pattern: Two Pointers
 *
 * Time Complexity:  O(m+n)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    ListNode* getIntersectionNode(ListNode* headA, ListNode* headB) {
        // Linked list traversal/manipulation
        ListNode dummy(0);
        dummy.next = headA;
        ListNode* prev = &dummy;
        ListNode* curr = headA;
        while (curr) {
            ListNode* nxt = curr->next;
            // Process current node
            prev = curr;
            curr = nxt;
        }
        return dummy.next;
    }
};
