# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        cur = head 
        while cur:
            cur = cur.next
            length += 1

        if length % 2:
            mid = (length + 1) // 2
        else:
            mid = length // 2 + 1

        idx = 1
        cur = head
        while cur:
            if mid == idx:
                return cur
            cur = cur.next
            idx += 1