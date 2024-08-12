# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nextlist = collections.deque([root])
        out = [[root.val]]
        while nextlist:
            outnew = []
            templist = collections.deque()
            while nextlist:
                node = nextlist.popleft()
                if node.left : 
                    templist.append(node.left)
                    outnew.append(node.left.val)
                if node.right : 
                    templist.append(node.right)
                    outnew.append(node.right.val)
            nextlist = templist
            if outnew:
                out.append(outnew) 
        return out