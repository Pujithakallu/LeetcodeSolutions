"""
Problem 2043: Simple Bank System
==============================
Difficulty: Medium
Tags: Array, Hash Table, Design, Simulation
Pattern: Design

Time Complexity:  O(1) per operation
Space Complexity: O(n)
"""

class Bank:
    def __init__(self, balance: List[int]):
        # Initialize data structure
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        return False

    def deposit(self, account: int, money: int) -> bool:
        return False

    def withdraw(self, account: int, money: int) -> bool:
        return False

