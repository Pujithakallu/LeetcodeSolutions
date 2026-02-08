"""
Problem 95: Unique Binary Search Trees II
=========================================
Difficulty: Medium
Tags: Dynamic Programming, Backtracking, Tree, Binary Search Tree, Binary Tree
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(n)):
                path.append(n[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
