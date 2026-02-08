"""
Problem 1233: Remove Sub-Folders from the Filesystem
==================================================
Difficulty: Medium
Tags: Array, String, Depth-First Search, Trie
Pattern: Trie / Prefix Tree

Time Complexity:  O(L) per operation
Space Complexity: O(N * L)
"""

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Trie-based approach
        trie = {}
        # Build trie from word list
        words = folder if isinstance(folder, list) else [folder]
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
