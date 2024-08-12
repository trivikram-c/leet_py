# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        return self.isSameTree(root, subRoot)  or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def isSameTree(self, root, newroot):
        if not root and not newroot:
            return True
        elif not root or not newroot:
            return False
        elif root.val != newroot.val:
            return False
        return self.isSameTree(root.right, newroot.right) and self.isSameTree(root.left, newroot.left)