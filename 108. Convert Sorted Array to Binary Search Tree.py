#Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def tree(start, end):
            if start > end:
                return None
            mid = (end + start) // 2
            root = TreeNode(nums[mid])
            root.left = tree(start, mid-1)
            root.right = tree(mid+1, end)
            return root
        return tree(0, len(nums)-1)

# in a soorted list, each time select the middle element as the root of the tree
# it's left child and right child is the rest part's middle element
