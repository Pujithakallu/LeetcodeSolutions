"""
Problem 792: Number of Matching Subsequences
===========================================
Difficulty: Medium
Tags: Array, Hash Table, String, Binary Search, Dynamic Programming, Trie, Sorting
Pattern: Trie / Prefix Tree

Time Complexity:  O(L) per operation
Space Complexity: O(N * L)
"""

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Trie-based approach
        trie = {}
        # Build trie from word list
        words = s if isinstance(s, list) else [s]
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
        
        return 0
