#For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
#Two binary trees are considered leaf-similar if their leaf value sequence is the same.
#Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            return dfs(root.left) + dfs(root.right)
        return dfs(root1) == dfs(root2)

# in the problem, i use dfs as the main search algorithm to find the leaf, return each leaves from left to right
# and compare the final list result to judge same or not
