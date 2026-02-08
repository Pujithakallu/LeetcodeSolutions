"""
Problem 2379: Minimum Recolors to Get K Consecutive Black Blocks
==============================================================
Difficulty: Easy
Tags: String, Sliding Window
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(blocks)):
            window[blocks[right]] += 1
            while len(window) > (k if isinstance(k, int) else len(blocks)):
                window[blocks[left]] -= 1
                if window[blocks[left]] == 0:
                    del window[blocks[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
