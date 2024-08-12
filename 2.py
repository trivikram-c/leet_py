# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        outhead = ListNode()
        temp1 = l1
        temp2 = l2
        tempout = outhead
        carry = 0
        prev = None
        while temp1 or temp2:
            v1 = temp1.val if temp1 else 0
            v2 = temp2.val if temp2 else 0
            su = v1 + v2 + carry
            val = su % 10
            carry = su // 10
            # if not tempout:
            #     tempout = Node(val)
            # else:
            tempout.val = val
            tempout.next = ListNode()
            prev = tempout
            tempout = tempout.next
            temp1 = temp1.next if temp1 else None
            temp2 = temp2.next if temp2 else None
        if not carry:
            prev.next = None
        else:
            tempout.val = carry
        return outhead