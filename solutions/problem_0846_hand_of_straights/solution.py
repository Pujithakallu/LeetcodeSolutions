"""
Problem 846: Hand of Straights
=============================
Difficulty: Medium
Tags: Array, Hash Table, Greedy, Sorting
Pattern: Greedy / Hash Map

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

from collections import Counter

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        for card in sorted(count):
            if count[card] > 0:
                need = count[card]
                for i in range(groupSize):
                    if count[card + i] < need:
                        return False
                    count[card + i] -= need
        return True
