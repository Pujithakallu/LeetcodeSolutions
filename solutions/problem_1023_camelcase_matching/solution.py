"""
Problem 1023: Camelcase Matching
==============================
Difficulty: Medium
Tags: Array, Two Pointers, String, Trie, String Matching
Pattern: Trie / Prefix Tree

Time Complexity:  O(L) per operation
Space Complexity: O(N * L)
"""

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        # Trie-based approach
        trie = {}
        # Build trie from word list
        words = queries if isinstance(queries, list) else [queries]
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
        
        return []
