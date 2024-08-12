# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxpath = 0
        def ib(root):
            if not root: return 0
            ar = ib(root.right)
            al = ib(root.left)
            self.maxpath = max(self.maxpath, al + ar)
            return 1 + max(al, ar)
        ib(root)
        return self.maxpath