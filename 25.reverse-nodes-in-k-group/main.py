# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        pre = None
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
            if len(stack) == k:
                start, end = self.reverse(stack)
                stack = []
                if pre:
                    pre.next = start
                    pre = end
                else:
                    pre = end
                    head = start

        pre.next = None
        if stack:
            pre.next = stack[0]

        return head


    def reverse(self, stack:list):
        head = None
        cur = None
        while stack:
            node = stack.pop()
            if cur:
                cur.next = node
                cur = node
            else:
                head = node
                cur = node
        return head, cur#return first and last k
            