class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        hm = [0 for i in range(n)]
        index = 0
        cnt =1
        #initialize 1th
        hm[0] = 1

        while True:
            index = (index+k*cnt)%n
            hm[index]+=1
            if hm[index] == 2:
                break
            cnt+=1
        
        ans = []
        for i in range(1, n):
            if hm[i] == 0:
                ans.append(i+1)
        return ans
        