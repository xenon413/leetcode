class Solution:
    def maxSum(self, nums: List[int]) -> int:
        hash_map = {str(key): [] for key in range(10)}
        max_num = -1

        for num in nums:
            n = str(num)
            max_digit = max(n)
            hash_map[max_digit].append((-num, num))


        for i in hash_map.keys():   
            cur = hash_map[i]
            if len(cur)<2:
                continue
            heapq.heapify(hash_map[i])
            num1 = heapq.heappop(hash_map[i])[1]
            num2 = heapq.heappop(hash_map[i])[1]
            max_num = max(max_num, num1+num2)

        return max_num