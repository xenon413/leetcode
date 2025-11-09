class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        arr = []
        if len(nums) < 1:
            return arr
        first = nums[0]
        string = ''
        
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1] != 1:
                string += str(first)
                if first == nums[i-1]:
                    arr.append(string)
                else:
                    string += '->'+str(nums[i-1])
                    arr.append(string)
                first = nums[i]
                print(first)
                string = ''
        string += str(first)
        if nums.index(first) == len(nums)-1:
            arr.append(string)
        else:
            string += '->'+str(nums[-1])
            arr.append(string)

        return arr