# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_LL(self, head):
        prev = None
        cur = head
        nxt = head.next 

        while cur:
            nxt = cur.next
            cur.next = prev 
            prev = cur
            cur = nxt 

        return prev

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse_LL(head)
        cur = head

        while cur and cur.next:
            if cur.next.val < cur.val:
                cur.next = cur.next.next

            else:
                cur = cur.next
                
        return self.reverse_LL(head)
