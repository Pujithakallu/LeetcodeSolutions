"""
Problem 386: Lexicographical Numbers
===================================
Difficulty: Medium
Tags: Depth-First Search, Trie
Pattern: Trie / Prefix Tree

Time Complexity:  O(L) per operation
Space Complexity: O(N * L)
"""

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # Trie-based approach
        trie = {}
        # Build trie from word list
        words = n if isinstance(n, list) else [n]
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
