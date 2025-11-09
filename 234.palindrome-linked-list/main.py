class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        curr = head
        arr = []

        while curr is not None:
            arr.append(curr.val)
            curr = curr.next
        
        return arr == arr[::-1]