"""
Problem 1603: Design Parking System
=================================
Difficulty: Easy
Tags: Design, Simulation, Counting
Pattern: Design

Time Complexity:  O(1) per operation
Space Complexity: O(n)
"""

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        # Initialize data structure
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        return False

