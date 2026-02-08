"""
Problem 2271: Maximum White Tiles Covered by a Carpet
===================================================
Difficulty: Medium
Tags: Array, Binary Search, Greedy, Sliding Window, Sorting, Prefix Sum
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(tiles)):
            window[tiles[right]] += 1
            while len(window) > (carpetLen if isinstance(carpetLen, int) else len(tiles)):
                window[tiles[left]] -= 1
                if window[tiles[left]] == 0:
                    del window[tiles[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
