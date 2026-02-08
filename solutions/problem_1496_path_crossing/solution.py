"""
Problem 1496: Path Crossing
=========================
Difficulty: Easy
Tags: Hash Table, String
Pattern: Hash Map String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Hash map for string/character frequency - O(n) time
        freq = {}
        for ch in path:
            freq[ch] = freq.get(ch, 0) + 1
        # Process frequency map
        for ch, cnt in freq.items():
            if cnt == 1:
                return path.index(ch)
        return False
