"""
Problem 1797: Design Authentication Manager
=========================================
Difficulty: Medium
Tags: Hash Table, Linked List, Design, Doubly-Linked List
Pattern: Linked List

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class AuthenticationManager:
    def __init__(self, timeToLive: int):
        # Initialize data structure
        self.timeToLive = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        return None

    def renew(self, tokenId: str, currentTime: int) -> None:
        return None

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return 0

