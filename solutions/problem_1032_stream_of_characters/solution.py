"""
Problem 1032: Stream of Characters
================================
Difficulty: Hard
Tags: Array, String, Design, Trie, Data Stream
Pattern: Trie / Prefix Tree

Time Complexity:  O(L) per operation
Space Complexity: O(N * L)
"""

class StreamChecker:
    def __init__(self, words: List[str]):
        # Initialize data structure
        self.words = words

    def query(self, letter: str) -> bool:
        return False

