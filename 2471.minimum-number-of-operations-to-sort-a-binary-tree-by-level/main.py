# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        ans = 0
        level = [root]
        while level:
            s = [x.val for x in level]
            s.sort()
            my_dict = {}
            next_level = []
            for i in range(len(s)):
                # create val/index pair
                my_dict[s[i]] = i

                # get next level
                if level[i].left:
                    next_level.append(level[i].left)
                if level[i].right:
                    next_level.append(level[i].right)


            i = 0
            while i < len(level):
                # check if in order
                if s[i] == level[i].val:
                    i += 1
                    continue
                # print(level[i].val)
                # print(level[my_dict[level[i].val]].val)
                
                # if out of order swap 
                target_index = my_dict[level[i].val]
                level[i].val, level[target_index].val = level[target_index].val, level[i].val
                ans += 1
            level = next_level[:]
        return ans
        