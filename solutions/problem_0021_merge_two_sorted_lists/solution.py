"""
Problem 21: Merge Two Sorted Lists
==================================
Difficulty: Easy
Tags: Linked List, Recursion
Pattern: Two Pointers / Merge

Time Complexity:  O(m+n)
Space Complexity: O(1)
"""

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2
        return dummy.next
