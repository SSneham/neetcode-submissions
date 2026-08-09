# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        lp, l = dummy, head
        for _ in range(left-1):
            lp = l
            l = l.next
        curr = l
        prev = None
        for _ in range(right-left+1):
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        lp.next = prev
        l.next = curr
        return dummy.next
        
