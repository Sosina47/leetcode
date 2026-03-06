# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # length = 0
        # cur = head 
        # while cur:
        #     cur = cur.next
        #     length += 1

        # n = length - n
        # dummy = ListNode(-1, head)
        # cur = dummy 
        
        # idx = 0
        # cur = head
        # while cur:
        #     if idx == n:
        #         cur.next = cur.next.next 
        #         return dummy.next
        #     cur = cur.next
        #     idx += 1
        
        dummy = ListNode(-1, head)
        slow = fast = dummy 
        idx = 0
        while fast and idx <= n:
            fast = fast.next
            idx += 1
            
        while fast:
            slow = slow.next
            fast = fast.next
        
        if slow is dummy:
            return head.next

        slow.next = slow.next.next 
        return head
