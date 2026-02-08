"""
Problem 297: Serialize and Deserialize Binary Tree
=================================================
Difficulty: Hard
Tags: String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree
Pattern: Tree / DFS / Serialization

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Codec:
    def serialize(self, root):
        vals = []
        def dfs(node):
            if not node:
                vals.append('#')
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(vals)

    def deserialize(self, data):
        vals = iter(data.split(','))
        def dfs():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
