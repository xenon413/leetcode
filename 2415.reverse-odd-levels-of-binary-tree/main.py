# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = 0
        nodes = [root]
        while True:
            # reverse using two pointers
            if level%2 == 1:
                i = 0
                j = len(nodes)-1
                while i < j:
                    nodes[i].val, nodes[j].val = nodes[j].val, nodes[i].val
                    i+=1
                    j-=1

            # break point no next level
            if not nodes[0].left:
                break

            # find next level
            next_nodes = []
            for i in nodes:
                next_nodes.append(i.left)
                next_nodes.append(i.right)
            nodes = next_nodes

            level += 1
        return root
            
