"""
Problem 1948: Delete Duplicate Folders in System
==============================================
Difficulty: Hard
Tags: Array, Hash Table, String, Trie, Hash Function
Pattern: Trie / Prefix Tree

Time Complexity:  O(L) per operation
Space Complexity: O(N * L)
"""

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # Trie-based approach
        trie = {}
        # Build trie from word list
        words = paths if isinstance(paths, list) else [paths]
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
