# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        
        even = even_head = head.next
        odd = head
        cur = head.next.next
        count = 1

        while cur:
            if count % 2 == 1:
                odd.next = cur
                odd = odd.next
            
            else:
                even.next = cur
                even = even.next

            count += 1
            cur = cur.next

        odd.next = even_head
        even.next = None

        return head