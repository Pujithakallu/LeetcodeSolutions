"""
Problem 30: Substring with Concatenation of All Words
=====================================================
Difficulty: Hard
Tags: Hash Table, String, Sliding Window
Pattern: Sliding Window / Hash Map

Time Complexity:  O(n * m * w) where n=len(s), m=num words, w=word len
Space Complexity: O(m)
"""

from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = Counter(words)
        result = []
        for i in range(len(s) - total_len + 1):
            seen = Counter()
            j = 0
            while j < len(words):
                word = s[i + j * word_len: i + (j + 1) * word_len]
                if word in word_count:
                    seen[word] += 1
                    if seen[word] > word_count[word]:
                        break
                else:
                    break
                j += 1
            if j == len(words):
                result.append(i)
        return result
