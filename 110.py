# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def ib(root):
            if not root: return True, 0
            statr, depr = ib(root.right)
            statl, depl = ib(root.left)
            if not statl or not statr: return False, 0
            return abs(depl - depr) <= 1 , 1 + max(depl, depr)
        return ib(root)[0]