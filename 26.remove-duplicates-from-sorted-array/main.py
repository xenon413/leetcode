class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = list(set(nums))
        temp.sort()
        nums.clear()
        nums.extend(temp)
        return len(nums)