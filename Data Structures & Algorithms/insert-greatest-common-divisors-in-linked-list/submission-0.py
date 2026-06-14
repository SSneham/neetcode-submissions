# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            if b>a:
                a,b = b,a
            while b:
                a,b = b,a%b
            return a

        # print(gcd(3,4))
        
        temp = head

        if not temp.next: return temp

        while temp and temp.next:
            new_node = ListNode(gcd(temp.val, temp.next.val))
            # print(new_node.val)
            new_node.next = temp.next
            temp.next = new_node

            temp = new_node.next
        return head



