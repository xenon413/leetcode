from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        hq = []
        for i in range(len(nums)):
            # (val, index)
            heapq.heappush(hq, (nums[i], i))

        for _ in range(k):
            cur = heapq.heappop(hq)
            nums[cur[1]]*=multiplier
            heapq.heappush(hq, (cur[0]*multiplier, cur[1]))

        return nums