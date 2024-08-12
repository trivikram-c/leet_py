# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        out = []
        def rsv(root, depth):
            if not root:
                return
            if depth > len(out):
                out.append(root.val)
            rsv(root.right, depth +1)
            rsv(root.left, depth +1)
        rsv(root, 1)
        return out
        # if not root:
            # return []
        # out = []
        # rowlist = collections.deque([root])
        # while rowlist:
        #     nextlist = collections.deque()
        #     while rowlist:
        #         node = rowlist.popleft()
        #         if len(rowlist) == 0:
        #             out.append(node.val)
        #         if node.left:  nextlist.append(node.left) 
        #         if node.right: nextlist.append(node.right)
        #     rowlist = nextlist
        # return out