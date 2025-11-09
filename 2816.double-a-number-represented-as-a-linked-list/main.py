# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode(0, head)
        head = cur
        while cur.next:
            cur.val += cur.next.val*2//10
            cur.next.val = cur.next.val*2%10
            cur = cur.next
        if head.val == 0:
            return head.next
        return head
            
