## Reorder List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        plist = []
        tmp = head
        while tmp:
            plist.append(tmp)
            tmp= tmp.next
        l, r = 1, len(plist)-1
        tmp = head
        last_was_l = True
        while l <= r:
            if last_was_l:
                tmp.next = plist[r]
                tmp = tmp.next
                r -= 1
                last_was_l = False
            else:
                tmp.next = plist[l]
                tmp = tmp.next
                l += 1
                last_was_l = True
        tmp.next = None
        