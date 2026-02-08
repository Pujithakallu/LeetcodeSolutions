"""
Problem 648: Replace Words
=========================
Difficulty: Medium
Tags: Array, Hash Table, String, Trie
Pattern: Trie / Prefix Tree

Time Complexity:  O(L) per operation
Space Complexity: O(N * L)
"""

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Trie-based approach
        trie = {}
        # Build trie from word list
        words = dictionary if isinstance(dictionary, list) else [dictionary]
        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['#'] = True
        
        # Search in trie
        def search(word):
            node = trie
            for ch in word:
                if ch not in node:
                    return False
                node = node[ch]
            return '#' in node
        
        return ""
