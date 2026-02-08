"""
Problem 160: Intersection of Two Linked Lists
============================================
Difficulty: Easy
Tags: Hash Table, Linked List, Two Pointers
Pattern: Two Pointers

Time Complexity:  O(m+n)
Space Complexity: O(1)
"""

class Solution:
    def getIntersectionNode(self, headA, headB):
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
