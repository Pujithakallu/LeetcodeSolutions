"""
Problem 911: Online Election
===========================
Difficulty: Medium
Tags: Array, Hash Table, Binary Search, Design
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        # Initialize data structure
        self.persons = persons
        self.times = times

    def q(self, t: int) -> int:
        return 0

