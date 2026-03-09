# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        left = dummy
        right = dummy.next

        while right and right.next:
            right = right.next.next
            left = left.next

        left.next = left.next.next
        
        return dummy.next