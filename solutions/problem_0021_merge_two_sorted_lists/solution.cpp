/*
 * Problem 21: Merge Two Sorted Lists
 * ==================================
 * Difficulty: Easy
 * Tags: Linked List, Recursion
 * Pattern: Two Pointers / Merge
 *
 * Time Complexity:  O(m+n)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // Linked list traversal/manipulation
        ListNode dummy(0);
        dummy.next = list1;
        ListNode* prev = &dummy;
        ListNode* curr = list1;
        while (curr) {
            ListNode* nxt = curr->next;
            // Process current node
            prev = curr;
            curr = nxt;
        }
        return dummy.next;
    }
};
