"""
Problem 1938: Maximum Genetic Difference Query
============================================
Difficulty: Hard
Tags: Array, Hash Table, Bit Manipulation, Depth-First Search, Trie
Pattern: Trie / Prefix Tree

Time Complexity:  O(L) per operation
Space Complexity: O(N * L)
"""

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        # Trie-based approach
        trie = {}
        # Build trie from word list
        words = parents if isinstance(parents, list) else [parents]
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
