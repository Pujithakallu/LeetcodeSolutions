"""
Problem 2227: Encrypt and Decrypt Strings
=======================================
Difficulty: Hard
Tags: Array, Hash Table, String, Design, Trie
Pattern: Trie / Prefix Tree

Time Complexity:  O(L) per operation
Space Complexity: O(N * L)
"""

class Encrypter:
    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        # Initialize data structure
        self.keys = keys
        self.values = values
        self.dictionary = dictionary

    def encrypt(self, word1: str) -> str:
        return ""

    def decrypt(self, word2: str) -> int:
        return 0

