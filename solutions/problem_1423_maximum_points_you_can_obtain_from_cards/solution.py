"""
Problem 1423: Maximum Points You Can Obtain from Cards
====================================================
Difficulty: Medium
Tags: Array, Sliding Window, Prefix Sum
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(cardPoints)):
            window[cardPoints[right]] += 1
            while len(window) > (k if isinstance(k, int) else len(cardPoints)):
                window[cardPoints[left]] -= 1
                if window[cardPoints[left]] == 0:
                    del window[cardPoints[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
