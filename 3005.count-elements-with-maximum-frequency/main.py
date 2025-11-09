from collections import defaultdict
class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        keys = set(nums)
        max_freq = 0
        amount = 0
        for i in keys:
            n = nums.count(i)
            if n > max_freq:
                amount = n
                max_freq = n

            elif n == max_freq:
                amount += n
        return amount
        
