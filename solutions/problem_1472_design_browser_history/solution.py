"""
Problem 1472: Design Browser History
==================================
Difficulty: Medium
Tags: Array, Linked List, Stack, Design, Doubly-Linked List, Data Stream
Pattern: Linked List

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class BrowserHistory:
    def __init__(self, homepage: str):
        # Initialize data structure
        self.homepage = homepage

    def visit(self, url: str) -> None:
        return None

    def back(self, steps: int) -> str:
        return ""

    def forward(self, steps: int) -> str:
        return ""

