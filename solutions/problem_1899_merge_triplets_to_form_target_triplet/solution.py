"""
Problem 1899: Merge Triplets to Form Target Triplet
=================================================
Difficulty: Medium
Tags: Array, Greedy
Pattern: Greedy

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def mergeTriplets(self, triplets, target):
        good = set()
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                for i in range(3):
                    if t[i] == target[i]:
                        good.add(i)
        return len(good) == 3
