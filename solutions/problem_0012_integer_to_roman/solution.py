"""
Problem 12: Integer to Roman
============================
Difficulty: Medium
Tags: Hash Table, Math, String
Pattern: Greedy

Time Complexity:  O(1)
Space Complexity: O(1)
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        vals = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),
                (100,'C'),(90,'XC'),(50,'L'),(40,'XL'),
                (10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
        result = []
        for val, sym in vals:
            while num >= val:
                result.append(sym)
                num -= val
        return ''.join(result)
