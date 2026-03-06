# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head 
        while cur:
            cur = cur.next
            length += 1

        n = length - n
        if n == 0:
            return head.next
        
        idx = 1
        cur = head
        while cur:
            if idx == n:
                cur.next = cur.next.next
                return head
            cur = cur.next
            idx += 1