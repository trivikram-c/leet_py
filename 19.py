## Remove Nth element from the end of list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = head
        plist = []
        while tmp:
            plist.append(tmp)
            tmp = tmp.next
        plist.append(None)
        next = plist[-n ]
        if n > len(plist) - 2:
            return plist[1]
        plist[-n-2].next = next
        return head
        