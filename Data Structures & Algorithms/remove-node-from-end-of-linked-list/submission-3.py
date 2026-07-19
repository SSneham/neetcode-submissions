# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lenn = 0
        curr = head
        while curr:
            lenn += 1
            curr = curr.next
        count = 0

        if lenn == 1: return None
        if n == lenn: return head.next

        curr = head
        k = lenn-n
        while curr:
            count += 1
            if count == k:
                curr.next = curr.next.next
                break
            curr = curr.next
        
        return head