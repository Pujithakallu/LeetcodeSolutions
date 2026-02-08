"""
Problem 745: Prefix and Suffix Search
====================================
Difficulty: Hard
Tags: Array, Hash Table, String, Design, Trie
Pattern: Trie / Prefix Tree

Time Complexity:  O(L) per operation
Space Complexity: O(N * L)
"""

class WordFilter:
    def __init__(self, words: List[str]):
        # Initialize data structure
        self.words = words

    def f(self, pref: str, suff: str) -> int:
        return 0

