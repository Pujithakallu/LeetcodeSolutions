"""
Problem 690: Employee Importance
===============================
Difficulty: Medium
Tags: Array, Hash Table, Tree, Depth-First Search, Breadth-First Search
Pattern: DFS Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # Initialize data structure
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        return 0

