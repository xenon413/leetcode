# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import reduce
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        #initialize
        queue = [root]
        nextrow = []
        res = []

        #special case
        if root == None:
            return res
        
        
        while True:
            #break point
            if len(queue) == 0:
                return res
            
            #find row max
            max = (queue[0], queue[0].val)
            for current in queue:
                left = current.left
                right = current.right

                #get next
                if left is not None:
                    nextrow.append(left)
                if right is not None:
                    nextrow.append(right)
            
                #get max
                if current.val > max[1]:
                    max = (current, current.val)
            
            res.append(max[1])

            queue = nextrow[:]
            nextrow = []