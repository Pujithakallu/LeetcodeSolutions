"""
Problem 692: Top K Frequent Words
================================
Difficulty: Medium
Tags: Array, Hash Table, String, Trie, Sorting, Heap (Priority Queue), Bucket Sort, Counting
Pattern: Trie / Prefix Tree

Time Complexity:  O(L) per operation
Space Complexity: O(N * L)
"""

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Trie-based approach
        trie = {}
        # Build trie from word list
        words = words if isinstance(words, list) else [words]
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
