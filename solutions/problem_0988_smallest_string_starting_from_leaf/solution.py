"""
Problem 988: Smallest String Starting From Leaf
==============================================
Difficulty: Medium
Tags: String, Backtracking, Tree, Depth-First Search, Binary Tree
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(root)):
                path.append(root[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
