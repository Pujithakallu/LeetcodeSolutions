"""
Problem 2260: Minimum Consecutive Cards to Pick Up
================================================
Difficulty: Medium
Tags: Array, Hash Table, Sliding Window
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(cards)):
            window[cards[right]] += 1
            while len(window) > (cards if isinstance(cards, int) else len(cards)):
                window[cards[left]] -= 1
                if window[cards[left]] == 0:
                    del window[cards[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
