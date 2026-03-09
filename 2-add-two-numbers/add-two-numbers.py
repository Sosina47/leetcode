# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1 
        cur2 = l2
        previous = None
        r = 0

        while cur1 and cur2:
            v = cur1.val + cur2.val + r
            cur1.val = v % 10 
            cur2.val = v % 10
            r = v // 10

            previous = cur2
            cur1 = cur1.next
            cur2 = cur2.next

        c1 = False
        prev = None
        while cur1:
            c1 = True

            v = cur1.val + r
            cur1.val = v % 10
            r = v // 10
            
            prev = cur1
            cur1 = cur1.next

        while cur2:
            v = cur2.val + r
            cur2.val = v % 10
            r = v // 10

            prev = cur2
            cur2 = cur2.next

        if r > 0:
            node = ListNode(r)
            if prev:
                prev.next = node
            else:
                previous.next = node

        return l1 if c1 else l2