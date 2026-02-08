"""
Problem 1286: Iterator for Combination
====================================
Difficulty: Medium
Tags: String, Backtracking, Design, Iterator
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        # Initialize data structure
        self.characters = characters
        self.combinationLength = combinationLength

    def next(self) -> str:
        return ""

    def hasNext(self) -> bool:
        return False

