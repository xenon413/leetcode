from collections import defaultdict
from typing import List
class Solution:
    def findScore(self, nums: List[int]) -> int:
        res = 0
        value_index = defaultdict(list)
        marked = [0 for i in nums]
        for i in range(len(nums)):
            value_index[nums[i]].append(i)
        
        check = list(set(nums))
        check.sort()
        for i in check:
            queue = value_index[i]
            for k in queue:
                if marked[k] == 0:
                    res += nums[k]
                    marked[k] = 1
                    if k-1 >= 0:
                        marked[k-1] = 1
                    if k+1 < len(marked):
                        marked[k+1] = 1
        return res