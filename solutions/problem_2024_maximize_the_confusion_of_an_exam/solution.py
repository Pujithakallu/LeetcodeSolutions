"""
Problem 2024: Maximize the Confusion of an Exam
=============================================
Difficulty: Medium
Tags: String, Binary Search, Sliding Window, Prefix Sum
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(answerKey)):
            window[answerKey[right]] += 1
            while len(window) > (k if isinstance(k, int) else len(answerKey)):
                window[answerKey[left]] -= 1
                if window[answerKey[left]] == 0:
                    del window[answerKey[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
