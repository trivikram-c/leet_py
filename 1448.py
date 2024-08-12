# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # count = 0
        # maxtn = float('-inf')
        def dfs(root, maxtn):
            if not root:
                return 0
            curr = ( root.val >= maxtn) + 0
            maxtn = max(maxtn, root.val)
            return curr + dfs(root.right, maxtn) + dfs(root.left, maxtn)
        return dfs(root, float('-inf'))