"""
Problem 554: Brick Wall
======================
Difficulty: Medium
Tags: Array, Hash Table
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(wall):
            complement = wall - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return 0
