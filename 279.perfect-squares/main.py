class Solution:
    dp = {}
    def numSquares(self, n: int) -> int:
        return self.recursive(n)
    def recursive(self, n: int) -> int:
        if n in self.dp.keys():
            return self.dp[n] 
        if n <= 3:
            return n
        max = int(n**0.5)
        min_num = -1
        for start in range(max, max//2-1, -1):
            square = start**2
            cnt = self.recursive(n % square) + n//square
            if min_num == -1:
                min_num = cnt
            if min_num > cnt:
                min_num = cnt
        self.dp[n] = min_num
        return min_num