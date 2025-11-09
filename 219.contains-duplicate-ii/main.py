class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        size = len(nums)
        for i in range(size): # O(n)
            try:
                if i - dic[nums[i]] <= k:
                    return True
            except:
                pass
            dic[nums[i]] = i

        return False