class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in set(nums):
            if nums.count(i)!=2:
                return i