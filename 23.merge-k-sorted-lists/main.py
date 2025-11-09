#my first thought was to make a append and go over two list and append to the new list and repeat the process till finish all the list 
#then I thought of doing it in-place to reduce the space complexity but with the same process
 
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def merge(lst1:ListNode, lst2:ListNode):#O(n) # n = lst1 + lst2
        # do inplace 
        if lst1 == None:
            return lst2
        if lst2 == None:
            return lst1
        if lst1.val > lst2.val:# garanteen that lst1[0] < lst2[0]
            lst1, lst2 = lst2, lst1

        iter1 = lst1
        iter2 = lst2
        next = iter1.next

        while iter2 != None:
            if next == None:
                iter1.next = iter2
                break
            if next.val > iter2.val:
                iter1.next = iter2
                iter2 = iter2.next
                iter1.next.next = next
                iter1 = iter1.next
            else:
                iter1 = next
                next = next.next
                if next == None:
                    iter1.next = iter2
                    break
        return lst1

    def mergeKLists(self, lists):
        ans = None
        for i in lists:
            ans = self.merge(ans, i)
        return ans



        