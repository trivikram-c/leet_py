"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        o2n = {}
        temp = head
        while temp:
            o2n[temp] = Node(temp.val)
            temp = temp.next

        temp = head
        while temp:
            o2n[temp].next = o2n[temp.next] if temp.next else None
            o2n[temp].random = o2n[temp.random] if temp.random else None
            temp = temp.next
        return o2n[head]
        # temp = head
        # while temp:
        #     temp.next = Node(temp.val, temp.next, None)
        #     temp = temp.next.next

        # temp = head
        # nh = head.next
        # while temp:
        #     nextnode = temp.next.next
        #     temp.next.next = nextnode.next if nextnode else None
        #     temp.next.random = temp.random.next if temp.random else None
        #     temp.next = nextnode
        #     temp = temp.next
        # return nh