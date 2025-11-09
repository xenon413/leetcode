from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        my_list = list(set(arr))
        my_list.sort()

        # set rank
        my_dict = {}
        for i in range(len(my_list)):
            # value/rank
            my_dict[my_list[i]] = i+1
        
        # set answer
        ans = []
        for i in arr:
            ans.append(my_dict[i])
        
        return ans