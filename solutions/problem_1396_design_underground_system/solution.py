"""
Problem 1396: Design Underground System
=====================================
Difficulty: Medium
Tags: Hash Table, String, Design
Pattern: Design / Hash Map

Time Complexity:  O(1) per operation
Space Complexity: O(n)
"""

from collections import defaultdict

class UndergroundSystem:
    def __init__(self):
        self.checkins = {}
        self.totals = defaultdict(lambda: [0, 0])

    def checkIn(self, id, stationName, t):
        self.checkins[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        start, t0 = self.checkins.pop(id)
        key = (start, stationName)
        self.totals[key][0] += t - t0
        self.totals[key][1] += 1

    def getAverageTime(self, startStation, endStation):
        total, count = self.totals[(startStation, endStation)]
        return total / count
