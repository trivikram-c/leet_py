# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isbst(root, minthresh, maxthresh):
            if not root: return True
            if root.val <= minthresh or root.val >= maxthresh: return False
            return isbst(root.left, minthresh, root.val) and isbst(root.right, root.val, maxthresh)
        return isbst(root, float('-inf'), float('inf'))    
        