## Merge 2 Sorted Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # head = ListNode()
        # current = head
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         current.next = list1
        #         list1 = list1.next
        #     else:
        #         current.next = list2
        #         list2 = list2.next
        #     current = current.next
        # current.next = list1 or list2
        # return head.next
        head = ListNode()
        temp = head
        if not list1:
            return list2
        if not list2:
            return list1
        while True:
            if list1.val < list2.val:
                temp.val = list1.val
                if not list1.next:
                    temp.next = list2
                    break
                else:
                    temp.next = ListNode()
                    temp = temp.next
                    list1 = list1.next
            else:
                temp.val = list2.val
                if not list2.next:
                    temp.next = list1
                    break
                else:
                    temp.next = ListNode()
                    temp = temp.next
                    list2 = list2.next
        return head
        