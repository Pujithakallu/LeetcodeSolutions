"""
Problem 68: Text Justification
==============================
Difficulty: Hard
Tags: Array, String, Simulation
Pattern: String Simulation

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def fullJustify(self, words, maxWidth):
        result, line, line_len = [], [], 0
        for word in words:
            if line_len + len(word) + len(line) > maxWidth:
                for i in range(maxWidth - line_len):
                    line[i % (len(line)-1 or 1)] += ' '
                result.append(''.join(line))
                line, line_len = [], 0
            line.append(word)
            line_len += len(word)
        result.append(' '.join(line).ljust(maxWidth))
        return result
