# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.head = head
        self.stack = []

        #init
        pre = None
        current = self.head
        self.stack.append(pre)
        n = self.head.next
        

        while True:
            if n is None:
                break

            if current.val < n.val:
                self.remove(pre)
                pre = self.stack[-1]
                if pre is None:
                    current = self.head
                    n = current.next
                else:   
                    current = pre.next
                    n = pre.next.next

            else:
                pre = current
                self.stack.append(pre)
                current = n
                n = current.next

        return self.head
    
    def remove(self, pre=None):
        if pre is None:
            self.head = self.head.next
        else:
            pre.next = pre.next.next
            self.stack.pop()
