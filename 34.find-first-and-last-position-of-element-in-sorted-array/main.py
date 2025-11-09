class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = end = -1
        for i, num in enumerate(nums):
            if num == target:
                end = i
                if start == -1:
                    start = i
        return [start, end]