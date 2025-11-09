class Solution:
    @staticmethod
    def toSeconds(time:str) -> int:
        h, s = list(map(int, time.split(":")))
        return h*60 + s
    
    def convertTime(self, current: str, correct: str) -> int:
        sep = self.toSeconds(correct) - self.toSeconds(current)
        ans = 0
        
        ans += sep // 60
        sep %= 60

        ans += sep // 15
        sep %= 15

        ans += sep // 5
        sep %= 5

        ans += sep

        return ans