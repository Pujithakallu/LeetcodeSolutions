"""
Problem 17: Letter Combinations of a Phone Number
=================================================
Difficulty: Medium
Tags: Hash Table, String, Backtracking
Pattern: Backtracking

Time Complexity:  O(4^n) where n = len(digits)
Space Complexity: O(n)
"""

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        phone = {'2':'abc','3':'def','4':'ghi','5':'jkl',
                 '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        result = []
        def backtrack(idx, path):
            if idx == len(digits):
                result.append(''.join(path))
                return
            for ch in phone[digits[idx]]:
                path.append(ch)
                backtrack(idx + 1, path)
                path.pop()
        backtrack(0, [])
        return result
