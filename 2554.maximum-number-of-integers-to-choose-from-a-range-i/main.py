class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = list(set(banned))
        banned.sort()
        i = 0
        j = 1

        cur_sum = 0
        cnt=0
        while True:
            if j == banned[i]:
                j+=1
                i = min(i+1, len(banned)-1)
                continue

            if j > n:
                break

            if cur_sum + j > maxSum:
                break
            
            cur_sum += j
            j += 1
            cnt += 1

        return cnt