class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n, m, size= sum(set(nums)), sum(nums), len(nums)
        k = (1 + size) * size // 2
        return [m - n, k - n]