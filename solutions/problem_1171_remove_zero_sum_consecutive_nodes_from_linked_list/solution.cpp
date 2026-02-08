/*
 * Problem 1171: Remove Zero Sum Consecutive Nodes from Linked List
 * ==============================================================
 * Difficulty: Medium
 * Tags: Hash Table, Linked List
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
    ListNode* removeZeroSumSublists(ListNode* head) {
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
